import re

operations = {
    "*" : lambda a,b: a*b,
    "/" : lambda a,b: a//b,
    "+" : lambda a,b: a+b,
    "-" : lambda a,b: a-b,
}

md_regex = re.compile(r"[*/]")
as_regex = re.compile(r"[+-]")

def solve_multiply_divide(s):
    nums = list(map(int,md_regex.split(s)))
    ops = md_regex.findall(s)

    answer = nums[0]
    for i in range(1,len(nums)):
        num = nums[i]
        op = ops[i-1]
        answer = operations[op](answer,num)
    return answer

def solve_add_subtract(s):
    nums = list(map(solve_multiply_divide,as_regex.split(s)))
    ops = as_regex.findall(s)

    answer = nums[0]
    for i in range(1,len(nums)):
        num = nums[i]
        op = ops[i-1]
        answer = operations[op](answer,num)
    return answer

def calc(s):
    s = s.replace(" ","")
    return solve_add_subtract(s)
