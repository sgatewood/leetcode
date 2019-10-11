import re
# [+-]?[\d]+([.][\d]+)?(e[\d]+([.][\d]+)?)?

final = re.compile(r'"[\s]*[+-]?(([\d]+)([.][\d]*)?|([\d]+)?([.][\d]+))(e[+-]?[\d]+)?[\s]*"')

def valid_number(s):
    s = '"%s"' % s
    return final.fullmatch(s) is not None
