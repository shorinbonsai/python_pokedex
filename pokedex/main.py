import sys
from datetime import timedelta
from api_client import Client
from pokecache import Cache
from utils import *
from typing import Callable
from typing import Any

class Config:
    def __init__(self):
        self.pokeapi_client = Client(timedelta(hours=0.5))
        self.caught_pokemon = {}


def clean_input(text: str) -> list[str]:
    return text.lower().split()


def start(cfg, stdin, stdout):
    while True:
        line = input("Pokedex > ")
        text = clean_input(line)
        if not text:
            continue
        command_name = text[0]
        args = text[1:]
        command = get_commands().get(command_name)
        if command:
            try:
                command.callback(cfg, *args)
            except Exception as e:
                print(e)
        else:
            print("Unknown command")


if __name__ == "__main__":
    cfg = Config()
    start(cfg, sys.stdin, sys.stdout)