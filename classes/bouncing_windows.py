import random

import win32gui

from constants import MAX_SPEED, WIDTH, HEIGHT


class BouncingWindow:
    def __init__(self, hwnd: int):
        self.hwnd = hwnd
        self.y_move_vector = random.randint(-MAX_SPEED, MAX_SPEED)
        self.x_move_vector = random.randint(-MAX_SPEED, MAX_SPEED)

        self.origin_bbox = win32gui.GetWindowRect(self.hwnd)
        self.width = self.origin_bbox[2] - self.origin_bbox[0]
        self.height = self.origin_bbox[3] - self.origin_bbox[1]

    def set_initial_position(self):
        if self.width >= WIDTH // 2:
            self.width = WIDTH // 2
        if self.height >= HEIGHT // 2:
            self.height = HEIGHT // 2
        win32gui.MoveWindow(self.hwnd, 10, 10, self.width, self.height, True)

    def move(self):
        bbox = win32gui.GetWindowRect(self.hwnd)
        x_1, y_1, x_2, y_2 = bbox
        if y_1 < 0 or y_2 > HEIGHT:
            self.y_move_vector = -self.y_move_vector
        if x_1 < 0 or x_2 > WIDTH:
            self.x_move_vector = -self.x_move_vector

        x_1 += self.x_move_vector
        y_1 += self.y_move_vector
        win32gui.MoveWindow(self.hwnd, x_1, y_1, self.width, self.height, True)

    def set_back_to_initial_state(self):
        win32gui.MoveWindow(self.hwnd, self.origin_bbox[0], self.origin_bbox[1],
                            self.origin_bbox[2], self.origin_bbox[3], False)
