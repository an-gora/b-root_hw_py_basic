import asyncio
import socket
from asyncio import AbstractEventLoop

import aiohttp


async def echo(connection: socket, loop: AbstractEventLoop) -> None:
    while data := await loop.sock_recv(connection, 1024):
        await loop.sock_sendall(connection, data)


async def listen_for_connection(server_socket: socket,
                                loop: AbstractEventLoop):
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        clients.append(connection)
        print(f"Got a connection from {address}")
        asyncio.create_task(echo(connection, loop))


async def send_joke():
    url = "https://api.chucknorris.io/jokes/random"
    async with aiohttp.ClientSession() as session:
        while True:
            async with session.get(url) as result:
                res_json = await result.json()
                print(res_json)
                await asyncio.sleep(5)


clients = []


async def send_to_all(text):
    global clients
    loop = asyncio.get_event_loop()
    list_clients = []
    for client in clients:
        try:
            await loop.sock_sendall(client, text.encode())
            list_clients.append(client)
        except:
            print("hhh")

    clients = list_clients


async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()
    asyncio.create_task(send_joke())

    await listen_for_connection(server_socket, asyncio.get_event_loop())


asyncio.run(main())