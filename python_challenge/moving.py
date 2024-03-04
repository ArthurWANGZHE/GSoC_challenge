import pygame
import math



def wall_time(pos, vel, radius, win_size):
    if vel > 0.0:
        del_t = (win_size - radius - pos) / vel
    elif vel < 0.0:
        del_t = (pos - radius) / abs(vel)
    else:
        del_t = float('inf')
    return del_t


pygame.init()
clock = pygame.time.Clock()
win_size = 800
win = pygame.display.set_mode((win_size, win_size))
radius = 15
color = (255, 0, 0)


pos = [0.5 * win_size, 0.5 * win_size]
vel = [100, 60]

dt = 0.01


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    wall_times = [wall_time(pos[i], vel[i], radius, win_size) for i in range(2)]
    next_event = min(wall_times)

    if next_event <= dt:
        for i in range(2): pos[i] += vel[i] * next_event
        collision_direction = wall_times.index(next_event)
        vel[collision_direction] *= -1.0
    else:
        for i in range(2): pos[i] += vel[i] * dt


    win.fill((255, 255, 255))
    pygame.draw.circle(win, color, (int(pos[0]), int(pos[1])), radius)
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
