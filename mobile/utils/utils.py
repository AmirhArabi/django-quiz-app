import json

from flet import *
import requests


def MainNavBar(page):
    def change_route(e, page):
        print(page.route)
        print(e.control)

    item = NavigationBar(
        bgcolor="transparent",
        height=60,
        width=300,
        expand=False,
        expand_loose=False,
        selected_index=0,
        elevation=0,
        label_behavior=NavigationBarLabelBehavior.ONLY_SHOW_SELECTED,
        # indicator_color='#d3d8db',

        on_change=lambda e: change_route(page=page, e=e),
        destinations=[
            NavigationDestination(icon=icons.HOME_OUTLINED, selected_icon=icons.HOME_ROUNDED, label="Home", ),
            NavigationDestination(icon=icons.PERSON_2_OUTLINED, selected_icon=icons.PERSON_ROUNDED, label="Profile"),
            NavigationDestination(icon=icons.BAR_CHART, label="LeaderBoard"),
            NavigationDestination(icon=icons.SETTINGS_OUTLINED, selected_icon=icons.SETTINGS_ROUNDED, label="Setting")
        ],

    )
    return item


def get_qustions(page, category):
    if category is None:
        category = "Earth"
    base_url = "http://127.0.0.1:8000/api/categories/{}/questions".format(category)
    user = page.session.get("user_data")
    print("user data", user)
    token = page.session.get("user_data")['token']
    print(token)
    headers = {
        "Authorization": token
    }
    req = requests.get(base_url, headers=headers)
    if req.status_code == 200:
        data = json.loads(req.text)
        return data
    else:
        print(req.status_code)

