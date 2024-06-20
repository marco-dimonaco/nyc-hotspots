import networkx as nx
from database.DAO import DAO
from geopy.distance import distance


class Model:
    def __init__(self):
        self._grafo = nx.Graph()

    def buildGraph(self, provider, distanza):
        allNodes = DAO.getAllLocations(provider)
        self._grafo.add_nodes_from(allNodes)
        self.addEdges(provider, distanza)
        return True

    def addEdges(self, provider, distanza):
        allConnessioni = DAO.getAllConnessioni(provider)
        for edge in allConnessioni:
            dist = distance((edge.lat1, edge.lon1), (edge.lat2, edge.lon2)).km
            if dist <= distanza:
                self._grafo.add_edge(edge.l1, edge.l2, weight=dist)

    def getMaxVicini(self):
        nVicini = []
        listaViciniMax = []
        for n in self._grafo.nodes:
            nVicini.append(len(list(self._grafo.neighbors(n))))
        maxVicini = max(nVicini)
        for n in self._grafo.nodes:
            if len(list(self._grafo.neighbors(n))) == maxVicini:
                listaViciniMax.append(n)
        return listaViciniMax, maxVicini






    def getAllProviders(self):
        return DAO.getAllProviders()

    def printGraphDetails(self):
        return f"Vertici: {len(self._grafo.nodes)}; Archi: {len(self._grafo.edges)}"
