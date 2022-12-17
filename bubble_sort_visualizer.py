import turtle
import random
import time


class Colors:
    background = "#efe6d5"
    moving = "#e73213"
    stationary = "#9dbeb7"
    finished = "#478376"


SORTING_SPEED = 0.01 # 1 is slow, and 0 is fastest
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
NUM_OF_BARS = 50
BAR_WIDTH = (SCREEN_WIDTH * 0.60) // NUM_OF_BARS
BAR_PADDING = BAR_WIDTH // 2
MIN_BAR_HEIGHT = 10
MAX_BAR_HEIGHT = 750
screen = turtle.Screen()


def bubble_sort(bars):
    n = len(bars)
    a_swap_has_occurred = False

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if bars[j] > bars[j + 1]:
                a_swap_has_occurred = True
                bars[j], bars[j + 1] = bars[j + 1], bars[j]
                generate_bars(bars, j + 1, False)

        if not a_swap_has_occurred:
            return
    
    generate_bars(bars, 0, True)
    

def exit_window():
    screen.bye()
    exit(1)


def generate_random_bars():
    bars = []
    for _ in range(NUM_OF_BARS):
        n = random.randint(MIN_BAR_HEIGHT, MAX_BAR_HEIGHT)
        bars.append(n)
    return bars


def generate_bars(bars, currently_moving, is_done):
    turtle.clear()
    
    bar_x = -450
    bar_y = -475

    for idx, bar in enumerate(bars):
        bar_color = Colors.stationary
        if idx is currently_moving and not is_done:
            bar_color = Colors.moving
        elif is_done:
            bar_color = Colors.finished
        draw_bar(bar_x, bar_y, BAR_WIDTH, bar, bar_color)
        bar_x += BAR_WIDTH + BAR_PADDING

    turtle.update()
    time.sleep(SORTING_SPEED)


def draw_bar(x, y, w, h, color):
    turtle.color(color)
    turtle.up()
    turtle.goto(x, y)
    turtle.seth(0)
    turtle.down()
    turtle.begin_fill()

    turtle.fd(w)
    turtle.left(90)
    turtle.fd(h)
    turtle.left(90)
    turtle.fd(w)
    turtle.left(90)
    turtle.fd(h)
    turtle.left(90)
    
    turtle.end_fill()


def init_turtle():
    screen.title("Bubble Sort Visualizer")
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.tracer(0)
    
    screen.listen()
    screen.onkeypress(exit_window, "Escape")
    
    turtle.speed(0)
    turtle.hideturtle()
    turtle.bgcolor(Colors.background)
    
    bubble_sort(generate_random_bars())


init_turtle()
turtle.done()
