def decode_message( s: str, p: str) -> bool:
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

# Initialize the DP table for the case where both strings are empty
    dp[0][0] = True
    
    # Handle patterns that start with '*' (matching empty string)
    for j in range(1, len(p) + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    # Fill the DP table
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                # '*' can match zero characters (dp[i][j-1]) or one or more characters (dp[i-1][j])
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            elif p[j - 1] == '?':
                # '?' matches exactly one character
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Regular character must match exactly
                dp[i][j] = dp[i - 1][j - 1] and s[i - 1] == p[j - 1]
    
    # The result is whether the whole message matches the whole pattern
    return dp[len(s)][len(p)]

# Test the function with some examples
print(decode_message("aa", "*"))  # Should return True
print(decode_message("aa", "a"))  # Should return False
print(decode_message("cb", "?a"))  # Should return False
print(decode_message("aa", "a*"))  # Should return True
print(decode_message("cb", "*"))  # Should return True


