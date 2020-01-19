from core.baseapp import BaseApp

class MainApp(BaseApp):
    def __init__(self):
        self.books = []


if __name__ == "__main__":
    app = MainApp()
    app.run()