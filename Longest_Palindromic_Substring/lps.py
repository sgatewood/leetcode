# 2) Grow palindromes outward:
# -----------------------------------
def get_all_palindromes(s):
    palindromes = []
    for i in range(len(s)):
        palindromes.append((i,i))
        if i < len(s) - 1 and s[i] == s[i+1]:
            palindromes.append((i,i+1))

    while len(palindromes) != 0:
        palindromes2 = []
        for p in palindromes:
            start = p[0]
            end = p[1]
            yield s[start:end+1]
            if start == 0 or end == len(s)-1:
                continue
            if s[start-1] == s[end+1]:
                palindromes2.append((start-1,end+1))

        palindromes = palindromes2

def grow_lps(s):
    max_palindrome = ""
    for p in get_all_palindromes(s):
        if len(p) > len(max_palindrome):
            max_palindrome = p
    return max_palindrome

# 1) Brute force
# -----------------------------------

def get_all_substrings(s
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            yield(s[i:j])

def brute_force_lps(s):
    max_found = ""
    for substring in get_all_substrings(s):
        if is_palindrome(substring) and len(substring) > len(max_found):
            max_found = substring
    return max_found
