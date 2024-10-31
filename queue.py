class MyQueue(object):

    def __init__(self):
        self.enqueueStack = []
        self.dequeueStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
            
        self.enqueueStack.append(x)
        

    def pop(self):
        """
        :rtype: int
        """

        if (not self.enqueueStack) and (not self.dequeueStack):
            return None
        elif not self.dequeueStack:
            while self.enqueueStack:
                self.dequeueStack.append(self.enqueueStack.pop())
        
        return(self.dequeueStack.pop())

    def peek(self):
        """
        :rtype: int
        """
        if (not self.enqueueStack) and (not self.dequeueStack):
            return None
        elif not self.dequeueStack:
            while self.enqueueStack:
                self.dequeueStack.append(self.enqueueStack.pop())
        return self.dequeueStack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        if (not self.enqueueStack) and (not self.dequeueStack):
            return True
        else:
            return False
