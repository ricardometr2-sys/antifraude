import flet as ft

from diabetes_view import DiabetesView
from diabetes_controller import DiabetesController

def main(page: ft.Page):

    # CREAR VISTA
    vista = DiabetesView(page)

    # CREAR CONTROLADOR
    controlador = DiabetesController(vista)

    # EVENTOS
    vista.btn_estadisticas.on_click = (
        controlador.mostrar_estadisticas
    )

    vista.btn_riesgo.on_click = (
        controlador.mostrar_riesgo
    )

    # MOSTRAR INTERFAZ
    page.add(
        vista.construir()
    )

# EJECUTAR APP
ft.app(target=main)