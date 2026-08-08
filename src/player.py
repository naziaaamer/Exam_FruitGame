import grid


class Player:
    marker = "@"

    def __init__(self, x, y):
        self.player = None
        self.pos_x = x
        self.pos_y = y
        self.g = grid.Grid()
        self.inventory = []
        self.has_shovel = False
        self.keys = 0


    # Flyttar spelaren. "dx" och "dy" är skillnaden
    def move(self, dx, dy):
        """Flyttar spelaren.\n
        dx = horisontell förflyttning, från vänster till höger\n
        dy = vertikal förflyttning, uppifrån och ned"""
        self.pos_x += dx
        self.pos_y += dy


    def can_move(self, x, y, grid):
        new_x = self.pos_x + x
        new_y = self.pos_y + y

        # Check if outside the map
        if new_x < 0 or new_y < 0:
            return False

        # Check what is on the new tile
        tile = grid.get(new_x, new_y)

        # If it is a wall, don't move
        if tile == grid.wall:
            return False

        return True
        #TODO: returnera True om det inte står något i vägen

def handle_movement(command, state):
    directions = {
        "d": (1, 0),   # Right
        "a": (-1, 0),  # Left
        "w": (0, -1),  # Up
        "s": (0, 1)    # Down
    }

    if command not in directions:
        return False

    dx, dy = directions[command]

    # Try to move normally
    if state.player.can_move(dx, dy, state.g):
        state.player.move(dx, dy)

        # Check what the player stepped on
        tile = state.g.get(
            state.player.pos_x,
            state.player.pos_y
        )
        # Pick up key
        if tile == state.g.key:
            state.player.keys += 1
            state.g.clear(
                state.player.pos_x,
                state.player.pos_y
            )
        # Open the chest
        if tile == state.g.chest:
            if state.player.keys > 0:
                state.player.keys -= 1
                state.score += 100

                state.g.clear(
                    state.player.pos_x,
                    state.player.pos_y
                )
            else:
                state.score -= 1


        # Pick up shovel
        if tile == state.g.shovel:
            state.player.has_shovel = True
            state.g.clear(
                state.player.pos_x,
                state.player.pos_y
            )

        # Check for trap
        if tile == state.g.trap:
            state.score -= 10
        else:
            state.score -= 1  # Normal movement costs 1 point

        return True

    # Player tried to walk into a wall
    if state.player.has_shovel:
        wall_x = state.player.pos_x + dx
        wall_y = state.player.pos_y + dy

        if state.g.get(wall_x, wall_y) == state.g.wall:
            state.g.clear(wall_x, wall_y)
            state.player.has_shovel = False

    return False

def show_inventory(player):
    if not player.inventory:
        print("Inventory is empty.")
    else:
        print("Inventory:")
        for item in player.inventory:
            print(f"- {item.name}")