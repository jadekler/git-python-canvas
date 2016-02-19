def initGrid(maxX, maxY):
    grid = []
    for x in range(0, maxX):
        grid.append([])
        for y in range(0, maxY):
            grid[x].append(0)

    return grid

def drawGrid(grid):
    for x in range(0, len(grid)):
        for y in range(0, len(grid[x])):
            if grid[x][y] == 1:
                print '  X'
            else:
                print '  ',
        print '\n'

def drawLine(grid, startX, startY, endX, endY):
    # y = mx + b
    m = (endY - startY) / (endX - startX) # slope
    b = startY - m * startX # y-intercept

    if startX > endX:
        for x in range(endX, startX):
            y = m * x + b
            grid[x][y] = 1
    else:
        for x in range(startX, endX):
            y = m * x + b
            grid[x][y] = 1


    # grid[startX][startY] = 1
    # grid[endX][endY] = 1

grid = initGrid(10, 10)
drawLine(grid, 9, 9, 5, 6)
drawGrid(grid)
print 'Done'
