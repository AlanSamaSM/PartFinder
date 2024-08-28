import reflex as rx
from ui.base import base_page

def workorder_page() -> rx.Component:
    my_child=rx.vstack(
            rx.heading("Work Order", size="9"),
            rx.text("Here you can select the items you need"),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    return base_page(my_child)
