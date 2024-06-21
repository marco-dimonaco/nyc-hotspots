import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._btnAnalizzaGrafo = None
        self.txtField_distance = None
        self.txt_distance = None
        self.txt_provider = None
        self._btnCreaGrafo = None
        self.dd_provider = None
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("ESAME 18/01/2023 NYC-Hotspots", color="blue", size=24)
        self._page.controls.append(self._title)

        # ROW 1
        self.txt_provider = ft.Text("Provider (p): ")
        self.dd_provider = ft.Dropdown(label="Provider", width=500)
        self._controller.fillDDProvider()
        self._btnCreaGrafo = ft.ElevatedButton(text="Crea Grafo", on_click=self._controller.handleGraph, width=300)

        row1 = ft.Row([self.txt_provider, self.dd_provider, self._btnCreaGrafo],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        # ROW 2
        self.txt_distance = ft.Text("Distanza (x): ")
        self.txtField_distance = ft.TextField(label="Distanza", width=500)
        self._btnAnalizzaGrafo = ft.ElevatedButton(text="Analizza Grafo", on_click=self._controller.analizza, width=300)

        row2 = ft.Row([self.txt_distance, self.txtField_distance, self._btnAnalizzaGrafo],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        # ROW3
        self._txtInStringa = ft.TextField(label="Stringa")
        self._btnSetPercorso = ft.ElevatedButton(text="Calcola Percorso",
                                                 on_click=self._controller.handleGetPercorso)
        row3 = ft.Row([
            ft.Container(self._txtInStringa, width=300),
            ft.Container(self._btnSetPercorso, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)
        self._ddTarget = ft.Dropdown(label="Target")
        row4 = ft.Row([
            ft.Container(self._ddTarget, width=300)])
        self._page.controls.append(row4)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
