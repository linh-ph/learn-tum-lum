import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from chatgpt import ChatGPT

# Set up the Slack client and chatGPT model
client = WebClient(token="BwPPIITkuzOwmuPmCTwlbp07")
model = ChatGPT()

# Set up an event listener for messages in Slack channels
@slack_events_adapter.on("message")
def handle_message(event):
    # Get the message text and sender
    message = event["text"]
    sender = event["user"]

    # Use chatGPT to generate a response
    response = model.generate(prompt=message, max_tokens=256)

    # Send the response back to the channel
    try:
        client.chat_postMessage(channel=event["channel"], text=response)
    except SlackApiError as e:
        print("Error sending message: {}".format(e))