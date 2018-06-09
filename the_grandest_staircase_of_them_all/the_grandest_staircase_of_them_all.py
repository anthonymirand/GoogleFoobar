def answer(n):
  dp = [ [ 0 for _ in xrange(n) ] for _ in xrange(n + 1) ]

  for j in xrange(3):
    for i in xrange(j, n):
      dp[j][i] = 1

  for i in xrange(3, n + 1):
    for bottom in xrange(2, n):
      dp[i][bottom] = dp[i][bottom - 1]
      if bottom <= i:
        dp[i][bottom] += dp[i - bottom][bottom - 1]

  return dp[n][n - 1]
