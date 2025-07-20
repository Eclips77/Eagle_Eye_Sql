from ui.console_ui import ConsoleUI
# from ui.tk_ui import TkUI


def run(use_tk: bool = False) -> None:
    """Launch the desired user interface."""
    ui = ConsoleUI()  # default
    if use_tk:
        from ui.tk_ui import TkUI  # imported lazily to avoid tkinter dependency when unused
        ui = TkUI()
    ui.run()


if __name__ == "__main__":
    run()
