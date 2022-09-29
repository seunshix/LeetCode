class StockPrice:

    def __init__(self):
      self.timestamps = {} # need to keep track of the timestamps and price at the timestamps
      self.maxTime = 0
      self.minHeap = []
      self.maxHeap = []
        
    def update(self, timestamp: int, price: int) -> None:
       self.timestamps[timestamp] = price
       self.maxTime = max(self.maxTime, timestamp)

       heapq.heappush(self.minHeap, (price, timestamp))
       heapq.heappush(self.maxHeap, (-price, timestamp))
        
    def current(self) -> int:
        # we need to know what the
        return self.timestamps[self.maxTime] 

    def maximum(self) -> int:
      cur_price, timestamp = heapq.heappop(self.maxHeap)
      while -cur_price != self.timestamps[timestamp]:
        cur_price, timestamp = heapq.heappop(self.maxHeap)
      heapq.heappush(self.maxHeap, (cur_price, timestamp))
   
      return -cur_price
        

    def minimum(self) -> int:
      cur_price, timestamp = heapq.heappop(self.minHeap)
      while cur_price != self.timestamps[timestamp]:
        cur_price, timestamp = heapq.heappop(self.minHeap)
      heapq.heappush(self.minHeap, (cur_price, timestamp))
   
      return cur_price
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()