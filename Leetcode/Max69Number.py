class Solution:
    def maximum69Number(self, num: int) -> int:
        res = [num]
        num = list(str(num))
        for i in range(len(num)):
            temp = num[i]
            num[i] = '9' if num[i] == '6' else '6'
            res.append(int("".join(num)))
            num[i] = temp
        return max(res)
