import eel

eel.init("web")

@eel.expose
def new_window(target: str):
    eel.show(f"html/{target}")


eel.start("html/new_window.html", port=9000)