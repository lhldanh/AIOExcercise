def levenshtein_distance(src, target):
    # Step 1: create matrix (len(src) + 1) * (len(target) + 1)
    m = len(src)
    n = len(target)
    dp = [[0 for _ in range(n + 1)] for i in range(m + 1)] 

    # Step 2: first col and first row
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Step 3: fill the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if (src[i - 1] == target[j - 1]): #char match, cost = 0
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    
    return dp[m][n]
    

assert levenshtein_distance("hi", "hello") == 4
print(levenshtein_distance("hola", "hello"))