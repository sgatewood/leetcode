

# 2) Grow palindromes outward:
# -----------------------------------

def get_expansions(p,s):
    start,end = p
    yield s[start:end+1]
    while (start > 0 and end < len(s)-1) and s[start-1] == s[end+1]:
        start -= 1
        end += 1
        yield s[start:end+1]

def get_initial_palindromes(s):
    for i in range(len(s)):
        yield (i,i)
        if i < len(s) - 1 and s[i] == s[i+1]:
            yield (i,i+1)

def get_all_palindromes(s):
    for p in get_initial_palindromes(s):
        for e in get_expansions(p,s):
            yield e

def lps(s):
    max_palindrome = ""
    for p in get_all_palindromes(s):
        if len(p) > len(max_palindrome):
            max_palindrome = p
    return max_palindrome

# 1) Brute force
# -----------------------------------

def get_all_substrings(s):
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            yield(s[i:j])

def brute_force_lps(s):
    max_found = ""
    for substring in get_all_substrings(s):
        if is_palindrome(substring) and len(substring) > len(max_found):
            max_found = substring
    return max_found
