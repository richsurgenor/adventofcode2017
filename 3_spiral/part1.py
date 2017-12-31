
def foo (x, total, ring):
    total = total + ( 8 * ring  ) 
    if total >= x:
        return ring, (total - (8 * ring) + 1)
    ring = ring + 1
    return foo (x, total, ring)

def calculate_coordinates(input, n, current):
    x = n 
    y = -n + 1

    if input is current:
        return x, y

    # first stage
    while y < n: 
        y += 1
        current += 1
        if input == current:
            return x,y

    # second stage
    while x > -n: 
        x -= 1
        current += 1
        if input == current:
            return x,y

    # third stage
    while y > -n: 
        y -= 1
        current += 1
        if input == current:
            return x,y

    # fourth stage
    while x < n:
        x += 1
        current += 1
        if input == current:
            return x,y

input = 289326
bar = foo(input, 1, 0)
n = bar[0] # ring number
current = bar[1] # first number of new sequence

coords = calculate_coordinates(input, n, current)

print ("x: " + str(coords[0]) + " y: " + str(coords[1]))

steps = abs(coords[0]) + abs(coords[1])
print ("steps required: " + str(steps))
#while x < 100:
#    foo (x, 0, 0)
