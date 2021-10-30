import pygame
import os
import sys


def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)


def add_textures_to_list(t_path: str, t_file: str):
    f_path = resource_path(os.path.join(t_path, t_file))
    obj_text = pygame.image.load(f_path)
    return obj_text


def images_storyboard(anim_count, player_stand, right, left, walk_right,
                      walk_left, x, y, t_r_path: str, t_l_path: str,
                      t_file: str):

    if anim_count + 1 >= 36:
        anim_count = 0

    if right:
        win.blit(walk_right[anim_count // 2], (x, y))
        anim_count += 1
        player_stand = add_textures_to_list(t_r_path, t_file)
    elif left:
        win.blit(walk_left[anim_count // 2], (x, y))
        anim_count += 1
        player_stand = add_textures_to_list(t_l_path, t_file)
    else:
        win.blit(player_stand, (x, y))
    return anim_count, player_stand


def draw_window():
    global anim_count_1, player_stand_1, anim_count_2, player_stand_2
    win.blit(bg, (0, 0))

    anim_count_1, player_stand_1 = images_storyboard(
        anim_count_1, player_stand_1, right_1, left_1, walk_right_1,
        walk_left_1, x_1, y_1, 'PNG/Minotaur_01/PNG Sequences/Walking_right',
        'PNG/Minotaur_01/PNG Sequences/Walking_left', 'Minotaur_01_Stand.png')
    anim_count_2, player_stand_2 = images_storyboard(
        anim_count_2, player_stand_2, right_2, left_2, walk_right_2,
        walk_left_2, x_2, y_2, 'PNG/Minotaur_02/PNG Sequences/Walking_right',
        'PNG/Minotaur_02/PNG Sequences/Walking_left', 'Minotaur_02_Stand.png')

    pygame.display.update()


pygame.init()
win = pygame.display.set_mode((1280, 720))
path = resource_path('Blockheads - Stay the Night.mp3')
pygame.mixer.music.load(path)
pygame.mixer.music.play(-1)

pygame.display.set_caption('Walking Minotaur')

walk_right_1 = []
walk_left_1 = []
walk_right_2 = []
walk_left_2 = []

num_files = 18
for i in range(num_files):
    walk_right_1.append(add_textures_to_list(
        'PNG/Minotaur_01/PNG Sequences/Walking_right',
        f'Minotaur_01_Walking_00{i}.png'))
    walk_left_1.append(add_textures_to_list(
        'PNG/Minotaur_01/PNG Sequences/Walking_left',
        f'Minotaur_01_Walking_00{i}.png'))
    walk_right_2.append(add_textures_to_list(
        'PNG/Minotaur_02/PNG Sequences/Walking_right',
        f'Minotaur_02_Walking_00{i}.png'))
    walk_left_2.append(add_textures_to_list(
        'PNG/Minotaur_02/PNG Sequences/Walking_left',
        f'Minotaur_02_Walking_00{i}.png'))

bg = add_textures_to_list('PNG/Game_background', 'game_background_test.png')
player_stand_1 = add_textures_to_list(
    'PNG/Minotaur_01/PNG Sequences/Walking_right',
    'Minotaur_01_Stand.png')

player_stand_2 = add_textures_to_list(
    'PNG/Minotaur_02/PNG Sequences/Walking_right',
    'Minotaur_02_Stand.png')

clock = pygame.time.Clock()

x_1 = 80
y_1 = 355
width_1 = 180
height_1 = 180
speed_1 = 5

is_jump_1 = False
jump_count_1 = 10

left_1 = False
right_1 = False
anim_count_1 = 0

x_2 = 680
y_2 = 355
width_2 = 180
height_2 = 180
speed_2 = 5

is_jump_2 = False
jump_count_2 = 10

left_2 = False
right_2 = False
anim_count_2 = 0


run_1 = True
run_2 = True
while run_1 and run_2:
    clock.tick(36)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_1 = False
            run_2 = False

    keys_1 = pygame.key.get_pressed()
    if keys_1[pygame.K_LEFT] and x_1 > 5:
        x_1 -= speed_1
        left_1 = True
        right_1 = False
    elif keys_1[pygame.K_RIGHT] and x_1 < 1280 - width_1 - 5:
        x_1 += speed_1
        left_1 = False
        right_1 = True
    else:
        left_1 = False
        right_1 = False
        anim_count_1 = 0
    if not is_jump_1:
        if keys_1[pygame.K_RCTRL]:
            is_jump_1 = True
    else:
        if jump_count_1 >= -10:
            if jump_count_1 < 0:
                y_1 += (jump_count_1 ** 2) / 2
            else:
                y_1 -= (jump_count_1 ** 2) / 2
            jump_count_1 -= 1
        else:
            is_jump_1 = False
            jump_count_1 = 10

    keys_2 = pygame.key.get_pressed()
    if keys_2[pygame.K_a] and x_2 > 5:
        x_2 -= speed_2
        left_2 = True
        right_2 = False
    elif keys_2[pygame.K_d] and x_2 < 1280 - width_2 - 5:
        x_2 += speed_2
        left_2 = False
        right_2 = True
    else:
        left_2 = False
        right_2 = False
        anim_count_2 = 0
    if not is_jump_2:
        if keys_2[pygame.K_SPACE]:
            is_jump_2 = True
    else:
        if jump_count_2 >= -10:
            if jump_count_2 < 0:
                y_2 += (jump_count_2 ** 2) / 2
            else:
                y_2 -= (jump_count_2 ** 2) / 2
            jump_count_2 -= 1
        else:
            is_jump_2 = False
            jump_count_2 = 10

    draw_window()
