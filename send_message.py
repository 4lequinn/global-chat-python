import asyncio
import websockets

async def send_message():
    async with websockets.connect('ws://0.0.0.0:8765') as websocket:
        while True:
            message = input("Escribe un mensaje: ")
            await websocket.send(message)


asyncio.get_event_loop().run_until_complete(asyncio.gather(send_message()))
