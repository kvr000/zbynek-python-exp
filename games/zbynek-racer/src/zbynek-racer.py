#!/usr/bin/env python3

import random
import time
import pgzrun  # Required to run with pgzero

# Constants
WIDTH = 800  # 10 pixels per character (horizontal)
HEIGHT = 600  # 10 pixels per character (vertical)
CELL_WIDTH = 10
CELL_HEIGHT = 10
COLS = WIDTH // CELL_WIDTH
ROWS = HEIGHT // CELL_HEIGHT
TRACK_WIDTH = 20

# Track data
track = []
track_offset = COLS // 2 - TRACK_WIDTH // 2
offset_dir = 0
offset_counter = 0
kerb_offset = 0

# Player data
player_pos = COLS // 2
player_dir = 0

next_update_time = time.time()
speed = 10.0

distance = 0


def initialize_game():
    global track, track_offset

    track_offset = COLS // 2 - TRACK_WIDTH // 2
    for i in range(0, ROWS):
        track.append([ track_offset, track_offset + TRACK_WIDTH ])

def update_track():
    """Updates the track with a new line, adjusting the offset."""
    global track_offset, offset_dir, offset_counter, kerb_offset

    if offset_counter == 0:
        offset_dir = random.choice([-1, 0, 1])
        offset_counter = random.randint(10, 40)

    new_offset = track_offset + offset_dir
    new_offset = max(1, min(COLS - TRACK_WIDTH - 1, new_offset))
    track.append([ new_offset, new_offset + TRACK_WIDTH ])
    if len(track) > ROWS:
        track.pop(0)
        kerb_offset = 1 - kerb_offset

    track_offset = new_offset
    offset_counter -= 1

def update_car():
    global player_dir, player_pos
    if player_dir < 0:
        if player_pos > 0:
            player_pos = player_pos - 1
    elif player_dir > 0:
        if player_pos < COLS - 1:
            player_pos = player_pos + 1

def update():
    global next_update_time, speed
    global distance

    now = time.time()
    if now >= next_update_time:
        update_car()

        update_track()

        distance = distance + 1

        # Slowly increase the speed by reducing the interval
        if speed < 100:
            speed += 0.02
        next_update_time = now + 1 / speed

def draw():
    """Draws the current game state."""
    global distance, speed

    screen.clear()

    for y, bounds in enumerate(track):
        left = bounds[0] * CELL_WIDTH
        right = bounds[1] * CELL_WIDTH
        top = (ROWS - y - 1) * CELL_HEIGHT

        screen.draw.filled_rect(Rect(0, top, left, CELL_HEIGHT), "green")
        screen.draw.filled_rect(Rect(right, top, COLS * CELL_WIDTH - right, CELL_HEIGHT), "green")
        screen.draw.filled_rect(Rect(left, top, CELL_WIDTH, CELL_HEIGHT), ["white", "red"][(y + kerb_offset)&1])
        screen.draw.filled_rect(Rect(left + CELL_WIDTH, top, right - left - 2 * CELL_WIDTH, CELL_HEIGHT), "gray")
        screen.draw.filled_rect(Rect(right - CELL_WIDTH, top, CELL_WIDTH, CELL_HEIGHT), ["white", "red"][(y + kerb_offset + 1)&1])

    # Draw the player car
    car_x = player_pos * CELL_WIDTH
    car_y = (ROWS - 2) * CELL_HEIGHT
    screen.draw.text("▲", (car_x, car_y), fontsize=CELL_HEIGHT*2, color="red")

    # Draw statistics
    screen.draw.text(f"Speed: {speed*3.6:.1f} km/h", (0, 0), fontsize=CELL_HEIGHT*2, color="darkblue")
    screen.draw.text(f"Distance: {distance/1000.0:.3f} km", (WIDTH - 200, 0), fontsize=CELL_HEIGHT*2, color="darkblue")

def on_key_down(key):
    """Handles user input for moving the car left or right."""
    global player_dir
    if key.name == "LEFT":
        player_dir = -1
    elif key.name == "RIGHT":
        player_dir = 1
    elif key.name == "UP":
        player_dir = 0

initialize_game()

# Launch the game
pgzrun.go()
