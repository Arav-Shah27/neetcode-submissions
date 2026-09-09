# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        result_arr = []
        n = len(pairs)
        if n == 0:
            return result_arr
        # Work on a copy to avoid mutating original input
        arr = pairs[:]  

        # Add the initial state
        result_arr.append(arr[:])

        for i in range(1, n):
            key_pair = arr[i]
            j = i - 1

            # Move elements that are greater than key_pair.key one position ahead
            while j >= 0 and arr[j].key > key_pair.key:
                arr[j + 1] = arr[j]
                j -= 1

            # Insert key_pair at correct position
            arr[j + 1] = key_pair

            # Append the current state (copy)
            result_arr.append(arr[:])

        return result_arr
