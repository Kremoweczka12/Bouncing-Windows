from typing import List

import keyboard
import pywintypes

from classes.bouncing_windows import BouncingWindow
from constants import FINISHING_SHORTCUT


class WindowManager:
    def __init__(self, hwnds: List[int]):
        self.windows = [BouncingWindow(hwnd) for hwnd in hwnds]
        self.save_invoke_loop(BouncingWindow.set_initial_position)

    def __getitem__(self, item):
        return self.windows[item]

    def save_invoke_loop(self, func):
        hwnds_to_remove = []
        for window in self.windows:
            try:
                func(window)
            except pywintypes.error:
                hwnds_to_remove.append(window.hwnd)

        self.windows = [window for window in self.windows if window.hwnd not in hwnds_to_remove]

    def run(self):
        while True:
            if keyboard.is_pressed(FINISHING_SHORTCUT):
                self.save_invoke_loop(BouncingWindow.set_back_to_initial_state)
                return
            else:
                self.save_invoke_loop(BouncingWindow.move)

