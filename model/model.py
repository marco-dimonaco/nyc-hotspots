import networkx as nx
from database.DAO import DAO
from geopy.distance import distance
import random
import copy


class Model:
    def __init__(self):
        self._bestComp = []
        self._maxVicini = []
        self._grafo = nx.Graph()

    def buildGraph(self, provider, distanza):
        self._grafo.clear()
        allNodes = DAO.getAllLocations(provider)
        self._grafo.add_nodes_from(allNodes)
        self.addEdges(provider, distanza)
        return True

    def addEdges(self, provider, distanza):
        allConnessioni = DAO.getAllConnessioni(provider)
        for c1 in allConnessioni:
            for c2 in allConnessioni:
                if c1.Location != c2.Location:
                    dist = distance((c1.Latitude, c1.Longitude), (c2.Latitude, c2.Longitude)).km
                    if dist < distanza:
                        self._grafo.add_edge(c1.Location, c2.Location, weight=dist)

    def getMaxVicini(self):
        nVicini = []
        listaViciniMax = []
        for n in self._grafo.nodes:
            nVicini.append(len(list(self._grafo.neighbors(n))))
        maxVicini = max(nVicini)
        for n in self._grafo.nodes:
            if len(list(self._grafo.neighbors(n))) == maxVicini:
                listaViciniMax.append(n)
                self._maxVicini.append(n)
        return listaViciniMax, maxVicini

    def getPath(self, target, s):
        # caching con variabili della classe (percorso migliore e peso maggiore)
        self._bestComp = []
        nodo = self._maxVicini[random.randint(0, len(self._maxVicini)-1)]
        # inizializzo il parziale con il nodo iniziale
        parziale = [nodo]
        self._ricorsione(parziale, target, s)
        return self._bestComp

    def _ricorsione(self, parziale, target, s):
        # verifico se soluzione è migliore di quella salvata in cache
        if parziale[-1] == target:
            if len(parziale) > len(self._bestComp):
                self._bestComp = copy.deepcopy(parziale)
            return
        # verifico se posso aggiungere un altro elemento
        for a in self._grafo.neighbors(parziale[-1]):
            if a not in parziale and s not in a:
                parziale.append(a)
                self._ricorsione(parziale, target, s)
                parziale.pop()  # rimuovo l'ultimo elemento aggiunto: backtracking

    def getAllProviders(self):
        return DAO.getAllProviders()

    def printGraphDetails(self):
        return f"Vertici: {len(self._grafo.nodes)}; Archi: {len(self._grafo.edges)}"
