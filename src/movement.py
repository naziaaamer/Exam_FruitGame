def handle_movement(command, state):
    directions = {
        "d": (1, 0),  # Right
        "a": (-1, 0),  # Left
        "w": (0, -1),  # Up
        "s": (0, 1)  # Down
    }

    if command not in directions:
        return False

    dx, dy = directions[command]

    # Try to move normally
    if state.player.can_move(dx, dy, state.g):
        state.player.move(dx, dy)
    else:
        #Use shovel to break wall.
        if state.player.has_shovel:

            wall_x = state.player.pos_x + dx
            wall_y = state.player.pos_y + dy

            if state.g.get(wall_x, wall_y) == state.g.wall:
                # Remove wall
                state.g.clear(wall_x, wall_y)

                # Use up shovel
                state.player.has_shovel = False

                print("You used the shovel to break the wall!")

                return True


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
        print("You picked a key. Use to open the chest!")

    # Open the chest
    if tile == state.g.chest:
        if state.player.keys > 0:
            state.player.keys -= 1
            state.score += 100

            state.g.clear(
                state.player.pos_x,
                state.player.pos_y
            )
            print("You opened the chest! +100 points!")
        else:
            state.score -= 1
            print("You need key to open the chest!")

    # Pick up shovel
    if tile == state.g.shovel:
        state.player.has_shovel = True
        state.g.clear(
            state.player.pos_x,
            state.player.pos_y
        )
        print("You picked a shovel. Use to break the wall!")


    # Check for trap
    if tile == state.g.trap:
        state.score -= 10
        print("You stepped on the trap. -10 points!")
    else:
        state.score -= 1  # Normal movement costs 1 point
    return True


def show_inventory(player):
    if not player.inventory:
        print("Inventory is empty.")
    else:
        print("Inventory:")
        for item in player.inventory:
            print(f"- {item.name}")