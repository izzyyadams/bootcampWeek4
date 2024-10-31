class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []  
        currentString = ""
        timesToRepeat = 0 

        for item in s:
            if item.isdigit():
                timesToRepeat =  timesToRepeat * 10 + int(item)
            elif item == "[":
                stack.append(currentString)
                stack.append(timesToRepeat)
                timesToRepeat = 0  
                currentString = ""
            elif item == "]":
                repeat = stack.pop()
                lastString = stack.pop() 
                currentString = lastString + (currentString * repeat)
            else:
                currentString += item  
        return currentString
