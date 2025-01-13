class Font:
    def __init__(self, font_dict):
        self.__dict = font_dict
        self.__height = len(list(self.__dict.values())[0])

    def getCharacter(self, normal_char, row = -1):
        if row >= 0:
            return self.__dict[normal_char][row]
        return self.__dict[normal_char]

    def getHeight(self):
        return self.__height

