import demo1_l3 as demo


class Second_schoo(demo.Our_school):
    def __init__(self):
        super().__init__("crappy school", 2000, 4.0)

    def __str__(self):
        return f"our students are stressed because our school is {self.rate()}"


example = Second_schoo()

print(example)
