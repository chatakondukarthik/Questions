### UNDERWORK ###
# Return any binary tree that matches the given preorder and postorder traversals.Values in the traversals pre and post are distinct positive integers.
# input: pre=[1,2,4,5,3,6,7], post= [4,5,2,6,7,3,1]
# output: [1,2,3,4,5,6,7]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):

        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def constructFromPrePost(self, pre, post):
        def make(i0, i1, N):
            if N == 0:
                return None
            root = TreeNode(pre[i0])
            if N == 1:
                return root

            for L in range(N):
                if post[i1 + L - 1] == pre[i0 + 1]:
                    break

            root.left = make(i0 + 1, i1, L)
            root.right = make(i0 + L + 1, i1 + L, N - 1 - L)
            return root

        return make(0, 0, len(pre))


pre = [1, 2, 4, 5, 3, 6, 7]
post = [4, 5, 2, 6, 7, 3, 1]
x = Solution()
print(x.constructFromPrePost(pre, post).val)
