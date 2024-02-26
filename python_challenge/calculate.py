import math

def wall_time(pos, vel, sigma):
    if vel > 0.0:
        del_t = (1.0 - sigma - pos) / vel
    elif vel < 0.0:
        del_t = (pos - sigma) / abs(vel)
    else:
        del_t = float('inf')
    return del_t

pos = [0.5, 0.5]
vel = [0.21, 0.12]
sigma = 0.15
t = 0.0
n_events = 100
for event in range(n_events):
    wall_times = [wall_time(pos[i], vel[i], sigma ) for i in range(2)]
    next_event = min(wall_times)
    t += next_event
    for i in range(2): pos[i] += vel[i] * next_event
    collision_direction = wall_times.index(next_event)
    vel[collision_direction] *= -1.0
    print('event', event)
    print('time', t)
    print('pos', pos)
    print('vel', vel)
