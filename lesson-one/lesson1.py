class Thomas_Uptergrove:

    is_awesome = None

    def init(self):
        self.is_awesome = True

    def sees_math(self):
        print("heck yeah!")


class L_Cubed:

    is_awesome = None

    def init(self):
        self.is_awesome = True

    def sees_math(self):
        print("hecken get me out of here!")


def sees_math():
    print("oh heck")


tom = Thomas_Uptergrove()
lauren = L_Cubed()

print(lauren.is_awesome)
