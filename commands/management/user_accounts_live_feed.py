import asyncio

from copra.websocket import Channel, Client

KEY = "3HzQwFfNUKiLOl6j"
SECRET = "NwJgOuVqKP7k5TPs0DXW10Sht1OLjG9d"
PASSPHRASE = "g7skqjihovm"

loop = asyncio.get_event_loop()

channel = Channel('user', 'LTC-USD')

ws = Client(loop, channel, auth=True, key=KEY, secret=SECRET, passphrase=PASSPHRASE)

try:
    loop.run_forever()
except KeyboardInterrupt:
    loop.run_until_complete(ws.close())
import asyncio

# from copra.rest import Client
#
#
# BTC_ACCOUNT_ID = "f4e76582-25e9-533d-adeb-62d2d0fd30e6"
#
# loop = asyncio.get_event_loop()
#
# async def get_btc_account():
#     async with Client(loop, auth=True, key=KEY,
#                       secret=SECRET, passphrase=PASSPHRASE) as client:
#
#         btc_account = await client.account(BTC_ACCOUNT_ID)
#         print(btc_account)
#
# loop.run_until_complete(get_btc_account())


# import asyncio
#
# from copra.websocket import Channel, Client
#
# loop = asyncio.get_event_loop()
#
# ws = Client(loop, Channel('heartbeat', 'BTC-USD'))
#
# try:
#     loop.run_forever()
# except KeyboardInterrupt:
#     loop.run_until_complete(ws.close())
#     loop.close()