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


class Solution:
    def maximum69Number(self, num: int) -> int:
        res = num
        num = list(str(num))
        for i in range(len(num)):
            temp = num[i]
            num[i] = '9' if num[i] == '6' else '6'
            no = int("".join(num))
            if res < no:
                res = no
            num[i] = temp
        return res


class Solution:
    def maximum69Number(self, num: int) -> int:
        num = str(num)
        for i in range(len(num)):
            if num[i] == '6':
                num = num.replace('6', '9', 1)
                break
        return int(num)
