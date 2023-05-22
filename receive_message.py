import asyncio
import websockets

async def receive_message():
    async with websockets.connect('ws://0.0.0.0:8765') as websocket:
        while True:
            mensaje = await websocket.recv()
            print("Mensaje recibido:", mensaje)


asyncio.get_event_loop().run_until_complete(asyncio.gather(receive_message()))
