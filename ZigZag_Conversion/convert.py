def convert(s,numRows):
    out = ""
    if numRows == 1:
        return s
    for rowNum in range(numRows):
        base = rowNum
        if base == 0 or base == numRows-1:
            while base < len(s):
                out += s[base]
                base += 2*(numRows-1)
        else:
            flip = True
            while base < len(s):
                out += s[base]
                if flip:
                    base += 2*(numRows-rowNum-1)
                else:
                    base += 2*(rowNum)
                flip = not flip
    return out



# First attempt
def convert_lists(s,numRows):
    rows = [[] for i in range(numRows)]

    row_counter = 0
    increment = 1
    if len(rows) <= 1:
        increment = 0
    for i in range(len(s)):
        # print("\033[1;31m", row_counter ,"\033[0m")
        rows[row_counter].append(s[i])
        row_counter += increment
        if row_counter == len(rows)-1 or row_counter == 0:
            increment *= -1
        # print("\033[1;33m", rows ,"\033[0m")

    out = ""
    for row in rows:
        out += "".join(row)
    return out
