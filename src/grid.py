import random



class Grid:
    """Representerar spelplanen. Du kan ändra standardstorleken och tecknen för olika rutor. """
    width = 36
    height = 12
    empty = "."  # Tecken för en tom ruta
    wall = "■"   # Tecken för en ogenomtränglig vägg
    trap = "T"   # Tecken för trap
    shovel = "S" # Tecken för shovel
    key = "K"    # Tecken för key
    chest = "C"  # Tecken för chest


    def __init__(self):
        """Skapa ett objekt av klassen Grid"""
        # Spelplanen lagras i en lista av listor. Vi använder "list comprehension" för att sätta tecknet för "empty" på varje plats på spelplanen.
        self.data = [[self.empty for y in range(self.width)] for z in range(
            self.height)]


    def get(self, x, y):
        """Hämta det som finns på en viss position"""
        return self.data[y][x]

    def set(self, x, y, value):
        """Ändra vad som finns på en viss position"""
        self.data[y][x] = value

    def set_player(self, player):
        self.player = player

    def clear(self, x, y):
        """Ta bort item från position"""
        self.set(x, y, self.empty)

    def __str__(self):
        """Gör så att vi kan skriva ut spelplanen med print(grid)"""
        xs = ""
        for y in range(len(self.data)):
            row = self.data[y]
            for x in range(len(row)):
                if x == self.player.pos_x and y == self.player.pos_y:
                    xs += "@"
                else:
                    xs += str(row[x])
            xs += "\n"
        return xs


    def make_walls(self):
        """Skapa väggar runt hela spelplanen"""
        for i in range(self.height):
            self.set(0, i, self.wall)
            self.set(self.width - 1, i, self.wall)

        for j in range(1, self.width - 1):
            self.set(j, 0, self.wall)
            self.set(j, self.height - 1, self.wall)

        # Horisontell vägg
        for x in range(5, 15):
            self.set(x, 3, self.wall)

        # Vertikal vägg
        for y in range(3, 8):
            self.set(15, y, self.wall)

        # Horisontell vägg
        for x in range(15, 27):
            self.set(x, 7, self.wall)

        # Vertikal vägg
        for y in range(5, 8):
            self.set(27, y, self.wall)

    # Används i filen pickups.py
    def get_random_x(self):
        """Slumpa en x-position på spelplanen"""
        return random.randint(0, self.width-1)

    def get_random_y(self):
        """Slumpa en y-position på spelplanen"""
        return random.randint(0, self.height-1)


    def is_empty(self, x, y):
        """Returnerar True om det inte finns något på aktuell ruta"""
        return self.get(x, y) == self.empty

    def place_trap(self):
        """Placera en fälla på en slumpmässig tom ruta"""
        while True:
            x = random.randint(1, self.width - 2)
            y = random.randint(1, self.height - 2)

            if self.is_empty(x, y):
                self.set(x, y, self.trap)
                self.trap_x = x
                self.trap_y = y
                break

    def place_shovel(self):
        """Place a shovel on a random empty tile"""
        while True:
            x = random.randint(1, self.width - 2)
            y = random.randint(1, self.height - 2)

            if self.is_empty(x, y):
                self.set(x, y, self.shovel)
                return

    def place_key(self):
        """Place a key on a random empty tile"""
        while True:
            x = random.randint(1, self.width - 2)
            y = random.randint(1, self.height - 2)

            if self.is_empty(x, y):
                self.set(x, y, self.key)
                return

    def place_chest(self):
        """Place a chest on a random empty tile"""
        while True:
            x = random.randint(1, self.width - 2)
            y = random.randint(1, self.height - 2)

            if self.is_empty(x, y):
                self.set(x, y, self.chest)
                return

    def place_keys_and_chests(self, amount):
        for _ in range(amount):
            self.place_key()
            self.place_chest()