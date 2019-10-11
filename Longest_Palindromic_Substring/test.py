from lps import lps

tests = {}

def add_test(name,args,expected):
    if type(args) != tuple:
        args = (args,)
    tests[name] = (args,expected)

def run_all_tests(f):
    num_passed = 0
    for name in tests:
        args,expected = tests[name]
        arg_string = "(%r)" % args[0] if len(args) == 1 else str(args)
        print("\033[1;36m>>>",f.__name__ + arg_string ,"\033[0m")
        try:
            actual = f(*args)
            print("Output:","%r" % actual)
            if(expected != actual):
                print("\033[1;33mExpected: %r" % expected ,"\033[0m")
            else:
                print("\033[1;32m✅ PASS" ,"\033[0m")
                num_passed += 1
        except Exception as e:
            print("\033[1;31m" + type(e).__name__ + ":", e ,"\033[0m")

        print()

    num_failed = len(tests) - num_passed
    print("Passed: %d" % num_passed)
    print("Failed: %d" % num_failed)

add_test("Example 1",("babad"),expected = "aba")
add_test("Example 2",("cbbd"),expected = "bb")

run_all_tests(lps)
