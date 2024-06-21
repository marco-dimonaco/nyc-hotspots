import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self.maxVicini = None
        self._selected_target = None
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleGraph(self, e):
        provider = self._view.dd_provider.value
        if provider is None:
            print("Seleziona un provider")
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Seleziona un provider."))
            self._view.update_page()
            return

        soglia = self._view.txtField_distance.value
        if soglia == "":
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Distanza non inserita."))
            self._view.update_page()
            return
        try:
            sogliaFloat = float(soglia)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Attenzione, soglia inserita non numerica."))
            self._view.update_page()
            return

        self._model.buildGraph(provider, sogliaFloat)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(
            ft.Text(f"Grafo correttamente creato. {self._model.printGraphDetails()}"))
        self.fillDDTarget()
        self._view.update_page()

    def analizza(self, e):
        listaViciniMax, self.maxVicini = self._model.getMaxVicini()
        for nodo in listaViciniMax:
            self._view.txt_result.controls.append(ft.Text(f"{nodo}, numero vicini = {self.maxVicini}"))
        self._view.update_page()

    def fillDDProvider(self):
        for p in self._model.getAllProviders():
            self._view.dd_provider.options.append(ft.dropdown.Option(p))
        self._view.update_page()

    def fillDDTarget(self):
        nodi = self._model._grafo.nodes
        for n in nodi:
            self._view._ddTarget.options.append(ft.dropdown.Option(text=n, data=n, on_click=self.readDDTarget))
        self._view.update_page()
    def readDDTarget(self, e):
        if e.control.data is None:
            self._selected_target = None
        else:
            self._selected_target = e.control.data

    def handleGetPercorso(self, e):
        self._view.txt_result.controls.clear()
        if len(self._model._grafo.nodes) == 0:
            self._view.txt_result.controls.append(ft.Text("Creare un grafo!", color='red'))
            self._view.update_page()
            return
        if self._selected_target is None:
            self._view.txt_result.controls.append(ft.Text("Selezionare una località!", color='red'))
            self._view.update_page()
            return
        if self.maxVicini is None:
            self._view.txt_result.controls.append(ft.Text("Analizzare il grafico!", color='red'))
            self._view.update_page()
            return
        if self._view._txtInStringa.value is None or self._view._txtInStringa.value == '':
            self._view.txt_result.controls.append(ft.Text("Inserire una stringa!", color='red'))
            self._view.update_page()
            return
        componenti = self._model.getPath(self._selected_target, str(self._view._txtInStringa.value))
        if componenti:
            for c in componenti:
                self._view.txt_result.controls.append(ft.Text(f"{c}"))
            self._view.update_page()
            return
        else:
            self._view.txt_result.controls.append(ft.Text("Nessun percorso trovato!", color='red'))
            self._view.update_page()
            return
