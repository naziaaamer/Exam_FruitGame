from src.grid import Grid
from src.player import Player
from src.movement import handle_movement, show_inventory
from src import pickups



# TODO: flytta denna till en annaDn fil
class GameState:
    """Samla spelets variabler i en klass."""
    def __init__(self):

        self.score = 0
        self.inventory = []
        self.g = Grid()
        center_x = self.g.width // 2 #gives floating point
        center_y = self.g.height // 2
        self.player = Player(center_x, center_y)
        self.g.set_player(self.player)
        self.g.make_walls()
        self.g.place_trap()
        self.g.place_shovel()
        self.g.place_keys_and_chests(3)
        self.moves = 0
        pickups.randomize(self.g)

# TODO: flytta denna till en annan fil
def print_status(game_grid, state):
    """Visa spelvärlden och antal poäng."""
    print("--------------------------------------")
    print(f"You have {state.score} points.")
    print(game_grid)


def start(state):
    command = "a"
    # Loopa tills användaren trycker Q eller X.
    while not command.casefold() in ["q", "x"]:
        print_status(state.g, state)

        command = input("Use WASD to move, I for inventory, Q/X to quit. ")
        command = command.casefold()[:1]
        # print inventory
        if command == "i":
            show_inventory(state.player)
            continue


       ## if command == "d" and state.player.can_move(1, 0, state.g):  # move right
            # TODO: skapa funktioner, så vi inte behöver upprepa så mycket kod för riktningarna "W,A,S
        moved = handle_movement(command, state)
        # re-spawn fruits on map
        if moved:
            state.moves += 1

            if state.moves % 25 == 0:
                pickups.spawn_fruit(state.g)
        maybe_item = state.g.get(state.player.pos_x, state.player.pos_y)
        # state.player.move(1, 0)


        if isinstance(maybe_item, pickups.Item):
                state.player.inventory.append(maybe_item)
                # we found something
                state.score += maybe_item.value
                print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
                #g.set(player.pos_x, player.pos_y, g.empty)
                state.g.clear(state.player.pos_x, state.player.pos_y)


    # Hit kommer vi när while-loopen slutar
    print("Thank you for playing!")




# __name__ skapas av Python och sätts till "__main__" om man startar game.py
# direkt. Detta är för att undvika att start-funktionen körs om man importerar
# saker från game.py i en annan fil, till exempel vid testning.
if __name__ == "__main__":
    game_state = GameState()
    start(game_state)
