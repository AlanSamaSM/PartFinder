import reflex as rx
from .sidebar import sidebar_bottom_profile

def base_page(child:rx.Component) -> rx.Component:
    return rx.container (
        sidebar_bottom_profile(),
        child,
        rx.color_mode.button(position="top-right"), #Here is the location of the dark/light mode button   
        rx.logo(),
    )