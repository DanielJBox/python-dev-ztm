import pygame
import random

# Initialize pygame
pygame.init()

# Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
purple = (128, 0, 128)
pink = (255, 192, 203)

# Display dimensions
display_width = 600
display_height = 400

# Create the game window
dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

# Define the snake properties
snake_block = 10
snake_speed = 10

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


# Helper functions
def score_display(score):
    value = score_font.render("Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [display_width / 6, display_height / 3])


# Main game function
def game_loop():
    game_over = False
    game_close = False

    x1 = display_width / 2
    y1 = display_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(
        random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    foody = round(
        random.randrange(0, display_height - snake_block) / 10.0) * 10.0

    clock = pygame.time.Clock()

    game_over_msg = "Game Over! Womp Womp. Press Q to quit or C to play again."

    while not game_over:

        while game_close:
            dis.fill(pink)
            message(game_over_msg, red)
            score_display(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Check boundaries
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(pink)
        pygame.draw.rect(dis, yellow, [foodx, foody, snake_block, snake_block])
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        score_display(length_of_snake - 1)

        pygame.display.update()

        # Check if the snake ate the food
        if x1 == foodx and y1 == foody:
            foodx = round(
                random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            foody = round(
                random.randrange(0, display_height - snake_block) /
                10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


# Run the game
game_loop()
