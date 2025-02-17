# Given the root of a binary tree, invert the tree, and return its root.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insertNode(self, data): #level order insertion
        if self:
            q = []
            q.append(self)
            while (len(q)):
                temp = q[0]
                q.pop(0)
                if (not temp.left):
                    temp.left = TreeNode(data)
                    break
                else:
                    q.append(temp.left)
 
                if (not temp.right):
                    temp.right = TreeNode(data)
                    break
                else:
                    q.append(temp.right)

    def insertNodes(self, datas):
        for data in datas:
            self.insertNode(data)

class Solution(object):
    def invertTree(self, root):
        if not root:
            return None
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    
    def printLevelOrder(self, root): #Breadth First Traversal
        if root is None:
            return
        queue = []
        out=[]
        queue.append(root)
        while(len(queue) > 0):
            out.append(queue[0].val)
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return out
    
class Test (object):
    def testInvertTree(self, Actual_Tree_Data, Invert_Tree_Data):
        if len(Actual_Tree_Data)!=0:
            root = TreeNode(Actual_Tree_Data[0])
            if len(Actual_Tree_Data)>0:
                root.insertNodes(Actual_Tree_Data[1:])
            s= Solution()
            root = s.invertTree(root)
            assert s.printLevelOrder(root) == Invert_Tree_Data, "Fail"
        else:
            assert Actual_Tree_Data == Invert_Tree_Data, "Fail"
        
if __name__ == '__main__':
    t = Test()
    t.testInvertTree([4,2,7,1,3,6,9], [4,7,2,9,6,3,1])
    t.testInvertTree([2,1,3], [2,3,1])
    t.testInvertTree([0], [0])
    t.testInvertTree([], [])
    print "everything passed"
    
# O(n)
