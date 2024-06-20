import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
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
        self._view.update_page()

    def analizza(self, e):
        listaViciniMax, maxVicini = self._model.getMaxVicini()
        for nodo in listaViciniMax:
            self._view.txt_result.controls.append(ft.Text(f"{nodo}, numero vicini = {maxVicini}"))
        self._view.update_page()

    def fillDDProvider(self):
        for p in self._model.getAllProviders():
            self._view.dd_provider.options.append(ft.dropdown.Option(p))
        self._view.update_page()
