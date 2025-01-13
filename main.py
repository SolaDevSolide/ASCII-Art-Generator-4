from converter import GenerateConvertingDict
from render import render
from utils import *

if __name__ == "__main__":
    big_dict = GenerateConvertingDict("./fonts/big.flf")
    big_font = Font(big_dict)
    text = input("Input your text: ")
    render(text, big_font, spacing=0)