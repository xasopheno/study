from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        height = len(mat)
        width = len(mat[0])
        new_mat = [[0 for i in range(width)] for j in range(height)]
        for y in range(height):
            for x in range(width):
                box_total = 0
                for j in range(max(0, y - K), min(y + K + 1, height)):
                    for i in range(max(0, x - K), min(x + K + 1, width)):
                        box_total += mat[j][i]
                new_mat[y][x] = box_total

        return new_mat


s = Solution()
print(s.matrixBlockSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1))
