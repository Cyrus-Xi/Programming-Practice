#!/usr/bin/env

"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally 
or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        
        island_ct = 0
        for ri, row in enumerate(grid):
            for ci, cell in enumerate(row):
                if cell == '1':
                    self.dfs(grid, ri, ci)
                    island_ct += 1
                    
        return island_ct
                    
    def dfs(self, grid, rowi, coli):
        offsets = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        neighbor_indices = [(rowi + i, coli + j) for i, j in offsets]
        neighbor_indices = [(ri, ci) for ri, ci in neighbor_indices if ri >= 0 and ci >= 0 
                            and ri < len(grid) and ci < len(grid[0])]

        grid[rowi][coli] = 'x'
        
        for i, j in neighbor_indices:
            if grid[i][j] == '1': self.dfs(grid, i, j)
