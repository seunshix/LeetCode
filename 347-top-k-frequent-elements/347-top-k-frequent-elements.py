class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        result = []
    
        for num in nums:
            if num in dictionary:
                dictionary[num] +=1
            else:
                dictionary[num] = 1 
        print(dictionary)

        for value, key in dictionary.items():
            result.append((value, key))

        result.sort(key=lambda x: (-x[1], x[0]))
        print(result)
        return [i[0] for i in result[:k]]
    
        