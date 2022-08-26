#DFS Approach
#Time Complexity : O(n) 
#Space Complexity :O(h) 
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No


class Solution:
    def __init__(self):
        self.flag = True
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        self.dfs(root.left, root.right)
        return self.flag       
        
    def dfs(self, left, right):
        #base
        if left == None and right == None:
            return
        if ((left == None) or (right == None) or (left.val != right.val)):
            self.flag = False
            return
            
        #logic
        if(self.flag):
            self.dfs(left.left, right.right)
        #st.pop()
        if(self.flag):
            self.dfs(left.right, right.left)
        #st.pop()
