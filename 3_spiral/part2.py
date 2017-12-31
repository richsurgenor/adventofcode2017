## Should contain dict of { "x y" : val }

def check(x, y):
    return str(x) + " " + str(y) in container

def find_adjacent_tiles(x, y):
    """
    Returns an interable of adjacent tiles with the corresponding values
    """
    
    adjacents = []
    checks = [ [x+1,y], [x-1, y], [x,y+1], [x,y-1], [x+1,y+1], [x-1,y+1], [x+1,y-1], [x-1, y-1] ]

    for cond in checks:
        if check(cond[0], cond[1]):
            adjacents.append(cond)

    return adjacents
        
def add_adjacent_tiles(x, y):
    total = 0
    for tile in find_adjacent_tiles(x,y):
       total += container[str(tile[0]) + " " + str(tile[1])]
    return total

def calculate_coordinates(n):
    input = 289326

    x = n 
    y = -n + 1

    amt = add_adjacent_tiles(x, y)
    container[str(x) + " " + str(y)] = amt
    if amt > input:
        return amt

    # first stage
    while y < n: 
        y += 1
        amt = add_adjacent_tiles(x,y)
        container[str(x) + " " + str(y)] = amt
        if amt > input:
            return amt

    # second stage
    while x > -n: 
        x -= 1
        amt = add_adjacent_tiles(x, y)
        container[str(x) + " " + str(y)] = amt
        if amt > input:
            return amt

    # third stage
    while y > -n: 
        y -= 1
        amt = add_adjacent_tiles(x, y)
        container[str(x) + " " + str(y)] = amt
        if amt > input:
            return amt

    # fourth stage
    while x < n:
        x += 1
        amt = add_adjacent_tiles(x, y)
        container[str(x) + " " + str(y)] = amt
        if amt > input:
            return amt
    

if __name__ == "__main__":
    ongoing = True
    container = {"0 0": 1}

    current = 1
    while ongoing:
        state = calculate_coordinates(current)
        if state:
            ongoing = False
            print ("Result : " + str(state))

        current += 1

# map of coordinates to find adjacent tiles each iteration
# calculate coordinates by inputting each ring..
