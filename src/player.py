class Player:
    marker = "@"

    def __init__(self, x, y):
        self.player = None
        self.pos_x = x
        self.pos_y = y
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

