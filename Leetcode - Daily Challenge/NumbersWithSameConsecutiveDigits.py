class Solution:
    # The idea is to use BFS to try appending 0 - 9 to each number
    # starting from a single digit 1 - 9 until the number has n digits
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = []
        d = deque((1, d) for d in range(1, 10))
        while d:
            pos, num = d.pop()
            if pos == n:
                ans.append(num)
            else:
                for j in range(10):
                    if abs(num % 10 - j) == k:
                        d.append((pos + 1, num * 10 + j))
        return ans
