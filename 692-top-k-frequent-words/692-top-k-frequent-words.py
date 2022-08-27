class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dictionary = {}
        result = []
    
        for word in words:
            if word in dictionary:
                dictionary[word] +=1
            else:
                dictionary[word] = 1 

        for value, key in dictionary.items():
            result.append((value, key))

        result.sort(key=lambda x: (-x[1], x[0]))
        print(result)
        return [i[0] for i in result[:k]]