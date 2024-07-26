import flet as ft
from flet import *
from utils.utils import MainNavBar


def home_view(page: ft.Page):
    page.title = "Home"
    user = page.session.get('user_data')
    print(user['username'])
    page.navigation_bar = MainNavBar(page)

    def show_image_in_dialog(page: ft.Page, image_src: str):
        dialog = ft.AlertDialog(
            modal=False,
            content=ft.Image(src=user['profile_image'], border_radius=25, fit="fill"),
            bgcolor=ft.colors.with_opacity(0.5, ft.colors.BLACK),
        )
        page.add(dialog)
        dialog.open = True

    class ImageContainer(Container):
        def __init__(self, *args, image_src=None, **kwargs):
            super().__init__(*args, **kwargs)
            self.image_src = image_src

    def get_banner(page: ft.Page):
        names = ["Earth.png", "Mind.png", "History.png", "Code.png"]
        items = []
        for i in names:
            c = ImageContainer(
                width=270,
                height=250,
                image_src="assets/{}".format(i),
                image_fit="fill",
                alignment=alignment.center
            )
            c.on_click = (lambda current_container: lambda e: set_quiz_type(page, current_container))(c)
            items.append(c)

        return items

    def set_quiz_type(page: ft.Page, current_container: ImageContainer):
        quiz_type = current_container.image_src.split('/')[-1].replace('.png', '')
        page.session.set('quiz_type', quiz_type)
        page.go('/quiz')

    def on_scroll(event: ft.OnScrollEvent):
        print(f"Scrolled to position: {event}")

    page.add(
        Container(
            content=Column(
                [
                    Container(
                        height=page.window_height * 0.2,
                        width=page.window_width * 0.95,
                        padding=10,
                        border_radius=BorderRadius(bottom_left=25, bottom_right=20, top_right=0, top_left=0),
                        content=Column(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                Text(
                                    "QWIZARD",
                                    style=TextStyle(
                                        color=colors.BLACK,
                                        weight="bold",
                                        size=30
                                    )
                                ),
                                Container(
                                    height=20
                                ),
                                Row(
                                    vertical_alignment=MainAxisAlignment.CENTER,
                                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                                    controls=[
                                        Text("Hi, {}👋🏻".format(user['username']),
                                             style=TextStyle(
                                                 color="black",
                                                 weight="bold",
                                                 size=18
                                             )
                                             ),
                                        Container(
                                            width=60,
                                            height=60,
                                            image_src=user['profile_image'],
                                            border_radius=20,
                                            on_click=lambda e: show_image_in_dialog(page, user['profile_image'])
                                        )
                                    ]
                                ),
                            ]
                        )
                    ),

                    Container(
                        padding=10,
                        border_radius=BorderRadius(top_left=25, top_right=25, bottom_left=0, bottom_right=0),
                        bgcolor="White",
                        shadow=ft.BoxShadow(
                            spread_radius=1,
                            blur_radius=20,
                            color=ft.colors.BLUE_GREY_300,
                            offset=ft.Offset(0, 0),
                            blur_style=ft.ShadowBlurStyle.OUTER
                        ),
                        content=Column(
                            controls=[
                                Container(
                                    width=400,
                                    height=300,
                                    # border_radius=20,
                                    content=ft.Column(
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        controls=[
                                            Row(
                                                scroll=ScrollMode.ALWAYS,
                                                on_scroll_interval=on_scroll,
                                                controls=get_banner(page),
                                                expand=True
                                            )
                                        ]
                                    ),
                                ),
                                Container(
                                    height=200,
                                    width=page.window_width * 0.95,
                                    image_src="assets/banner.png"
                                ),
                            ]
                        )
                    )
                ],
                alignment="start",

                horizontal_alignment="center"
            ),
            alignment=alignment.center,
            # border_radius=25,
            padding=-5,
            width=page.window_width,
            height=page.window_height * 0.9 - 60,


        )
    )
