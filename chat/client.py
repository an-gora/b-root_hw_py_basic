import asyncio


async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8000)

    await asyncio.gather(reader_f(reader), writer_f(writer))

    print('Close the connection')
    writer.close()


async def reader_f(reader):
    while True:
        data = await reader.read(100)
        print(f'Received: {data.decode()!r}')


async def writer_f(writer):
    while True:
        message = "kuku"
        writer.write(message.encode())
        await asyncio.sleep(5)


asyncio.run(tcp_echo_client('Hello World!'))