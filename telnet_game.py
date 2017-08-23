from twisted.conch.telnet import TelnetTransport, TelnetProtocol
from twisted.internet import asyncioreactor, defer
from twisted.internet.protocol import ServerFactory
from twisted.application.internet import TCPServer
from twisted.application.service import Application
import asyncio


class GameWorld(object):
    def __init__(self, io):
        self.io = io

    async def start(self):
        await self.scene1()

    async def scene1(self):
        self.io.send('What is your name? ')
        self.player_name = await self.io.get_input()
        print("got player name:", self.player_name)
        self.io.send('Hello '+self.player_name+"\n")
        await self.scene2()

    async def scene2(self):
        self.io.send('This is the final scene, do you continue? ')
        msg = await self.io.get_input()
        if msg[0].lower() == 'y':
            self.io.send('Poor choice\n')
        else:
            self.io.send('Wise choice\n')


class IOBus(object):
    '''
    asyncio bus for twisted
    '''
    def __init__(self, transport):
        self._input_cb = None
        self.transport = transport

    def send(self, astr):
        self.transport.write(astr.encode('utf8'))

    def get_input(self):
        '''
        Returns an awaitable future
        '''
        future = asyncio.Future()
        self._input_cb = future.set_result
        return future

    def receive(self, data):
        if self._input_cb:
            self._input_cb(data.decode('utf8').strip())
            self._input_cb = None
        else:
            print('lost receive')

    def prime(self, fn):
        '''
        prime the io pump.
        starts a coroutine to push io and closes the transport when done.
        '''
        f = asyncio.ensure_future(fn())
        f.add_done_callback(lambda x: self.transport.loseConnection())
        return f


class TelnetWorld(TelnetProtocol):
    def __init__(self):
        self.world_busses = dict()
        super(TelnetWorld, self).__init__()

    def connectionMade(self):
        print('making game world')
        iobus = IOBus(self.transport)
        world = GameWorld(iobus)
        self.world_busses[self.transport] = iobus
        iobus.prime(world.start)

    def dataReceived(self, data):
        self.world_busses[self.transport].receive(data)

    def connectionLost(self, reason):
        del self.world_busses[self.transport]


factory = ServerFactory()
factory.protocol = lambda: TelnetTransport(TelnetWorld)


if __name__ == '__main__':
    #enables asyncio on twisted
    asyncioreactor.install(asyncio.get_event_loop())
    from twisted.internet import reactor
    reactor.listenTCP(6023, factory)
    reactor.run()
