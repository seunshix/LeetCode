class Solution:
	def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

		count = dict()

		for num in arr:
			if num in count:
				count[num] += 1
			else:
				count[num] = 1

		sorted_nums = sorted(count, key=lambda x : count[x]) # sorting the dictionary based on the count

		if k == 0:
			return len(count)

		for key in sorted_nums:

			k -= count[key]
			del count[key]

			if k == 0:
				return len(count)
			if k < 0:
				return len(count) + 1