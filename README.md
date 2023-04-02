# WebSocket Message Sender

This is a Python script that sends messages over a WebSocket connection and records the send times of each message. The send times are then plotted as a bar chart using Matplotlib.

## Requirements

Python 3.x
websocket-client
Matplotlib

## Usage

1. Update the ws_url variable to the WebSocket endpoint URL for your application.
2. Set the num_messages and message_interval variables to the desired number of messages to send and the interval (in seconds) between each message.
3. Run the script using the following command: python websocket_sender.py

## Code Overview

The script connects to the WebSocket endpoint using the websocket.create_connection method and sends a JSON-formatted message. The send time of each message is recorded using the time.time() method and stored in a list.

Multiple threads are used to send messages concurrently, with each thread calling the send_message function. The threads list is created using a list comprehension, and the start method is called on each thread to start execution.

After all messages have been sent, the send times are calculated relative to the start time and plotted as a bar chart using Matplotlib.
