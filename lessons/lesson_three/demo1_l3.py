import math


class Our_school:
    def __init__(self, name: str, population: int, avg_gpa: float):
        self.name = name
        self.population = population
        if avg_gpa > 3.0:
            self.is_good_school = True
        else:
            self.is_good_school = False
        self.avg_gpa = avg_gpa

    def __str__(self):
        return f"{self.name} is {self.rate()}"

    def rate(self):
        if self.is_good_school:
            return "a good school"
        elif not self.is_good_school:
            return 'definately a "school" maybe?'


if __name__ == "__main__":
    school = Our_school("great school", 3, 2.74)

    print(school)
