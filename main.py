from converter import GenerateConvertingDict
from render import render
from utils import *

if __name__ == "__main__":
    print("Select your font:")
    file_path = file_selector("./fonts")
    font = Font(GenerateConvertingDict(file_path))

    text = "something"
    while text != "":
        text = input("Input your text (to stop input nothing): ")
        render(text, font, spacing=0)