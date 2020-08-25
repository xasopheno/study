class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        vds = self.value_depths(root)
        print(vds)

    def value_depths(self, node, vds=[], depth=1):
        if not node:
            return vds
        vds.append({depth: node.value})
        vds += self.value_depths(node.right, vds, depth + 1)
        vds += self.value_depths(node.left, vds, depth + 1)
        return vds


s = Solution()
print(s.deepestLeavesSum(root))
