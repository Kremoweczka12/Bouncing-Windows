import win32gui
import pyautogui

from classes.windows_manager import WindowManager


def get_hwnds():
    windows = [element for element in pyautogui.getAllTitles() if element]
    hwnds = [win32gui.FindWindow(None, element) for element in windows]
    hwnds = list(set(hwnds))
    return hwnds


def main():
    hwnds = get_hwnds()
    input("PRESS ENTER TO START, PRESS ESCAPE TO STOP BOUNCING.")
    manager = WindowManager(hwnds)
    manager.run()


if __name__ == '__main__':
    main()
