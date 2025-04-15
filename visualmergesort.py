import pygame
import random

# Initialize
pygame.init()
pygame.font.init()

# Screen settings
WIDTH, HEIGHT = 900, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Merge Sort Visualizer - Enhanced")

# Fonts
title_font = pygame.font.SysFont("arial", 28, bold=True)
info_font = pygame.font.SysFont("arial", 20)

# Array setup
NUM_BARS = 120
array = [0] * (NUM_BARS + 1) # stores height
colors = [(0, 204, 102)] * (NUM_BARS + 1) #initially green color

# Color definitions
color_map = {
    "default": (0, 204, 102), # green
    "compare": (255, 87, 34), # orange 
    "swap": (3, 169, 244), # blue
    "sorted": (139, 195, 74), # light green
    "final": (156, 39, 176) # purple
}

def generate_array(): 
    for i in range(1, NUM_BARS + 1):
        array[i] = random.randint(10, 100)
        colors[i] = color_map["default"]

def draw_array():
    screen.fill((245, 245, 245))  # Light whitish background

    # Header
    screen.blit(title_font.render("Merge Sort Visualizer", True, (33, 33, 33)), (30, 15))
    screen.blit(info_font.render("Press 'ENTER' to sort | Press 'R' to reset", True, (80, 80, 80)), (30, 55))

    # Drawing bars
    bar_width = WIDTH / NUM_BARS
    for i in range(1, NUM_BARS + 1):
        x = i * bar_width
        y = HEIGHT - array[i] * 5
        pygame.draw.rect(screen, colors[i], (x, y, bar_width - 2, array[i] * 5), border_radius=3)

    pygame.display.update()

def merge_sort(start, end):
    if start >= end:
        return

    mid = (start + end) // 2
    merge_sort(start, mid)
    merge_sort(mid + 1, end)
    merge(start, mid, end)

def merge(start, mid, end):
    left = array[start:mid+1]
    right = array[mid+1:end+1]

    i = j = 0
    k = start

    # Jab tak dono arrays khatam nahi ho jaate, compare karte hai elements
    while i < len(left) and j < len(right):
        colors[k] = color_map["compare"]
        draw_array()
        pygame.time.delay(15)

        # smaller element ko merge kar rhe
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1

        colors[k] = color_map["swap"]
        draw_array()
        pygame.time.delay(10)
        colors[k] = color_map["default"] # swap ke bad default
        k += 1

    # agar left ya right me kuch bacha hai to use bhi merge kar lo
    while i < len(left):
        array[k] = left[i]
        i += 1
        colors[k] = color_map["swap"]
        draw_array()
        pygame.time.delay(10)
        colors[k] = color_map["default"]
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        colors[k] = color_map["swap"]
        draw_array()
        pygame.time.delay(10)
        colors[k] = color_map["default"]
        k += 1

    # Final pass to highlight sorted section
    for i in range(start, end + 1):
        colors[i] = color_map["sorted"]
        draw_array()
        pygame.time.delay(5)

# Main game loop
def main():
    generate_array()
    sorting = False
    running = True

    while running:
        draw_array() # continuously drawing bars

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False # after closing window program stops

            # On pressing R array resets
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    generate_array()
                    sorting = False
                    
                # On pressing ENTER sorting starts
                if event.key == pygame.K_RETURN and not sorting:
                    sorting = True
                    merge_sort(1, NUM_BARS)

                    # Highlight final sorted result
                    for i in range(1, NUM_BARS + 1):
                        colors[i] = color_map["final"]
                        draw_array()
                        pygame.time.delay(4)

    pygame.quit()

main()
