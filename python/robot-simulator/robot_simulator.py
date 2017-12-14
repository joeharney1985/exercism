# Globals for the bearings
# Change the values as you see fit
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

dir_vectors = {
    NORTH: (0, 1),
    EAST: (1, 0),
    SOUTH: (0, -1),
    WEST: (-1, 0),
}


class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.x = x
        self.y = y
        self.bearing = bearing
        self.dispatch = {
            'L': self.turn_left,
            'R': self.turn_right,
            'A': self.advance,
        }
        pass

    @property
    def coordinates(self):
        return self.x, self.y

    def turn_right(self):
        self.bearing = (self.bearing + 1) % 4

    def turn_left(self):
        self.bearing = (self.bearing - 1) % 4

    def advance(self):
        vector = dir_vectors[self.bearing]
        self.x += vector[0]
        self.y += vector[1]

    def simulate(self, commands):
        for command in commands:
            self.dispatch[command]()
