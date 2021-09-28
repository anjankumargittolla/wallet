import asyncio

from copra.websocket import Channel, Client


loop = asyncio.get_event_loop()

ws = Client(loop, Channel('ticker', 'BTC-USD'))


def loop_data(request):
    try:
        return loop.run_forever()
    except KeyboardInterrupt:
        return loop.run_until_complete(ws.close())
loop_data()
