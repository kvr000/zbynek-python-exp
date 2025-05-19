#!/usr/bin/env python3

import random
import time
from typing import List, Tuple
import pgzrun  # pgzero runtime
from pgzero.screen import Screen
from pygame import Rect

# Constants
WIDTH = 800
HEIGHT = 600
CELL_WIDTH = 10
CELL_HEIGHT = 10
COLS = WIDTH // CELL_WIDTH
ROWS = HEIGHT // CELL_HEIGHT
TRACK_WIDTH = 20

class RacingGame:
    state: int # -1 crashed, 0 pause, 1 running
    track: List[Tuple[int, int]]
    track_offset: int
    offset_dir: int
    offset_counter: int
    kerb_offset: int

    player_pos: int
    player_dir: int

    next_update_time: float
    speed: float
    distance: int

    def initialize_game(self) -> None:
        self.state = 0
        self.track = []
        self.track_offset = COLS // 2 - TRACK_WIDTH // 2
        self.offset_dir = 0
        self.offset_counter = 0
        self.kerb_offset = 0

        self.player_pos = COLS // 2
        self.player_dir = 0

        self.next_update_time = time.time()
        self.speed = 10.0
        self.distance = 0

        for _ in range(ROWS):
            self.track.append((self.track_offset, self.track_offset + TRACK_WIDTH))

    def update_track(self) -> None:
        if self.offset_counter == 0:
            self.offset_dir = random.choice([-1, 0, 1])
            self.offset_counter = random.randint(10, 40)

        new_offset = self.track_offset + self.offset_dir
        new_offset = max(1, min(COLS - TRACK_WIDTH - 1, new_offset))

        self.track.append((new_offset, new_offset + TRACK_WIDTH))
        if len(self.track) > ROWS:
            self.track.pop(0)
            self.kerb_offset = 1 - self.kerb_offset

        self.track_offset = new_offset
        self.offset_counter -= 1

    def update_car(self) -> bool:
        if self.player_dir < 0 and self.player_pos > 0:
            self.player_pos -= 1
        elif self.player_dir > 0 and self.player_pos < COLS - 1:
            self.player_pos += 1

        if self.player_pos < self.track[1][0] or self.player_pos >= self.track[1][1]:
            self.state = -1
            return False
        else:
            return True

    def update(self) -> None:
        now = time.time()
        if self.state == 1 and now >= self.next_update_time:
            if self.update_car():
                self.update_track()

                self.distance += 1

                self.speed = min(100.0, self.speed + 0.02)

                self.next_update_time = now + 1 / self.speed

    def draw(self, screen: Screen) -> None:
        screen.clear()
        for y, (left_col, right_col) in enumerate(self.track):
            top = (ROWS - y - 1) * CELL_HEIGHT
            left = left_col * CELL_WIDTH
            right = right_col * CELL_WIDTH

            # Green grass
            screen.draw.filled_rect(Rect(0, top, left, CELL_HEIGHT), "green")
            screen.draw.filled_rect(Rect(right, top, COLS * CELL_WIDTH - right, CELL_HEIGHT), "green")

            # Kerbs
            screen.draw.filled_rect(
                Rect(left, top, CELL_WIDTH, CELL_HEIGHT),
                ["white", "red"][(y + self.kerb_offset) & 1]
            )
            screen.draw.filled_rect(
                Rect(right - CELL_WIDTH, top, CELL_WIDTH, CELL_HEIGHT),
                ["white", "red"][(y + self.kerb_offset + 1) & 1]
            )

            # Track surface
            screen.draw.filled_rect(
                Rect(left + CELL_WIDTH, top, right - left - 2 * CELL_WIDTH, CELL_HEIGHT),
                "gray"
            )

        # Draw car
        car_x = self.player_pos * CELL_WIDTH
        car_y = (ROWS - 2) * CELL_HEIGHT
        screen.draw.text("▲", (car_x, car_y), fontsize=CELL_HEIGHT * 2, color="blue")

        # Statistics
        screen.draw.text(f"Speed: {self.speed * 3.6:.1f} km/h", (5, 0), fontsize=CELL_HEIGHT * 2, color="darkblue")
        screen.draw.text(f"Distance: {self.distance / 1000.0:.3f} km", topright=(WIDTH - 5, 0), fontsize=CELL_HEIGHT * 2, color="darkblue")

        # Crash
        if self.state < 0:
            screen.draw.text("You crashed!", center=(WIDTH // 2, HEIGHT // 2), fontsize=CELL_HEIGHT * 10, color="black")

    def on_key_down(self, key) -> None:
        if key.name == "SPACE":
            if self.state == -1:
                self.initialize_game()
                self.state = 0
            elif self.state == 1:
                self.state = 0
            return
        elif key.name == "Q":
            exit()
        if key.name == "LEFT":
            self.player_dir = -1
        elif key.name == "RIGHT":
            self.player_dir = 1
        elif key.name == "UP":
            self.player_dir = 0
        if self.state == 0:
            self.state = 1
            self.next_update_time = time.time()

# Create game instance
game = RacingGame()
game.initialize_game()

# Pygame Zero callbacks
def draw():
    game.draw(screen)

def update():
    game.update()

def on_key_down(key):
    game.on_key_down(key)

pgzrun.go()
