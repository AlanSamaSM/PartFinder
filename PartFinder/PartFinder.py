"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

from .ui.base import base_page





class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    my_child=rx.vstack(
            rx.heading("Welcome to PartFinder", size="9"),
            rx.link(
                rx.button("Create new order"),
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    return base_page(my_child)


app = rx.App()
app.add_page(index)
