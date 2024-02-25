import pygame
import math

# 定义墙壁碰撞时间计算函数
def wall_time(pos, vel, sigma):
    if vel > 0.0:
        del_t = (1.0 - sigma - pos) / vel
    elif vel < 0.0:
        del_t = (pos - sigma) / abs(vel)
    else:
        del_t = float('inf')
    return del_t

# 初始化 Pygame
pygame.init()

# 设置窗口大小
win_size = 800
win = pygame.display.set_mode((win_size, win_size))

# 设置球的半径和颜色
radius = 15
color = (255, 0, 0)

# 初始化球的位置和速度
pos = [0.5, 0.5]
vel = [0.21, 0.12]
sigma = 0.15

# 开始主循环
running = True
while running:
    # 处理 Pygame 事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 计算下一个碰撞事件
    wall_times = [wall_time(pos[i], vel[i], sigma) for i in range(2)]
    next_event = min(wall_times)
    for i in range(2): pos[i] += vel[i] * next_event
    collision_direction = wall_times.index(next_event)
    vel[collision_direction] *= -1.0

    # 清除窗口
    win.fill((0, 0, 0))

    # 绘制球
    pygame.draw.circle(win, color, (int(pos[0]*win_size), int(pos[1]*win_size)), radius)

    # 更新窗口
    pygame.display.flip()

# 退出 Pygame
pygame.quit()
