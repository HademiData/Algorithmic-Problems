

'''
Problem 1: Edit Distance
Given two strings s1 and s2, find the minimum number of operations required to convert 
s1 to s2, where each operation is either an insertion, deletion, or substitution of a character.
'''


def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        dp[i][0] = i
    for j in range(1, n+1):
        dp[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]
  

  
  '''
  In the above code, we first initialize a 2D list dp of size (m+1) x (n+1) where m and n are 
  the lengths of s1 and s2 respectively. We then fill in the first row and column of the dp table 
  with the number of operations required to convert an empty string to a non-empty prefix of s1 or s2, 
  respectively. We then iterate over the two strings and fill in the dp table according to the following recurrence relation:
  
  dp[i][j] = dp[i-1][j-1]    if s1[i-1] == s2[j-1]
           1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])    otherwise
           The final answer is stored in dp[m][n].
  '''
  
  
'''
  
Problem 2: Unique Paths
Given a m x n grid, find the number of unique paths from the top-left 
corner to the bottom-right corner, where each step can only be taken down or right.
'''


def unique_paths(m, n):
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
       dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]
  
'''
 
In the above code, we first initialize a 2D list dp of
size m x n, where dp[i][j] represents the number of unique paths to reach the 
cell (i,j) from the top-left corner. We then fill in the first row and column 
of the dp table with 1, since there is only one way to reach any cell in the 
first row or column. We then iterate over the remaining cells of the dp table and fill them in according to the following recurrence relation:

dp[i][j] = dp[i-1][j] + dp[i][j-1]

The final answer is stored in dp[m-1][n-1], which represents 
the number of unique paths to reach the bottom-right corner from the top-left corner.
'''




  
  
  
  
  
  
  
  
  
  
  
