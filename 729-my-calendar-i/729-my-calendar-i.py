class MyCalendar:

    def __init__(self):
        self.calendar = []
        

    def book(self, start: int, end: int) -> bool:
        for start1, end1 in self.calendar:
            if start1 < end and start < end1:
                return False
            
        self.calendar.append((start, end))
        return True
        
        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)