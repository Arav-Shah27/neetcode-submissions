class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output = []
        x, y = 0, len(numbers) - 1
        while True:
            add = numbers[x] + numbers[y]
            if add > target:
                y -= 1
            if add < target:
                x += 1
            if add == target:
                output.append(x + 1)
                output.append(y + 1)
                break
        return output