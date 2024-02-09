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

class ConsoleCommand:
    def __init__(self, name: str, description: str, callback: Callable[[Any], None]):
        self.name = name
        self.description = description
        self.callback = callback

def clean_input(text: str) -> list[str]:
    return text.lower().split()

def get_commands() -> dict[str, ConsoleCommand]:
    return {
        "help": ConsoleCommand("help", "Displays a help message", command_help),
        "map": ConsoleCommand("map", "List some location areas", command_map),
        "mapb": ConsoleCommand("mapb", "List previous location areas", command_mapb),
        "explore": ConsoleCommand("explore {location_area}", "List encountered pokemon in a location area", command_explore),
        "catch": ConsoleCommand("catch {pokemon_name}", "Try to catch a pokemon and add to pokedex", command_catch),
        "inspect": ConsoleCommand("inspect {pokemon_name}", "Inspect a pokemon if it exists in the pokedex", command_inspect),
        "pokedex": ConsoleCommand("pokedex", "List all pokemon in the pokedex", command_pokedex),
        "exit": ConsoleCommand("exit", "Exit the Pokedex", command_exit),
    }

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