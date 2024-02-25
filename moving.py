import pygame
import math


# 定义墙壁碰撞时间计算函数
def wall_time(pos, vel, radius, win_size):
    if vel > 0.0:
        del_t = (win_size - radius - pos) / vel
    elif vel < 0.0:
        del_t = (pos - radius) / abs(vel)
    else:
        del_t = float('inf')
    return del_t


# 初始化 Pygame 和时钟
pygame.init()
clock = pygame.time.Clock()

# 设置窗口大小
win_size = 800
win = pygame.display.set_mode((win_size, win_size))

# 设置球的半径和颜色
radius = 15
color = (255, 0, 0)

# 初始化球的位置和速度
pos = [0.5 * win_size, 0.5 * win_size]
vel = [100, 60]  # 速度单位为像素/秒

# 设置时间步长
dt = 0.01

# 开始主循环
running = True
while running:
    # 处理 Pygame 事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 计算下一个碰撞事件
    wall_times = [wall_time(pos[i], vel[i], radius, win_size) for i in range(2)]
    next_event = min(wall_times)

    if next_event <= dt:
        for i in range(2): pos[i] += vel[i] * next_event
        collision_direction = wall_times.index(next_event)
        vel[collision_direction] *= -1.0
    else:
        for i in range(2): pos[i] += vel[i] * dt

    # 清除窗口并设置为白色
    win.fill((255, 255, 255))

    # 绘制黑色边框
    # border_thickness = 10
    # pygame.draw.rect(win, (0, 0, 0), pygame.Rect(0, 0, win_size, win_size), border_thickness)

    # 绘制球
    pygame.draw.circle(win, color, (int(pos[0]), int(pos[1])), radius)

    # 更新窗口
    pygame.display.flip()

    # 限制帧率
    clock.tick(60)

# 退出 Pygame
pygame.quit()
