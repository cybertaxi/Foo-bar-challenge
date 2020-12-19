# Prepare the Bunnies' Escape
# ===========================

# You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's bunny prisoners, but once they're free of the prison blocks, the bunnies are going to need to escape Lambda's space station via the escape pods as quickly as possible. Unfortunately, the halls of the space station are a maze of corridors and dead ends that will be a deathtrap for the escaping bunnies. Fortunately, Commander Lambda has put you in charge of a remodeling project that will give you the opportunity to make things a little easier for the bunnies. Unfortunately (again), you can't just remove all obstacles between the bunnies and the escape pods - at most you can remove one wall per escape pod path, both to maintain structural integrity of the station and to avoid arousing Commander Lambda's suspicions. 

# You have maps of parts of the space station, each starting at a prison exit and ending at the door to an escape pod. The map is represented as a matrix of 0s and 1s, where 0s are passable space and 1s are impassable walls. The door out of the prison is at the top left (0,0) and the door into an escape pod is at the bottom right (w-1,h-1). 

# Write a function solution(map) that generates the length of the shortest path from the prison door to the escape pod, where you are allowed to remove one wall as part of your remodeling plans. The path length is the total number of nodes you pass through, counting both the entrance and exit nodes. The starting and ending positions are always passable (0). The map will always be solvable, though you may or may not need to remove a wall. The height and width of the map can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.

# Languages
# =========

# To provide a Python solution, edit solution.py
# To provide a Java solution, edit Solution.java

# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.

# -- Python cases --
# Input:
# solution.solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
# Output:
#     7

# Input:
# solution.solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
# Output:
#     11

# -- Java cases --
# Input:
# Solution.solution({{0, 1, 1, 0}, {0, 0, 0, 1}, {1, 1, 0, 0}, {1, 1, 1, 0}})
# Output:
#     7

# Input:
# Solution.solution({{0, 0, 0, 0, 0, 0}, {1, 1, 1, 1, 1, 0}, {0, 0, 0, 0, 0, 0}, {0, 1, 1, 1, 1, 1}, {0, 1, 1, 1, 1, 1}, {0, 0, 0, 0, 0, 0}})
# Output:
#     11

# Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.

# Java
# ====
# Your code will be compiled using standard Java 8. All tests will be run by calling the solution() method inside the Solution class

# Execution time is limited.

# Wildcard imports and some specific classes are restricted (e.g. java.lang.ClassLoader). You will receive an error when you verify your solution if you have used a blacklisted class.

# Third-party libraries, input/output operations, spawning threads or processes and changes to the execution environment are not allowed.

# Your solution must be under 32000 characters in length including new lines and and other non-printing characters.

# Python
# ======
# Your code will run inside a Python 2.7.13 sandbox. All tests will be run by calling the solution() function.

# Standard libraries are supported except for bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib.

# Input/output operations are not allowed.

# Your solution must be under 32000 characters in length including new lines and and other non-printing characters.

from collections import deque

#bfs here!
def solution(map):
    width = len(map)
    height = len(map[0])
    visited = set()
    search = deque()

    def find_neighbours(r, c, wall): #row, col, wall 
        for row, col in (r-1,c),(r+1,c),(r, c+1),(r, c-1): #move wihtin cardinal directions
            if 0 <= row < width and 0 <= col < height: #not out of grid 
                if map[r][c] == 0:
                    if (row, col, steps, wall) not in visited:
                        yield row, col, steps, wall
                else:
                    if wall > 0 and (row, col, steps, wall-1) not in visited: #encounter a wall, check if we stil have chance to break a wall and not visit yet.
                        yield row, col, steps, wall-1
                
    #init the first start point
    search = deque([(0,0,1,1)]) #row,col,steps, wall
    visited.add((0,0,1,1)) #row,col,steps,wall
    
    while search:        
        row, col, steps, wall = search.popleft() 
        if row == width-1 and col == height-1: #found
            return steps
        for (row, col, steps, wall) in find_neighbours(row,col,wall):
            search.append((row,col,steps+1,wall))
            visited.add((row,col,steps,wall))

maze1 = [   [0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0]] #Answer 21

maze2 = [   [0, 1, 1, 0], 
            [0, 0, 0, 1], 
            [1, 1, 0, 0], 
            [1, 1, 1, 0]] #Answer 7

maze3 = [   [0,1,0,0,0],
            [0,0,0,1,0],
            [1,1,1,1,0]] #Answer 7

maze4 = [[0,1,1,1],[0,1,0,0],[1,0,1,0],[1,1,0,0]] #Answer 7
maze5 = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]] #Answer 11
maze6 = [[0,1,1,1],
         [0,1,0,0],
         [1,0,1,0],
         [1,1,0,0]] #7

print(solution(maze1)) #21
print(solution(maze2)) #7
print(solution(maze3)) #7 
print(solution(maze4)) #7
print(solution(maze6)) #7

