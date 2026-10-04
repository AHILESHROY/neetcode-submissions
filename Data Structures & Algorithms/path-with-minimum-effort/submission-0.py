import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])

        effort = [[float('inf')] * cols for _ in range(rows)]
        effort[0][0] = 0

        # (effort, row, col)
        heap = [(0, 0, 0)]

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while heap:
            curr_effort, row, col = heapq.heappop(heap)

            # Reached destination with minimum possible effort
            if row == rows - 1 and col == cols - 1:
                return curr_effort

            # Ignore outdated heap entry
            if curr_effort > effort[row][col]:
                continue

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    diff = abs(
                        heights[nr][nc] -
                        heights[row][col]
                    )

                    new_effort = max(curr_effort, diff)

                    if new_effort < effort[nr][nc]:
                        effort[nr][nc] = new_effort
                        heapq.heappush(
                            heap,
                            (new_effort, nr, nc)
                        )

        return 0