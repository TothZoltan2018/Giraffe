class Chef:
    def make_chicken(self):
        print("The chef makes a chicken")

    def make_salad(self):
        print("The chef makes a salad")
    # alapbol overwrite, az ososztalyban levo fugvennyel valo nevazonossag alapjan
    def make_special_dish(self):
        print("The chef makes a bbq ribs")


# myChef = Chef()
# myChef.make_chicken()

class ChineseChef(Chef):  # oroklodes
    def make_fried_rice(self):
        print("The chef makes a fried rise")

    def make_special_dish(self):
        print("The chef makes orange chicken")


myChineseChef = ChineseChef()
myChineseChef.make_chicken()
myChineseChef.make_fried_rice()
myChineseChef.make_special_dish()
