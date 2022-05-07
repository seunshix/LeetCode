class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x : x[1], reverse = True)
        result = 0
        for box in boxTypes:
            if box[0] < truckSize:
                truckSize -= box[0]
                result += box[0] * box[1]
            else:
                result += truckSize * box[1]
                break
        return result