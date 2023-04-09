import websocket
import json

ws_url = "ws://127.0.0.1:3002/api/socket/{userid}"
userid = "078161616"

# Define the JSON message to send
message = {
    "id": "001",
    "payload": "Hello",
    "chatId": "123",
    "receiver": "0787316052",
    "sender": "078161616",
    "timestamp": "123"
}
json_message = json.dumps(message)

# Define a callback function to handle received messages
def on_message(ws, message):
    print("Received message:", message)

# Connect to the WebSocket URL and send the JSON message
ws = websocket.WebSocketApp(ws_url.format(userid=userid), on_message=on_message)
ws.on_open = lambda ws: ws.send(json_message)
ws.run_forever()

try:
    # Add a loop to keep the program running
    while True:
        pass
except KeyboardInterrupt:
    # Close the WebSocket connection and exit the program
    ws.close()
