import flet as ft
import matplotlib.pyplot as plt

from modelo.enfermedad_model import (
    EnfermedadModel
)

class EnfermedadController:

    def __init__(self, vista):
        self.vista = vista
        self.modelo = EnfermedadModel()

#=========================================================
#MOSTRAR ESTADISTICAS   
#=========================================================  
    def mostrar_estadisticas(self, e):
        total = (
            self.modelo.total_pacientes()
        )
        glucosa = (
            self.modelo.promedio_glucosa()
        )
        bmi = (
            self.modelo.promedio_bmi()
        )
        diabetes = (
            self.modelo.pacientes_diabetes()
        )
        sanos = (
            self.modelo.pacientes_sanos()
        )

        self.vista.resultados.value = f"""
Total de pacientes: {total}
Promedio de glucosa: {glucosa:.2f}
Promedio de BMI: {bmi:.2f}
Pacientes con diabetes: {diabetes}
Pacientes sanos: {sanos}
"""
        
        self.vista.page.update()

#=========================================================
#GRAFICA
#=========================================================  
        datos = [
            diabetes,
            sanos
        ]

        etiquetas = [
            "Diabetes",
            "Sanos"
        ]

        plt.pie(
            datos,
            labels=etiquetas,
            autopct="%1.1f%%"
        )
        plt.title(
            "Pacientes con y sin diabetes"
        )

        plt.show()

#=========================================================
#TABLA PACIENTES DE RIESGO
#========================================================= 

    def mostrar_riesgo(self, e):
        self.vista.tabla.rows.clear()

        datos = (
            self.modelo.pacientes_de_riesgo()
        )

        for _, fila in datos.iterrows():
            self.vista.tabla.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(
                            ft.Text(str(fila["Glucose"]))
                        ),
                        ft.DataCell(
                            ft.Text(str(fila["BMI"]))
                        ),
                        ft.DataCell(
                            ft.Text(str(fila["Age"]))
                        ),
                        ft.DataCell(
                            ft.Text(str(fila["Outcome"]))
                        ),
                    ]
                )
            )

        self.vista.page.update()

#=========================================================
#TABLA PACIENTES MAYORES
#========================================================= 

    def mostrar_mayores(self, e):
        self.vista.tabla.rows.clear()

        datos = (
            self.modelo.pacientes_mayores()
        )

        for _, fila in datos.iterrows():
            self.vista.tabla.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(
                            ft.Text(str(fila["Glucose"]))
                        ),
                        ft.DataCell(
                            ft.Text(str(fila["BMI"]))
                        ),
                        ft.DataCell(
                            ft.Text(str(fila["Age"]))
                        ),
                        ft.DataCell(
                            ft.Text(str(fila["Outcome"]))
                        ),
                    ]
                )
            )

        self.vista.page.update()

    #=========================================================
    #BARRAS 
    #=========================================================

    def mostrar_barras(self, e):
        total = (
            self.modelo.total_pacientes()
        )
        glucosa = (
            self.modelo.pacientes_glucosa_elevada()
        )
        bmi = (
            self.modelo.pacientes_bmi_elevado()
        )
        diabetes = (
            self.modelo.pacientes_diabetes()
        )
        sanos = (
            self.modelo.pacientes_sanos()
        )

        self.vista.resultados.value = f"""
Total de pacientes: {total}
Pacientes con glucosa elevada: {glucosa}
Pacientes con BMI elevado: {bmi}
Pacientes con diabetes: {diabetes}
Pacientes sanos: {sanos}
"""
        
        self.vista.page.update()

        datos = [
            diabetes,
            sanos,
            glucosa,
            bmi
        ]

        etiquetas = [
            "Diabetes",
            "Sanos",
            "Glucosa elevada",
            "BMI elevado"
        ]

        plt.bar(
            etiquetas,
            datos,
            color=['lightcoral', 'lightblue', 'lightgreen', 'lightyellow']
        )
        plt.title(
            "Pacientes con diabetes, sanos, glucosa elevada y BMI elevado"
        )

        plt.show()

