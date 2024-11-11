def decode_message( s: str, p: str) -> bool:
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    
    # Base case: Both strings are empty, so it matches
    dp[0][0] = True
    
    # Handle patterns that start with '*' (matching empty string)
    for j in range(1, len(p) + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    # Fill the DP table
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                # '*' matches zero or more characters, so either:
                # - Skip '*' (dp[i][j-1]), meaning it doesn't match anything here
                # - Or match one more character (dp[i-1][j]), meaning '*' matches some characters in s
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            elif p[j - 1] == '?':
                # '?' matches exactly one character
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Regular character must match exactly
                dp[i][j] = dp[i - 1][j - 1] and s[i - 1] == p[j - 1]
    
    # The result is whether the entire string matches the entire pattern
    return dp[len(s)][len(p)]
