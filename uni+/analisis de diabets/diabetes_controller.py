import flet as ft

from diabetes_model import DiabetesModel


class DiabetesController:

    def __init__(self, vista):

        self.vista = vista
        self.modelo = DiabetesModel()

    # MOSTRAR ESTADÍSTICAS
    def mostrar_estadisticas(self, e):

        total = self.modelo.total_pacientes()

        glucosa = self.modelo.promedio_glucosa()

        diabetes = self.modelo.pacientes_diabetes()

        edad = self.modelo.promedio_edad_diabetes()

        embarazos = (
            self.modelo.promedio_embarazos_diabetes()
        )

        self.vista.texto_resultado.value = f"""
Total pacientes: {total}

Promedio glucosa: {glucosa}

Edad promedio: {edad}

Pacientes con diabetes: {diabetes}

Promedio embarazos con diabetes: {embarazos}
"""

        self.vista.page.update()

    # MOSTRAR PACIENTES DE RIESGO
    def mostrar_riesgo(self, e):

        self.vista.limpiar_tabla()

        riesgo = self.modelo.pacientes_riesgo()

        for _, fila in riesgo.iterrows():

            tarjeta = ft.Container(

            content=ft.Column(
                controls=[

                    ft.Text(
                        f"Glucosa: {fila['Glucose']}"
                    ),

                    ft.Text(
                        f"BMI: {fila['BMI']}"
                    ),

                    ft.Text(
                        f"Edad: {fila['Age']}"
                    )

                ]
            ),

            padding=10,

            border=ft.border.Border(
                top=ft.BorderSide(1, "gray"),
                bottom=ft.BorderSide(1, "gray"),
                left=ft.BorderSide(1, "gray"),
                right=ft.BorderSide(1, "gray")
            ),

            border_radius=10
        )

            self.vista.tabla.content.controls.append(
                tarjeta
            )
            
        self.vista.page.update()