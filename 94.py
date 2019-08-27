class Solution:
    def inorderTraversal_1(self, root):
        res = []
        def helper(root):
            if not root :
                return
            helper(root.left)
            res.append(root.val)
            helper(root.right)
        helper(root)
        return res

    #使用栈实现中序遍历
    def inorderTraversal(self, root):
        res = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            tmp = stack.pop()
            res.append(tmp.val)
            root = tmp.right
        return res