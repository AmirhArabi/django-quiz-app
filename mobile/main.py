import flet as ft
from router import route


def main(page: ft.Page):
    page.window_width = 390
    page.window_height = 850
    page.platform = "ios"
    page.padding = 10
    page.bgcolor = "#f1f1f1"
    page.on_route_change = lambda e: route(page)
    page.go(page.route)


ft.app(target=main)
