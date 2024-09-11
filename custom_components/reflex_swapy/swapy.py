import reflex as rx

# I don't know how to fix is_default thing, so I'm going to leave it as it is
# if someone knows how to fix, make a PR
# uses react-swapy library by @vishnusankaran (a react wrapper of swapy)
class SwapyContainer(rx.Component):
    library = "react-swapy"
    tag = "Container"
    is_default = True  

    # Props
    enable: rx.Var[bool] = True
    config: rx.Var[dict] = {"animation": "dynamic"}
    onSwap: rx.EventHandler[lambda event: [event]]

container = SwapyContainer.create

class SwapySlot(rx.Component):
    library = "react-swapy"
    tag = "Slot"
    is_default = True  

    # Props
    id: rx.Var[int]
    name: rx.Var[str]

slot = SwapySlot.create

class SwapyItem(rx.Component):
    library = "react-swapy"
    tag = "Item"
    is_default = True  

    # Props
    name: rx.Var[str]

item = SwapyItem.create

class SwapyHandle(rx.Component):
    library = "react-swapy"
    tag = "Handle"
    is_default = True

handle = SwapyHandle.create