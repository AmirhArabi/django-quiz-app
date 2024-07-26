import flet as ft
from flet import Page, Container, Column, Row, Stack, Text, TextField, ElevatedButton, icons, alignment, \
    MainAxisAlignment, CrossAxisAlignment, FontWeight, TextStyle, TextAlign, Rotate, ButtonStyle
import requests
import json


def register_view(page: Page):
    def register(e):
        data = {
            "username": username_field.value,
            "password": password_field.value,
            "password2": password_field2.value,
            "email": email_field.value,
            "last_name": lastn_field.value,
            "first_name": firstn_field.value,

        }
        url = "http://127.0.0.1:8000/account/api/register/"
        req = requests.post(url, data)
        print(req.status_code)
        print(req.text)
        if req.status_code in [200, 201]:
            res = json.loads(req.text)
            token = res['token']
            res['profile_image'] = "https://uploadkon.ir/uploads/ddb016_24pi.jpg"
            res['token'] = f'token {res['token']}'
            page.session.set("user_data", res)
            page.session.set("logged_in", "True")
            page.go('/')
        else:
            error_message.visible = True

            page.update()
    page.title = "Register"
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

    password_field2 = TextField(
        hint_text="Password",
        border='underline',
        border_color='grey',
        password=True,
        prefix_icon=icons.LOCK,
        prefix_style=TextStyle(color="blue"),
        text_style=TextStyle(color='black'),
        hint_style=TextStyle(size=16, color='grey')
    )

    email_field = TextField(
        hint_text="Email",
        border='underline',
        border_color='grey',
        prefix_icon=icons.EMAIL_ROUNDED,
        prefix_style=TextStyle(color="blue"),
        text_style=TextStyle(color='black'),
        hint_style=TextStyle(size=16, color='grey')
    )

    firstn_field = TextField(
        hint_text="First Name",
        border='underline',
        border_color='grey',
        prefix_icon=icons.PERSON_2,
        prefix_style=TextStyle(color="blue"),
        text_style=TextStyle(color='black'),
        hint_style=TextStyle(size=16, color='grey')
    )

    lastn_field = TextField(
        hint_text="Last Name",
        border='underline',
        border_color='grey',
        prefix_icon=icons.PERSON_2,
        prefix_style=TextStyle(color="blue"),
        text_style=TextStyle(color='black'),
        hint_style=TextStyle(size=16, color='grey')
    )

    error_message = Text(
        "Cant register now please try again.",
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
                                                    wrap=True,
                                                    controls=[password_field2],
                                                ),
                                                Row(
                                                    wrap=True,
                                                    controls=[email_field],
                                                ),
                                                Row(
                                                    wrap=True,
                                                    controls=[firstn_field],
                                                ),
                                                Row(
                                                    wrap=True,
                                                    controls=[lastn_field],
                                                ),
                                                Row(
                                                    controls=[error_message],
                                                ),
                                            ],
                                        ),
                                        ElevatedButton(
                                            on_click=register,
                                            content=Text(
                                                "register",
                                                size=18,
                                                color=ft.colors.WHITE,
                                                weight=FontWeight.BOLD
                                            ),
                                            bgcolor=ft.colors.BLUE,
                                            width=page.window_width * 0.7,
                                            height=50,
                                        ),
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
    ft.app(target=register_view)
