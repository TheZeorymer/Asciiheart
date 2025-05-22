import os
import math
import time

def clear_screen():
    
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_heart_frame(t):
    heart = []
    for y in range(-6, 6):
        line = ""
        for x in range(-6, 6):
            if (x**2 + (y - (math.sqrt(abs(x))))**2 - 1)**3 - (x**2 * (y**3)) <= 0:
                line += '*'
            else:
                line += ' '
        heart.append(line)
    return heart

def display_heart(heart):
    clear_screen()
    for line in heart:
        print(line)

def rotate_heart():
    while True:
        for t in range(0, 360, 10):
            heart_frame = generate_heart_frame(t)
            display_heart(heart_frame)
            time.sleep(0.1)

if __name__ == "__main__":
    rotate_heart()