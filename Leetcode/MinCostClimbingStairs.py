def minCostClimbingStairs(self, cost: List[int]) -> int:
    for i in range(2, len(cost)):
        cost[i] += min(cost[i-1], cost[i-2])
    return min(cost[len(cost)-1], cost[len(cost)-2])

def minCostClimbingStairs1(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(2, len(cost)):
            cost[i] += min(cost[i-1], cost[i-2])
        return cost[len(cost)-1]

def minCostClimbingStairs(self, cost: List[int]) -> int:
        def fun(cost, n, dp):
            if n==0 or n==1:
                return cost[n]
            dp[n] = cost[n] + min(fun(cost, n-1, dp), fun(cost, n-2, dp))
            return dp[n]
        cost.append(0)
        dp = [0]*len(cost)
        return fun(cost, len(cost)-1, dp)

def minCostClimbingStairs(self, cost: List[int]) -> int:
    def fun(cost, n):
        if n==0 or n==1:
            return cost[n]
        return cost[n] + min(fun(cost, n-1), fun(cost, n-2))
    cost.append(0)
    return fun(cost, len(cost)-1)