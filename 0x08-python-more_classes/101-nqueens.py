#!/usr/bin/python3
""" Solving the N-queens problem using backtracking """
import sys


class Nqueens:
    """ Class built for the nqueen problem """

    def __init__(self, n):
        """ Instance creation for the Nqueen problem """

        self.N = n
        self.row = 0
        self.column = [0] * n
        self.result = []

    def solve(self):
        """ Solution code i guess """
        if self.row == self.N:
            return self.result.append(self.column[:])
        else:
            for col in range(self.N):
                if self.is_safe(col):
                    self.column[self.row] = col
                    self.row += 1
                    self.solve()
                    self.row -= 1

    def is_safe(self, col):
        """
        Checks if it is safe to place queen diagonally,
        horizontally or vertical
        """
        for i in range(self.row):
            if (
                    self.column[i] == col or
                    self.column[i] - i == col - self.row or
                    self.column[i] + i == col + self.row
            ):
                return False
        return True

    def print_solutions(self):
        """ Print all the solutions """
        for solution in self.result:
            formatted_solution = [[i, col] for i, col in enumerate(solution)]
            print(formatted_solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    N = sys.argv[1]

    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    n_queens = Nqueens(int(sys.argv[1]))
    n_queens.solve()
    n_queens.print_solutions()
