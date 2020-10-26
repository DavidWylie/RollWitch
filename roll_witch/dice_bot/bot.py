import os
from dotenv import load_dotenv
from .event_listener import EventListenerClient


def start_bot():
    load_dotenv()
    client_token = os.getenv("DISCORD_TOKEN")
    return EventListenerClient().start(client_token)
