import asyncio
import json
import time
import websockets
import random
import string
import matplotlib.pyplot as plt

from typing import List

async def send_message(sender_ws: websockets.WebSocketClientProtocol, receiver_ws: websockets.WebSocketClientProtocol,
                       message: dict, msg_times: List[float]):
    msg_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    message['id'] = msg_id
    message['timestamp'] = str(time.time())
    await sender_ws.send(json.dumps(message))
    await receiver_ws.recv()
    msg_times.append(time.time())

async def test_performance():
    async with websockets.connect('ws://127.0.0.1:3002/api/socket/1') as sender_ws, \
            websockets.connect('ws://127.0.0.1:3002/api/socket/2') as receiver_ws:
        num_messages = 1000
        message = {
            'payload': 'Hello World!',
            'chatId': '123',
            'receiver': '2',
            'sender': '1',
            'timestamp': 'test'
        }
        msg_times = []
        for i in range(num_messages):
            await send_message(sender_ws, receiver_ws, message, msg_times)
        transfer_times = [msg_times[i+1] - msg_times[i] for i in range(num_messages-1)]
        print(f'Average message transfer time: {sum(transfer_times)/len(transfer_times):.6f} seconds')
        plt.plot(range(num_messages-1), transfer_times)
        plt.xlabel('Message Number')
        plt.ylabel('Transfer Time (s)')
        plt.show()

asyncio.run(test_performance())
