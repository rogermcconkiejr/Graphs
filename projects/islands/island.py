# Write a function that takes a 2D binary array and returns the number of 1 islands. 
# An island consists of 1s that are connected to the north, south, east or west. For example:
# islands = [[0, 1, 0, 1, 0],
#            [1, 1, 0, 1, 1],
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0]]
# island_counter(islands) # returns 4

def island_counter(matrix):
    '''
    Create a visited matrix of the same dimensions as the given matrix.
    Walk through each cell of the matrix.
    Count up the connected components and return that number.
    '''
    visited = []
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            #when I reach a 1....
            if not visited[y][x]:
                # Do a DFT and mark each 1 as visited
                if matrix[y][x] == 1:
                # Increment the counter by 1
                    visisted = dft(x, y, matrix, visited)
                    island_count += 1
                else:
                    visited[y][x] = True


def dft(x, y, matrix, visited):
    s = Stack()
    s.push( (x, y) )
    while s.size() > 0:
        v = s.pop
        x= v[0]
        ### Stopping here, copy and paste from here. ###
        ### pay attention to that get neighbors function ###



islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]