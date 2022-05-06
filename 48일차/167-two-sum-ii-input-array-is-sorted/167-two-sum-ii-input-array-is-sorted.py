class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if target >= 0:
            for i in range(len(numbers) - 1):
                temp = target - numbers[i]
                if temp < 0:
                    break
                check = bisect.bisect_left(numbers[i+1:], temp)
                if check < len(numbers) - i - 1 and numbers[check + i + 1] == temp:
                    return (i + 1, i + check + 2)      
        else:
            for i in range(len(numbers) - 1):
                temp = target - numbers[i]
                if temp > 0:
                    break
                check = bisect.bisect_left(numbers[i+1:], temp)
                if check < len(numbers) - i - 1 and numbers[check + i + 1] == temp:
                    return (i + 1, i + check + 2)
        return -1