class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
        if not grid or not grid[0]:  # check for empty grid
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def dfs(r, c):
            # If out of bounds, already visited, or water, stop recursion
            if (r < 0 or r >= rows or c < 0 or c >= cols or
                    grid[r][c] == 'W' or (r, c) in visited):
                return
            # Mark the current cell as visited
            visited.add((r, c))
            # Explore neighboring cells (up, down, left, right)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Traverse the grid
        for r in range(rows):
            for c in range(cols):
                # If we find an unvisited land cell, it's a new island
                if grid[r][c] == 'L' and (r, c) not in visited:
                    islands += 1
                    dfs(r, c)  # Perform DFS to mark the whole island

        return islands
# Dispatch 1
solution = Solution()
grid1 = [
    ["L", "L", "L", "L", "W"],
    ["L", "L", "W", "L", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "W", "W", "W"],
]
print("Dispatch 1 Output:", solution.getTotalIsles(grid1))  # Expected output: 1

# Dispatch 2
grid2 = [
    ["L", "L", "W", "W", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "L", "W", "W"],
    ["W", "W", "W", "L", "L"],
]
print("Dispatch 2 Output:", solution.getTotalIsles(grid2)) 


