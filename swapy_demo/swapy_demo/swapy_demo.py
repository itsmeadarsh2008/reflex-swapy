import reflex as rx
from reflex_swapy import *

# Current code doesn't work (WIP 🚧 demo!)

def index():
    return container(
        slot(id=1, children=[
            item(name="item1", children=[
                handle(children="|||"),
                "Item 1 Content"
            ])
        ]),
        slot(id=2),
        slot(id=3, children=[
            item(name="item3", children="Item 3 Content")
        ]),
        onSwap=lambda event: print("Swap event:", event)
    )

app = rx.App()
app.add_page(index)