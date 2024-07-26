import flet as ft
from flet import *
import requests
import json


def login_view(page: Page):
    def login(e):
        data = {"username": username_field.value, "password": password_field.value}
        print(data)
        url = "http://127.0.0.1:8000/account/api/token/"
        req = requests.post(url, data)
        print(req.text)
        if req.status_code == 200:
            res = json.loads(req.text)
            token = res['token']
            res['token'] = f'token {res['token']}'
            page.session.set("user_data", res)
            page.session.set("logged_in", "True")
            page.go('/')
        else:
            error_message.visible = True
            page.update()

    page.title = "Login"
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER

    username_field = TextField(
        hint_text="Username",
        border='underline',
        border_color='grey',
        prefix_icon=icons.PERSON_2,
        prefix_style=TextStyle(color="blue"),
        text_style=TextStyle(color='black'),
        hint_style=TextStyle(size=16, color='grey')
    )

    password_field = TextField(
        hint_text="Password",
        border='underline',
        border_color='grey',
        password=True,
        prefix_icon=icons.LOCK,
        prefix_style=TextStyle(color="blue"),
        text_style=TextStyle(color='black'),
        hint_style=TextStyle(size=16, color='grey')
    )

    error_message = Text(
        "Invalid username or password.",
        color="red",
        style=TextStyle(size=16, weight=FontWeight.BOLD),
        visible=False
    )

    page.add(
        Container(
            content=Column(
                alignment=MainAxisAlignment.CENTER,
                controls=[
                    Stack(
                        controls=[
                            Container(
                                rotate=Rotate(1.03 * 3.14),
                                width=page.window_width * 0.7,
                                height=page.window_height * 0.65,
                                bgcolor="white",
                                opacity=0.6,
                                border_radius=25,
                            ),
                            Container(
                                content=Column(
                                    alignment=MainAxisAlignment.SPACE_AROUND,
                                    controls=[
                                        Row(
                                            vertical_alignment=CrossAxisAlignment.CENTER,
                                            alignment=MainAxisAlignment.CENTER,
                                            controls=[
                                                Text(
                                                    "Login",
                                                    color="black",
                                                    text_align=TextAlign.CENTER,
                                                    style=TextStyle(
                                                        size=25,
                                                        weight=FontWeight.BOLD,
                                                    ),
                                                ),
                                            ],
                                        ),
                                        Column(
                                            controls=[
                                                Row(
                                                    wrap=True,
                                                    controls=[username_field],
                                                ),
                                                Row(
                                                    wrap=True,
                                                    controls=[password_field],
                                                ),
                                                Row(
                                                    controls=[error_message],
                                                ),
                                            ],
                                        ),
                                        ElevatedButton(
                                            on_click=login,
                                            content=Text(
                                                "Login",
                                                size=18,
                                                color=ft.colors.WHITE,
                                                weight=FontWeight.BOLD
                                            ),
                                            bgcolor=ft.colors.BLUE,
                                            width=page.window_width * 0.7,
                                            height=50,
                                        ),
                                        TextButton(
                                            on_click=lambda e: page.go('/register'),
                                            content=Text(
                                                "Register",
                                                size=18,
                                                color=ft.colors.BLUE,
                                            ),
                                            width=page.window_width * 0.7,
                                            height=50,
                                        )
                                    ],
                                ),
                                alignment=alignment.center,
                                padding=20,
                                width=page.window_width * 0.7,
                                height=page.window_height * 0.65,
                                bgcolor="#ebf0f0",
                                border_radius=25,
                            ),
                        ],
                    ),
                ],
            ),
            alignment=alignment.center,
            border_radius=25,
            width=page.window_width,
            height=page.window_height * 0.9,
            image_fit="fill",
            image_src="assets/bg.jpg",
            padding=10,
        ),
    )


# Sample code to initialize and run the page
if __name__ == "__main__":
    ft.app(target=login_view)
