import unittest
from main import EightPuzzle
from main import NodeComputation


class TestEightPuzzle(unittest.TestCase):
    def test_output(self):
        puzzle = EightPuzzle(3)
        self.assertAlmostEqual(EightPuzzle.is_solvable(self,[[1, 8, 2], [0, 4, 3], [7, 6, 5]]), True)


if __name__ == '__main__':
    unittest.main()
