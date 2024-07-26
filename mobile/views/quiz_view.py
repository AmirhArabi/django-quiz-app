from utils.utils import get_qustions
import flet as ft
from flet import *
import requests


class QuizApp:
    def __init__(self, page):
        self.selected_option = None
        self.answers = None
        self.answer_list = []
        self.quiz_type = page.session.get('quiz_type')
        self.radio_group = None
        self.page = page
        self.page.horizontal_alignment = CrossAxisAlignment.CENTER
        self.current_question_index = 0
        self.questions = get_qustions(page, self.quiz_type)
        self.score = 0

    def next_question(self):
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.show_question()
        else:
            self.update_score()
            self.show_score()

    def on_option_select(self, option, btn):
        self.selected_option = option
        for row in self.answers.controls:
            for button in row.controls:
                button.bgcolor = colors.INDIGO_ACCENT_700
        btn.bgcolor = "Green"
        self.page.update()

    def show_question(self):
        question = self.questions[self.current_question_index]
        self.page.controls.clear()

        self.answers = Column(
            controls=[
                Row(
                    alignment=MainAxisAlignment.SPACE_EVENLY,
                    vertical_alignment=MainAxisAlignment.CENTER,
                    controls=[
                        ElevatedButton(
                            content=Container(
                                Text(
                                    question['option1'],
                                    rtl=True,
                                    text_align=TextAlign.CENTER,
                                    style=TextStyle(
                                        color='white',
                                        weight=FontWeight.BOLD
                                    )
                                )
                            ),

                            bgcolor=colors.INDIGO_ACCENT_700,
                            width=120,
                            height=60,
                            style=ButtonStyle(

                                color="white",
                                shape=ContinuousRectangleBorder(radius=30)

                            ),
                            on_click=lambda e: self.on_option_select('option1', e.control)
                        ),
                        Container(width=15),
                        ElevatedButton(
                            content=Container(
                                Text(
                                    question['option2'],
                                    rtl=True,
                                    text_align=TextAlign.CENTER,
                                    style=TextStyle(
                                        color='white',
                                        weight=FontWeight.BOLD
                                    )
                                )
                            ),
                            bgcolor=colors.INDIGO_ACCENT_700,
                            width=120,
                            height=60,
                            style=ButtonStyle(
                                color="white",
                                shape=ContinuousRectangleBorder(radius=40)
                            ),
                            on_click=lambda e: self.on_option_select('option2', e.control)
                        ),
                    ]
                ),
                Row(
                    alignment=MainAxisAlignment.SPACE_EVENLY,
                    vertical_alignment=MainAxisAlignment.CENTER,
                    controls=[
                        ElevatedButton(
                            # text=question['option3'],
                            content=Container(
                                Text(
                                    question['option3'],
                                    rtl=True,
                                    text_align=TextAlign.CENTER,
                                    style=TextStyle(
                                        color='white',
                                        weight=FontWeight.BOLD
                                    )
                                )
                            ),
                            bgcolor=colors.INDIGO_ACCENT_700,
                            width=120,
                            height=60,
                            style=ButtonStyle(
                                color="white",
                                shape=ContinuousRectangleBorder(radius=40)
                            ),
                            on_click=lambda e: self.on_option_select('option3', e.control)
                        ),
                        Container(width=15),
                        ElevatedButton(
                            content=Container(
                                Text(
                                    question['option4'],
                                    rtl=True,
                                    text_align=TextAlign.CENTER,
                                    style=TextStyle(
                                        color='white',
                                        weight=FontWeight.BOLD
                                    )
                                )
                            ),
                            bgcolor=colors.INDIGO_ACCENT_700,
                            width=120,
                            height=60,
                            style=ButtonStyle(
                                color="white",
                                shape=ContinuousRectangleBorder(radius=40)
                            ),
                            on_click=lambda e: self.on_option_select('option4', e.control)
                        ),
                    ]
                )
            ]
        )

        self.page.controls.append(
            Container(
                height=0
            ),
        )
        self.page.controls.append(
            Container(
                padding=Padding(top=25, bottom=25, right=0, left=0),
                border_radius=30,
                width=self.page.window_width * 0.85,
                bgcolor="White",
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=20,
                    color=ft.colors.BLUE_GREY_300,
                    offset=ft.Offset(0, 0),
                    blur_style=ft.ShadowBlurStyle.OUTER
                ),
                content=Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        Column(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                Row(
                                    alignment=MainAxisAlignment.START,
                                    vertical_alignment=MainAxisAlignment.START,
                                    controls=[
                                        Text(
                                            "سوال {} از {}".format(
                                                self.current_question_index + 1, len(self.questions)),
                                            style=ft.TextStyle(
                                                size=18,
                                                color="#666362",
                                                weight=ft.FontWeight.BOLD
                                            )
                                        )
                                    ]
                                ),
                                Container(
                                    height=20
                                ),
                                Row(
                                    controls=[
                                        Image(
                                            height=self.page.window_height * 0.4,
                                            width=self.page.window_width * 0.68,
                                            fit="Cover",
                                            src="http://127.0.0.1:8000{}".format(question['image']),
                                            border_radius=20
                                        ),
                                    ]
                                ),
                                Container(
                                    height=35
                                ),
                                Row(
                                    controls=[

                                        Text(
                                            question['question'],
                                            style=ft.TextStyle(
                                                size=20,
                                                color="Black",
                                                weight=ft.FontWeight.BOLD
                                            )
                                        )
                                    ]
                                ),
                                Container(
                                    height=20
                                ),
                                Row(
                                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                                    vertical_alignment=MainAxisAlignment.CENTER,
                                    controls=[
                                        self.answers
                                    ]
                                ),
                                Container(
                                    height=20
                                ),
                                Row(
                                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                                    vertical_alignment=MainAxisAlignment.CENTER,
                                    controls=[
                                        ElevatedButton(
                                            width=self.page.window_width * 0.5,
                                            height=50,
                                            icon=icons.ARROW_LEFT_ROUNDED,
                                            icon_color="white",
                                            text='سوال بعدی',
                                            on_click=self.submit_answer,
                                            style=ButtonStyle(
                                                bgcolor=colors.INDIGO_900,
                                                color="white",
                                                shape=ContinuousRectangleBorder(radius=40)
                                            )

                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                )
            )
        )

        self.page.update()

    def submit_answer(self, e):
        if self.selected_option:
            correct_answer = self.questions[self.current_question_index]['answer']
            if self.selected_option == correct_answer:
                self.score += 1

            self.answer_list.append({"qid": self.current_question_index, "answer": self.selected_option})
            self.selected_option = None
            self.next_question()

    def show_score(self):
        self.page.controls.clear()
        self.page.controls.append(
            Container(
                height=15,
                width=15
            ),
        )
        self.page.controls.append(
            Container(
                Column(
                    horizontal_alignment=MainAxisAlignment.CENTER,
                    alignment=MainAxisAlignment.CENTER,
                    width=self.page.window_width * 0.85,
                    height=self.page.window_height * 0.7,
                    controls=[
                        Row(
                            alignment=MainAxisAlignment.CENTER,
                            vertical_alignment=MainAxisAlignment.CENTER,
                            controls=[
                                Image(
                                    height=self.page.window_height * 0.4,
                                    width=self.page.window_width * 0.68,
                                    fit="Cover",
                                    src="assets/result.jpg",
                                    border_radius=20
                                ),
                            ]
                        ),
                        Row(
                          alignment=MainAxisAlignment.CENTER,
                          vertical_alignment=MainAxisAlignment.CENTER,
                          controls=[
                              Text(
                                  "هورااااه!",
                                  rtl=True,
                                  style=TextStyle(
                                      size=22,
                                      weight=FontWeight.BOLD,
                                      color="#023020"
                                  )
                              ),
                          ]
                        ),

                        Container(
                            Text(
                                "تو به {} سوال از مجموع {} سوال پاسخ درست دادی!!!".format(
                                    self.score,
                                    len(self.questions)
                                ),
                                rtl=True,
                                text_align=TextAlign.CENTER,
                                style=TextStyle(
                                    size=17,
                                    weight=FontWeight.BOLD,
                                    color="#023020"
                                )
                            ),
                        ),
                        Container(
                            width=40,
                            height=40
                        ),
                        Row(
                            alignment=MainAxisAlignment.CENTER,
                            vertical_alignment=MainAxisAlignment.CENTER,
                            controls=[
                                ElevatedButton(
                                    width=self.page.window_width * 0.5,
                                    height=50,
                                    icon=icons.RESTART_ALT,
                                    icon_color="white",
                                    text='شروع دوباره',
                                    on_click=lambda e: self.page.go('/'),
                                    style=ButtonStyle(
                                        bgcolor=colors.INDIGO_900,
                                        color="white",
                                        shape=ContinuousRectangleBorder(radius=40)
                                    )

                                )
                            ]
                        )


                    ]

                ),

                border_radius=30,
                width=self.page.window_width * 0.85,
                bgcolor="White",
                padding=Padding(top=25, bottom=25, right=25, left=25),
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=20,
                    color=ft.colors.BLUE_GREY_300,
                    offset=ft.Offset(0, 0),
                    blur_style=ft.ShadowBlurStyle.OUTER
                ),

            )
        )

        self.page.update()

    def update_score(self):
        data = self.page.session.get("user_data")
        print(self.answer_list)
        print(data['token'])
        url = "http://127.0.0.1:8000/api/game/submit"
        headers = {
            "Authorization": "{}".format(data['token']),
            "Content-Type": "application/json"
        }
        data = {
            "answers": self.answer_list,
            "username": data['username']
        }

        response = requests.post(url, headers=headers, json=data)
        print(response.json())

def quiz_view(page):
    quiz_app = QuizApp(page)
    quiz_app.show_question()

