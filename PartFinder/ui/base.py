import reflex as rx
from .sidebar import sidebar_bottom_profile

def base_page(child:rx.Component) -> rx.Component:
    return rx.container(
        sidebar_bottom_profile(),
        rx.box(child,
               #pading=1em
               # text_aling=center
               # you can add more characteristics in this part
            ),
        rx.color_mode.button(position="top-right"), #Here is the location of the dark/light mode button   
        rx.logo(),
    )