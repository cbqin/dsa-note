#
# @lc app=leetcode.cn id=733 lang=python3
#
# [733] 图像渲染
#
# https://leetcode-cn.com/problems/flood-fill/description/
#
# algorithms
# Easy (57.94%)
# Likes:    161
# Dislikes: 0
# Total Accepted:    41K
# Total Submissions: 70.8K
# Testcase Example:  '[[1,1,1],[1,1,0],[1,0,1]]\n1\n1\n2'
#
# 有一幅以二维整数数组表示的图画，每一个整数表示该图画的像素值大小，数值在 0 到 65535 之间。
#
# 给你一个坐标 (sr, sc) 表示图像渲染开始的像素值（行 ，列）和一个新的颜色值 newColor，让你重新上色这幅图像。
#
#
# 为了完成上色工作，从初始坐标开始，记录初始坐标的上下左右四个方向上像素值与初始坐标相同的相连像素点，接着再记录这四个方向上符合条件的像素点与他们对应四个方向上像素值与初始坐标相同的相连像素点，……，重复该过程。将所有有记录的像素点的颜色值改为新的颜色值。
#
# 最后返回经过上色渲染后的图像。
#
# 示例 1:
#
#
# 输入:
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1, sc = 1, newColor = 2
# 输出: [[2,2,2],[2,2,0],[2,0,1]]
# 解析:
# 在图像的正中间，(坐标(sr,sc)=(1,1)),
# 在路径上所有符合条件的像素点的颜色都被更改成2。
# 注意，右下角的像素没有更改为2，
# 因为它不是在上下左右四个方向上与初始点相连的像素点。
#
#
# 注意:
#
#
# image 和 image[0] 的长度在范围 [1, 50] 内。
# 给出的初始点将满足 0 <= sr < image.length 和 0 <= sc < image[0].length。
# image[i][j] 和 newColor 表示的颜色值在范围 [0, 65535]内。
#
#
#

# @lc code=start

from collections import deque


class Solution:
    # def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    #     if image[sr][sc] == newColor:
    #         return image

    #     directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    #     rows = len(image)
    #     cols = len(image[0])

    #     def dfs(i, j, originColor, newColor):
    #         image[i][j] = newColor
    #         for direction in directions:
    #             newi = i+direction[0]
    #             newj = j+direction[1]
    #             if inArea(newi, newj, rows, cols) and image[newi][newj] == originColor:
    #                 dfs(newi, newj, originColor, newColor)

    #     def inArea(i, j, rows, cols):
    #         if 0 <= i < rows and 0 <= j < cols:
    #             return True
    #         else:
    #             return False

    #     dfs(sr, sc, image[sr][sc], newColor)
    #     return image

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image

        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        rows = len(image)
        cols = len(image[0])

        def bfs(sr, sc, originColor, newColor):
            visited = [[0]*cols for _ in range(rows)]
            q = deque([(sr, sc)])
            visited[sr][sc] = 1

            while q:
                i, j = q.popleft()
                image[i][j] = newColor
                for direction in directions:
                    newi = i+direction[0]
                    newj = j+direction[1]
                    if inArea(newi, newj, rows, cols) and not visited[newi][newj] and image[newi][newj] == originColor:
                        q.append((newi, newj))
                        visited[newi][newj] = 1

        def inArea(i, j, rows, cols):
            if 0 <= i < rows and 0 <= j < cols:
                return True
            else:
                return False

        bfs(sr, sc, image[sr][sc], newColor)
        return image

# @lc code=end
