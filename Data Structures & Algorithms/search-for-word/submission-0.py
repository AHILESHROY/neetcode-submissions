from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def backtrack(r, c, index):
            # Entire word matched
            if index == len(word):
                return True

            # Invalid position or character doesn't match
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != word[index]
            ):
                return False

            # Mark as visited
            temp = board[r][c]
            board[r][c] = "#"

            # Explore all four directions
            found = (
                backtrack(r + 1, c, index + 1) or
                backtrack(r - 1, c, index + 1) or
                backtrack(r, c + 1, index + 1) or
                backtrack(r, c - 1, index + 1)
            )

            # Backtrack
            board[r][c] = temp

            return found

        # Try starting from every cell
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True

        return False