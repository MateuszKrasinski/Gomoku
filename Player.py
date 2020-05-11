class Player():
    def __init__(self, name_="Gracz", stone_="white"):
        self.name = name_
        self.stone_color = stone_

    def get_stone_color(self):
        return str(self.stone_color)

    def stone_white(self):
        self.stone_color = "white"

    def stone_black(self):
        self.stone_color = "black"

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
