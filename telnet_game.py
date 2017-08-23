from twisted.conch.telnet import TelnetTransport, TelnetProtocol
from twisted.internet import reactor
from twisted.internet.protocol import ServerFactory
from twisted.application.internet import TCPServer
from twisted.application.service import Application


class GameWorld(object):
    def __init__(self, io):
        self._io = io

    def scene1(self):
        self.io.send('>')
        self.io.get_input(self.scene1_response)

    def scene1_response(self, msg):
        self.io.send('We got: '+msg)


    async def async_scene1(self):
        self.io.send('>')
        msg = await self.io.get_input()
        self.io.send('We got: '+msg)


class IOQue(object): #shouldn't this be from collections?
    def __init__(self):
        self._input_cb = None
        self._messages = list() #deque?

    def send(self, astr):
        self._messages.append(astr)

    def get_input(self, cb):
        self._input_cb = cb

    def receive(self, astr):
        if self._input_cb:
            self._input_cb(astr)
            self._input_cb = None
        else:
            self.send('LULZ')

    def get_messages(self):
        msgs, self._messages = self._messages, []
        return msgs


class TelnetWorld(TelnetProtocol):
    def __init__(self, io_bus):
        self.io_bus = io_bus
        super(TelnetWorld, self).__init__()

    def dataReceived(self, data):
        for msg in self.io_bus.get_messages():
            self.transport.write(msg.encode('utf8'))
        self.io_bus.receive(data)


io_bus = IOQue()
world = GameWorld(io_bus)


factory = ServerFactory()
factory.protocol = lambda: TelnetTransport(TelnetWorld, io_bus=io_bus)
#service = TCPServer(6023, factory)

#application = Application("Telnet Echo Server")
#service.setServiceParent(application)

if __name__ == '__main__':
    reactor.listenTCP(6023, factory)
    reactor.run()
