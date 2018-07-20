#  Battleship game (https://en.wikipedia.org/wiki/Battleship_(game)) implementation in Python
#  Object model/ Classes
class Ship(object):
    taken_coordinates = set()

    def __init__(self, x1, y1, x2, y2):
        if not (x1 == x2 or y1 == y2) or len(
                {(x1, y1), (x2, y2)} & Ship.taken_coordinates) > 0:  # Diagonal or overlapping placement
            raise Exception("Invalid(diagonal or overlapping) coordinates.")
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        Ship.taken_coordinates.add((x1, y1))
        Ship.taken_coordinates.add((x2, y2))
        self.shot = []  # Coordinates that were shot by opponent


class Player(object):
    def __init__(self, symbol, ships):
        self.symbol = symbol
        self.ships = ships
        self.hits, self.misses, self.destroyed = 0, 0, 0

    def shoot(self, opponent, x, y):
        for ship in opponent.ships:
            if ship.x1 <= x <= ship.x2 and ship.y1 <= y <= ship.y2:
                ship.shot.append((x, y))
                self.hits += 1
                return
        self.misses += 1


# Execution
# e.g. grid
# 00, 01, 02
# 10, 11, 12
# 20, 21, 22

p1 = Player('p1', [Ship(0, 0, 0, 1), Ship(2, 1, 2, 2)])
p2 = Player('p2', [Ship(1, 0, 2, 0), Ship(1, 1, 1, 2)])

p1.shoot(p2, 1, 0)
p2.shoot(p1, 2, 2)
p1.shoot(p2, 0, 2)
p2.shoot(p1, 2, 1)
p1.shoot(p2, 2, 0)
p2.shoot(p1, 0, 1)

print "Player 1 stats**"
print "Hits:{0}\nMisses:{1}".format(p1.hits, p1.misses)
for ship in p2.ships:
    if set((x, y) for x in range(ship.x1, ship.x2 + 1) for y in range(ship.y1, ship.y2 + 1)) == set(ship.shot):
        p1.destroyed += 1
print "Ships destroyed:", p1.destroyed
print
print "Player 2 stats**"
print "Hits:{0}\nMisses:{1}".format(p2.hits, p2.misses)
for ship in p1.ships:
    print set((x, y) for x in range(ship.x1, ship.x2 + 1) for y in range(ship.y1, ship.y2 + 1)), set(ship.shot)
    if set((x, y) for x in range(ship.x1, ship.x2 + 1) for y in range(ship.y1, ship.y2 + 1)) == set(ship.shot):
        p2.destroyed += 1
print "Ships destroyed:", p2.destroyed

# Output
#
# battleship_game svalleru$ python battleship_game.py
# Player 1 stats**
# Hits:2
# Misses:1
# Ships destroyed: 1
#
# Player 2 stats**
# Hits:3
# Misses:0
# set([(0, 1), (0, 0)]) set([(0, 1)])
# set([(2, 1), (2, 2)]) set([(2, 1), (2, 2)])
# Ships destroyed: 1
