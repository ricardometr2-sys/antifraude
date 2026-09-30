import flet as ft

class EnfermedadView:

    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Dashboard Enfermedades"

        self.page.window_width = 1200  # type: ignore[attr-defined]
        self.page.window_height = 800  # type: ignore[attr-defined]

        self.page.scroll = ft.ScrollMode.AUTO

        #===================================
        #BOTONES
        #===================================
        self.btn_barras = (
            ft.ElevatedButton(
                "Gráfica de Barras"
            )
        )

        self.btn_estadisticas = (
            ft.ElevatedButton(
                "Estadísticas"
            )
        )

        self.btn_riesgo = (
            ft.ElevatedButton(
                "Pacientes de Riesgo"
            )
        )

        self.btn_mayores = (
            ft.ElevatedButton(
                "Pacientes Mayores"
            )
        )

        #===================================
        #RESULTADOS
        #===================================

        self.resultados = ft.Text(
            size=18
        )

    #TABLA
        self.tabla = ft.DataTable(
            columns=[
                ft.DataColumn(
                    label=ft.Text("Glucosa")
                ),

                ft.DataColumn(
                    label=ft.Text("BMI")
                ),

                ft.DataColumn(
                    label=ft.Text("Age")
                ),

                ft.DataColumn(
                    label=ft.Text("Outcome")
                )
            ],
            rows=[]
        )

    #===================================
    # interfaz
    # ===================================
    def construir(self):

        return ft.Column(
            controls=[
                ft.Text(
                    "Sistema de visualización",
                    size=32,
                    weight=ft.FontWeight.BOLD
                ),

                ft.Row(
                    controls=[
                        self.btn_barras,
                        self.btn_estadisticas,
                        self.btn_riesgo,
                        self.btn_mayores
                    ],
                ),

                ft.Divider(),
                self.resultados,
                self.tabla
            ],

            spacing=20
        )

