import flet as ft 

class DiabetesView: 

    def __init__(self, page: ft.Page):

        self.page = page 

        # CONFIGURACIÓN
        self.page.title = "Análisis Dataset Diabetes"

        self.page.window_width = 800 
        self.page.window_height = 700 
        self.page.padding = 20 

        # BOTONES
        self.btn_estadisticas = ft.ElevatedButton(
        "Mostrar estadísticas",
        icon=ft.Icons.BAR_CHART,
        bgcolor="blue",
        color="white"
    )

        self.btn_riesgo = ft.ElevatedButton(
        "Pacientes de riesgo",
        icon=ft.Icons.WARNING,
        bgcolor="red",
        color="white"
    )

        #Color de fondo de la ventana
        self.page.bgcolor = "#585DDA"

        # RESULTADOS
# RESULTADOS
        self.texto_resultado = ft.Text(
            size=18
        )

        self.resultado = ft.Container(
            content=self.texto_resultado,
            bgcolor="white",
            padding=20,
            border_radius=15
        )

        self.tabla = ft.Container(

            content=ft.Row(
                wrap=True
            ),

            bgcolor="cyan",
            padding=20,
            border_radius=15
        )

    # CONSTRUIR INTERFAZ
    def construir(self):

        return ft.Column(
            controls=[
                ft.Text(
                    "Sistema de Análisis Diabetes",
                    size=30,
                    weight=ft.FontWeight.BOLD
                ),

                ft.Divider(),

                ft.Row(
                    controls=[
                        self.btn_estadisticas,
                        self.btn_riesgo
                    ]
                ),

                ft.Divider(),

                self.resultado,
                self.tabla
            ],

            spacing=20
        )

    # LIMPIAR TABLA
    def limpiar_tabla(self):

        self.tabla.content.controls.clear()