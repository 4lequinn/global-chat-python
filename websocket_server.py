import asyncio
import websockets

# Lista para almacenar los clientes conectados
clients = set()

async def global_chat(websocket, path):
    # Agregar cliente a la lista de clientes conectados
    clients.add(websocket)
    try:
        # Mantener la conexión abierta para recibir mensajes
        async for message in websocket:
            # Enviar el mensaje recibido a todos los clientes conectados
            for client in clients:
                await client.send(message)
    finally:
        # Eliminar cliente de la lista al desconectarse
        client.remove(websocket)

# Iniciar el servidor WebSocket
start_server = websockets.serve(global_chat, '0.0.0.0', 8765)

# Ejecutar el servidor de forma asíncrona
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
