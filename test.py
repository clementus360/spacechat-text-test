import websocket
import time
import threading
import json
import matplotlib.pyplot as plt

# Define the URL for the WebSocket endpoint
ws_url = "ws://127.0.0.1:3002/api/socket/{userid}"

# Define the number of messages to send and the message interval (in seconds)
num_messages = 5000
message_interval = 0.1

# Define a list to store the message send times
send_times = []

# Define a function to send a single message and record the send time
def send_message():
    # Connect to the WebSocket endpoint
    ws = websocket.create_connection(ws_url)

    # Create a message in JSON format
    message = {
        "id": "001",
        "payload": "Hello World!",
        "chatId": "123",
        "receiver": "002",
        "sender": "003",
        "timestamp": "123"
    }
    message_json = json.dumps(message)

    # Record the send time
    send_time = time.time()
    send_times.append(send_time)

    # Send the message
    ws.send(message_json)

    # Close the WebSocket connection
    ws.close()

# Create a list of threads to send messages concurrently
threads = [threading.Thread(target=send_message) for i in range(num_messages)]

# Start the threads
for thread in threads:
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Calculate the message send times relative to the start time
start_time = min(send_times)
send_times = [t - start_time for t in send_times]

# Plot the message send times as a bar chart
plt.bar(range(num_messages), send_times, width=1.0)
plt.xlabel("Message Index")
plt.ylabel("Send Time (seconds)")
plt.title("Message Send Times")
plt.show()
