# Written with PyCharm
# @Author:          Shabbir, Csilla, Alexander
# @Date:            2021-05-06 12:07:44
# @Last Modified:   2021-05-09 19:50:23

# Python 3 program to solve
# the eight puzzle issue

# -------------------------------------------------------------------------------------------------------------- #
# Accepts start and goal states and checks mainly if goal is reached
class EightPuzzle:

    # Initialize the puzzle size by the specified size,open and closed lists to empty
    def __init__(self, size):

        self.number = size
        self.open = []
        self.closed = []
        self.admissible = True

    # Takes the start and goal state and checks if the validity is given
    def run(self):
        level = 0
        limits = 10000
        example_start = [["3", "2", "1"], ["4", "6", "5"], ["0", "7", "8"]]
        example_goal = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "0"]]

        print("*---------------------------------------------------------------*")
        print("Welcome user to Eight Puzzle")
        print("")
        print("Manual:")
        print("1: Enter the current state")
        for i in example_start:
            for j in i:
                print(j, end=" ")
            print()
        print("2: Enter the goal state")
        for i in example_goal:
            for j in i:
                print(j, end=" ")
            print()
        print("*---------------------------------------------------------------*")

        print("Enter the start state matrix \n")
        start = self.puzzle_maker()
        self.is_solvable(start)
        print("Enter the goal state matrix \n")
        goal = self.puzzle_maker()

        start = NodeComputation(start, 0, 0)
        start.f_number = self.f_x(start, goal)

        self.open.append(start)
        print("\n\n")
        if self.admissible:
            print("\n\n")
            while True:
                new_puzzle = self.open[0]
                print("")
                print("  | ")
                print(" \\\'/ \n")
                for i in new_puzzle.data:
                    for j in i:
                        print(j, end=" ")
                    print("")
                level += 1
                if self.h_x(new_puzzle.data, goal) == 0:
                    print(f"Steps: {level}")
                    break
                for i in new_puzzle.generate_child():
                    i.f_number = self.f_x(i, goal)
                    self.open.append(i)
                self.closed.append(new_puzzle)
                del self.open[0]

                # To hinder a long computation time, it will break the while after limits is 0.
                self.open.sort(key=lambda x: x.f_number, reverse=False)
                limits -= 1
                if limits == 0:
                    print("Maximum threshold of tries reached. Goal state can not be reached")
                    break
        else:
            print("Your Goal state is unreachable")

    # Accepts the puzzle from the user and convert it to a string list
    def puzzle_maker(self):
        puz = []
        for i in range(0, self.number):
            temporary = input().split(" ")
            puz.append(temporary)
        return puz

    # Heuristic Function to calculate heuristic value f(x) = h(x) + g(x)
    def f_x(self, start, goal):
        return self.h_x(start.data, goal) + start.level

    # Calculates the different between the given puzzles
    def h_x(self, start, goal):

        temp = 0
        for i in range(0, self.number):
            for j in range(0, self.number):
                if start[i][j] != goal[i][j] and start[i][j] != '0':
                    temp += 1
        return temp

    # Static method for computing the inversion.
    @staticmethod
    def get_inv_count(arr):
        # ----------------------------------------------------------------- #
        # Experimental (unnecessary)
        # for i in range(0, len(arr)-1):
        #    print(len(arr))
        #    for j in range(len(arr[i])-1):
        #        print(len(arr[i]))
        #        results = list(map(int, arr[i][j]))
        #        print(type(arr[i][j]))
        # ----------------------------------------------------------------- #

        inv_count = 0
        for i in range(0, 2):
            for j in range(i + 1, 3):

                # Value 0 is used for empty space
                if int(arr[j][i]) > 0 and int(arr[j][i]) > int(arr[i][j]):
                    inv_count += 1
        return inv_count

    # Checks if given start state is solvable and returns True or False
    def is_solvable(self, puz):

        # Count inversions in given 8 puzzle
        inv_count = self.get_inv_count(puz)

        # return true if inversion count is even.
        if inv_count % 2 != 0:
            self.admissible = False


# -------------------------------------------------------------------------------------------------------------- #

# -------------------------------------------------------------------------------------------------------------- #

#
class NodeComputation:

    #
    def __init__(self, data, level, f_number):

        self.data = data
        self.level = level
        self.f_number = f_number

    # Generate the child node and checks it
    def generate_child(self):
        x, y = self.find(self.data, '0')

        val_list = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
        children = []
        for i in val_list:
            child = self.shift(self.data, x, y, i[0], i[1])
            if child is not None:
                child_node = NodeComputation(child, self.level + 1, 0)
                children.append(child_node)
        return children

    # shift the numbers, if node has a good heuristic
    def shift(self, puz, x1, y1, x2, y2):
        if 0 <= x2 < len(self.data) and 0 <= y2 < len(self.data):
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None

    # Copy function to create a similar matrix of the given node
    @staticmethod
    def copy(root):
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp

    # find function to search the blank=0
    def find(self, puz, x):
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data)):
                if puz[i][j] == x:
                    return i, j


# -------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------- #

# Initialization
puzzle = EightPuzzle(3)
puzzle.run()

