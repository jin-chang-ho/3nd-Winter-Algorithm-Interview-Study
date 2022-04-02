# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        if not root:
            return ""
        
        queue = collections.deque()
        ser_list = []
        queue.append(root)

        while queue:
            if queue[0] != None:
                if queue[0].left == None:
                    queue.append(None)
                else:
                    queue.append(queue[0].left)

                if queue[0].right == None:
                    queue.append(None)
                else:
                    queue.append(queue[0].right)

            if queue[0] == None:
                ser_list.append(None)
            else:
                ser_list.append(queue[0].val)

            queue.popleft()
        
        while ser_list[-1] == None:
            ser_list.pop()
        
        for i in range(len(ser_list)):
            ser_list[i] = str(ser_list[i])
        
        return " ".join(ser_list)
        

    def deserialize(self, data):
        if data == "":
            return None
        
        data = data.split()
        for i in range(len(data)):
            if data[i] == "None":
                data[i] = None
            else:
                data[i] = int(data[i])
        
        root = TreeNode(data.pop(0))
        queue = collections.deque()
        queue.append(root)
        
        while data:
            node = queue.popleft()
            
            left = data.pop(0)
            if left == None:
                node.left = None
            else:
                temp = TreeNode(left)
                queue.append(temp)
                node.left = temp
                
            if data:
                right = data.pop(0)
            else:
                break
            
            if right == None:
                node.right = None
            else:
                temp = TreeNode(right)
                queue.append(temp)
                node.right = temp
                
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))