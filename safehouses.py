# safehouses.py

def manhattan_distance(x,y,hx,hy):
    return abs(x - hx) + abs(y - hy)

def find_nearest_house(grid, x, y, houses):

    min_distance = -1

    for house in houses:
        distance = manhattan_distance(x,y,house[0],house[1])
        if min_distance == -1:
            min_distance = distance
            continue
        if distance < min_distance:
            min_distance = distance
            continue


    return min_distance


def main():
    count = int(input())
    grid = []
    for i in range(count):
        grid.append(list(input()))
    
    houses = []
    spies = []

    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 'H':
                houses.append((x,y))
            if grid[x][y] == 'S':
                spies.append((x,y))

    max_ = 0

    for spy in spies:
        distance = find_nearest_house(grid, spy[0], spy[1], houses)
        if distance > max_:
            max_ = distance
    
    print(max_)


if __name__ == "__main__":
    main()
