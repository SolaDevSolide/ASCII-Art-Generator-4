from utils import Font

def render(text, font: Font, spacing = 1):
    output = ""
    for row in range(font.getHeight()):
        line = ""
        for char in text:
            line += font.getCharacter(char, row=row)
            if row != font.getHeight() - 1: line += font.getCharacter(' ', row=row) * spacing
        line += '\n'
        output += line

    print(output)