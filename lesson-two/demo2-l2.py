
import math


class Quadratic_solver:
    plus = 0.0
    minus = 0.0
    answers = (minus, plus)

    def __init__(self):
        coefficients = self.get_coefficients()
        self.minus = self.minus_case(coefficients)
        self.plus = self.plus_case(coefficients)

    def __str__(self):
        if math.isclose(self.minus, self.plus, rel_tol=0.0001):
            return f"The answer is {self.plus}"
        else:
            return f"The answers are ({self.minus},{self.plus})"

    def get_coefficients(self) -> list:
        a = input("what is the squared number?")
        b = input("what is the number next to X?")
        c = input("what is the constan?")
        return [a, b, c]

    def minus_case(self, nums):
        c = int(nums[2])
        b = int(nums[1])
        a = int(nums[0])

        return ((-b-math.sqrt((b*b)-4*(a*c)))/(2*a))

    @classmethod
    def plus_case(self, nums):
        c = int(nums[2])
        b = int(nums[1])
        a = int(nums[0])

        return ((-b+math.sqrt((b*b)-4*(a*c)))/(2*a))

    @classmethod
    def solve_quadratic(self, nums):
        answers = [
            self.minus_case(nums),
            self.plus_case(nums)
        ]
        return answers

# below is a common python practice
# it is an if statement that checks the name of the module calling it
# if this isn't used any module that imports this file will run ALL the code in the moduel
# so the practice is to put all code that you consider to be exportable outside the if statement
# then you put the code that you want only this module to execute in the statement
# here is a geeks for geeks article that goes more in depth
# https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/
if __name__ == "__main__":
    solver = Quadratic_solver()
    print(solver)
