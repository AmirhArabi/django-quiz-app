import flet as ft
import views.home_view
import views.login_view
import views.quiz_view
import views.register_view


def route(page: ft.Page):
    page.clean()
    logged_in = page.session.get("logged_in") == "True"

    if not logged_in and page.route != '/login' and page.route != '/register':
        page.go('/login')
        return

    if page.route == '/':
        views.home_view.home_view(page)
    elif page.route == '/login':
        views.login_view.login_view(page)
    elif page.route == '/logout':
        page.session.set("logged_in", "False")
        page.go('/login')
    elif page.route == '/quiz':
        views.quiz_view.quiz_view(page)
    elif page.route == "/register":
        views.register_view.register_view(page)
    else:
        return print("Page Not Found")