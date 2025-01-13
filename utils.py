import curses
import os

class Font:
    def __init__(self, font_dict):
        self.__dict = font_dict
        self.__height = len(list(self.__dict.values())[0])

    def getCharacter(self, normal_char, row=-1):
        if row >= 0:
            return self.__dict[normal_char][row]
        return self.__dict[normal_char]

    def getHeight(self):
        return self.__height


def file_selector(directory):
    def selector_logic(stdscr):
        # Disable cursor and enable keypad input
        curses.curs_set(0)
        stdscr.keypad(True)

        files = os.listdir(directory)
        if not files:
            stdscr.addstr(0, 0, "No files found in the directory.")
            stdscr.refresh()
            stdscr.getch()
            return None

        selected_index = 0

        while True:
            stdscr.clear()

            stdscr.addstr(0, 0, f"Select a file from: {directory}")
            stdscr.addstr(1, 0, "Use arrow keys to navigate and Enter to select.")

            for idx, file in enumerate(files):
                if idx == selected_index:
                    stdscr.addstr(idx + 2, 0, f"> {file}", curses.A_REVERSE)
                else:
                    stdscr.addstr(idx + 2, 0, f"  {file}")

            key = stdscr.getch()

            if key == curses.KEY_UP and selected_index > 0:
                selected_index -= 1
            elif key == curses.KEY_DOWN and selected_index < len(files) - 1:
                selected_index += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                return os.path.join(directory, files[selected_index])

    return curses.wrapper(selector_logic)