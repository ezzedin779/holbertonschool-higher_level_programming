#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    if len(argv)  == 4:
        operator = argv[2]
        if operator == "+":
            result = add(int(argv[1]), int(argv[3]))
            print("{} {} {} = {}".format(argv[1], operator, argv[3], result))
        elif operator == "-":
            result = sub(int(argv[1]), int(argv[3]))
            print("{} {} {} = {}".format(argv[1], operator, argv[3], result))
        elif operator == "*":
            result = mul(int(argv[1]), int(argv[3]))
            print("{} {} {} = {}".format(argv[1], operator, argv[3], result))
        elif operator == "/":
            result = div(int(argv[1]), int(argv[3]))
            print("{} {} {} = {}".format(argv[1], operator, argv[3], result))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

