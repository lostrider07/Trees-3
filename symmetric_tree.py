#BFS Approach
#Time Complexity : O(n) 
#Space Complexity :O(n)  
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        q = deque()
        q.append(root.left)
        q.append(root.right)
        
        while q:
            left = q.popleft()
            right = q.popleft()
            if left == None and right == None:
                continue
            if (left == None) or (right == None) or (left.val != right.val):
                return False
            q.append(left.left)
            q.append(right.right)
            q.append(left.right)
            q.append(right.left)
        return True


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
