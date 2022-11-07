from .api.server import Server


def init_server():
    server = Server()
    server.run()


def init_app():
    init_server()
