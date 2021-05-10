# Globals for the directions
# Change the values as you see fit
EAST = "EAST"
NORTH = "NORTH"
WEST = "WEST"
SOUTH = "SOUTH"

movement_dict = {"R": 0, "L": 0, "A": 1}
compass_dict = {
    "EAST": {"R": "SOUTH", "L": "NORTH", "A": lambda x, y: (x+1, y)},
    "NORTH": {"R": "EAST", "L": "WEST", "A": lambda x, y: (x, y+1)},
    "WEST": {"R": "NORTH", "L": "SOUTH", "A": lambda x, y: (x-1, y)},
    "SOUTH": {"R": "WEST", "L": "EAST", "A": lambda x, y: (x, y-1)}
}


class Robot:
    def __init__(self, direction=NORTH, x=0, y=0):
        self.x = x
        self.y = y
        self.coordinates = (self.x, self.y)
        self.direction = direction

    def move(self, movements: str):
        try:
            for movement in movements:
                if movement == "A":
                    self.x, self.y = compass_dict[self.direction]["A"](self.x, self.y)
                # For movement of 'R' or 'L'
                else:
                    self.direction = compass_dict[self.direction][movement]
            self.coordinates = (self.x, self.y)

        except KeyError:
            raise KeyError("Invalid move detected! Valid moves are 'R', 'L', and 'A' only.")
