characterOrder = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3',
                  '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                  'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[',
                  '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'Ä', 'Ö', 'Ü', 'ä', 'ö',
                  'ü', 'β']


def GenerateConvertingDict(filePath, log=False):
    convertingDict = dict.fromkeys(characterOrder)
    with open(filePath, 'r') as file:
        characterLeft = len(characterOrder)
        while line := file.readline():
            if DetectStartCharacter(line):
                character = [GrabFromLine(line)]
                while not DetectEndCharacter(line):
                    line = file.readline()
                    character.append(GrabFromLine(line))
                convertingDict[characterOrder[len(characterOrder) - characterLeft]] = character
                if log:
                    print(characterOrder[len(characterOrder) - characterLeft])
                    show(character)
                characterLeft -= 1
                if characterLeft == 0:
                    break
    return convertingDict


def DetectStartCharacter(line):
    return line.count("@\n") == 1


def DetectEndCharacter(line):
    return line.count("@@\n") == 1


def GrabFromLine(line):
    """
    Removes the end of line sequence of the font file
    :param line: The line of the font file
    :return: A string composed only of the font's part
    """
    if DetectEndCharacter(line):
        return line[:-3]
    return line[:-2]


def show(character):
    for line in character:
        print(line)
