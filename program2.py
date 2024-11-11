def decode_message( s: str, p: str) -> bool:
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
# Base case: both strings are empty, so it matches
    dp[0][0] = True
    # Fill the first row (pattern starts with *)
    for j in range(1, len(p) + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]  # '*' can match an empty string

    # Fill the DP table
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                # '*' matches zero or more characters
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            elif p[j - 1] == '?':
                # '?' matches exactly one character
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Regular character match
                dp[i][j] = dp[i - 1][j - 1] and s[i - 1] == p[j - 1]
# Return whether the entire string matches the entire pattern
    return dp[len(s)][len(p)]
# Test cases
print(decode_message("aa", "*"))  # Expected output: True
print(decode_message("aa", "a"))  # Expected output: False
print(decode_message("cb", "?a"))  # Expected output: False
print(decode_message("aa", "a*"))  # Expected output: True
print(decode_message("cb", "*"))  # Expected output: True


