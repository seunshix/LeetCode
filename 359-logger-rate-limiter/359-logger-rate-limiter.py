from collections import deque
class Logger:

    def __init__(self):
        self.messageSet = set()
        self.messageQueue = deque()
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        
        while self.messageQueue:
            msg, ts = self.messageQueue[0]
            print("A", msg, ts)
            if timestamp - ts >= 10:
                self.messageQueue.popleft()
                self.messageSet.remove(msg)
            else:
                break
        
        print("B", self.messageQueue)
        print("C", self.messageSet)   
        if message not in self.messageSet:
            self.messageSet.add(message)
            self.messageQueue.append((message, timestamp))
            return True
        else:
            return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)