import math


def get_coefficients() -> list:
    a = input("what is the squared number?")
    b = input("what is the number next to X?")
    c = input("what is the constan?")
    return [a, b, c]


def minus_case(nums):
    c = int(nums[2])
    b = int(nums[1])
    a = int(nums[0])

    return ((-b-math.sqrt((b*b)-4*(a*c)))/(2*a))


def plus_case(nums):
    c = int(nums[2])
    b = int(nums[1])
    a = int(nums[0])

    return ((-b+math.sqrt((b*b)-4*(a*c)))/(2*a))


def solve_quadratic(nums):
    answers = [
        minus_case(nums),
        plus_case(nums)
    ]
    return answers


def solve_from_dumb_ass():
    nums = get_coefficients()
    answers = solve_quadratic(nums)
    print(f"the answers are {answers[0]},{answers[1]}")



solve_from_dumb_ass()
