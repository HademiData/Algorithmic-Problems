'''

Given a list of items, each with a weight and a value, 
and a maximum weight capacity of a knapsack, determine the maximum total value that can be packed into the knapsack.

'''


def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, capacity+1):
            if weights[i-1] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i-1]] + values[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][capacity]

  
  '''
  In the above code, we first initialize a 2D list dp of size (n+1) x (capacity+1) 
  where n is the number of items. We then iterate over the items and fill in the dp table 
  according to the following recurrence relation:
  
  dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i-1]] + values[i-1])    if weights[i-1] <= j
           dp[i-1][j]    otherwise
           The final answer is stored in dp[n][capacity].
  '''
  
  
