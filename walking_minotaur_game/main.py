import pygame
import os


pygame.init()
win = pygame.display.set_mode((1280, 720))
pygame.mixer.music.load('Blockheads - Stay the Night.mp3')
pygame.mixer.music.play(-1)

pygame.display.set_caption('Walking Minotaur')

walk_right = []
walk_left = []
num_files = len(os.listdir('PNG/Minotaur_01/PNG Sequences/Walking_right')) - 1
for i in range(num_files):
    walk_right.append(pygame.image.load(
        f'PNG/Minotaur_01/PNG Sequences/Walking_right/Minotaur_01_Walking_00{i}.png'
    ))
    walk_left.append(pygame.image.load(
        f'PNG/Minotaur_01/PNG Sequences/Walking_left/Minotaur_01_Walking_00{i}.png'
    ))

bg = pygame.image.load('PNG/Game_background/game_background_test.png')
player_stand = pygame.image.load('PNG/Minotaur_01/PNG Sequences/Walking_right/\
Minotaur_01_Stand.png')

clock = pygame.time.Clock()

x = 80
y = 355
width = 180
height = 180
speed = 5

is_jump = False
jump_count = 10

left = False
right = False
anim_count = 0


def draw_window():
    global anim_count, player_stand
    win.blit(bg, (0, 0))

    if anim_count + 1 >= 36:
        anim_count = 0

    if right:
        win.blit(walk_right[anim_count // 2], (x, y))
        anim_count += 1
        player_stand = pygame.image.load(
            'PNG/Minotaur_01/PNG Sequences/Walking_right/Minotaur_01_Stand.png'
        )
    elif left:
        win.blit(walk_left[anim_count // 2], (x, y))
        anim_count += 1
        player_stand = pygame.image.load(
            'PNG/Minotaur_01/PNG Sequences/Walking_left/Minotaur_01_Stand.png'
        )
    else:
        win.blit(player_stand, (x, y))

    pygame.display.update()


run = True
while run:
    clock.tick(36)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 1280 - width - 5:
        x += speed
        left = False
        right = True
    else:
        left = False
        right = False
        anim_count = 0
    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -10:
            if jump_count < 0:
                y += (jump_count ** 2) / 2
            else:
                y -= (jump_count ** 2) / 2
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10

    draw_window()

pygame.quit()
