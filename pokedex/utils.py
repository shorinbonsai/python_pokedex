import sys
from typing import Callable
from typing import Any
# from main import get_commands


class ConsoleCommand:
    def __init__(self, name: str, description: str, callback: Callable[[Any], None]):
        self.name = name
        self.description = description
        self.callback = callback

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

# Placeholder functions for command callbacks
def command_help(cfg, *args):
    print()
    print("Welcome to the Pokedex.")
    print("Here are the available commands:")
    for name, command in get_commands().items():
        print(f"{name}: {command.description}")
    print()
    return None

def command_map(cfg, *args):
    pass

def command_mapb(cfg, *args):
    pass

def command_explore(cfg, *args):
    pass

def command_catch(cfg, *args):
    pass

def command_inspect(cfg, *args):
    pass

def command_pokedex(cfg, *args):
    pass

def command_exit(cfg, *args):
    sys.exit(0)