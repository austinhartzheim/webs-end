'''
WebsEnd Server: Software to manage multiple connections.
'''
import asyncio
import websockets

sockets = {}


class WebSocketManager():
    def __init__(self, ws, path):
        self.ws = ws
        self.path = path

    def handler(self):
        while True:
            try:
                message = yield from self.ws.recv()
                yield from self.ws.send(message)
            except websockets.exceptions.ConnectionClosed:
                # TODO: handle socket closed
                pass


def handler(ws, path):
    manager = WebSocketManager(ws, path)
    yield from manager.handler()


server = websockets.serve(handler, 'localhost', 33758)
asyncio.get_event_loop().run_until_complete(server)
asyncio.get_event_loop().run_forever()
