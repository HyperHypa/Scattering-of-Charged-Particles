import matplotlib.pyplot as plt
import numpy as np


# moving particle and resting particle
class par:  # particle class

    # vacuum electric permittivity
    vep = 8.8541878128 * 10 ** -12

    # self, mass, electric charge, x acceleration, y acceleration, x velocity, y velocity, x position, y position
    def __init__(self, m, e, xa, ya, xv, yv, xp, yp):
        self.m = m  # (kg)
        self.e = e  # (coulomb)
        self.xa = xa  # (m/s^2)
        self.ya = ya  # (m/s^2)
        self.xv = xv  # (m/s)
        self.yv = yv  # (m/s)
        self.xp = xp  # (m)
        self.yp = yp  # (m)

    def next_position(self):
        self.xp = self.xp + self.xv * time_interval
        self.yp = self.yp + self.yv * time_interval

    def next_velocity(self):
        self.xv = self.xv + self.xa * time_interval
        self.yv = self.yv + self.ya * time_interval

    def next_acceleration(self, other):
        dx = abs(self.xp - other.xp)
        dy = abs(self.yp - other.yp)
        self.xa = (dx * self.e * other.e) / ((dx ** 2 + dy ** 2) ** 1.5 * 4 * np.pi * par.vep * self.m)
        if self.xp < other.xp:
            self.xa = -self.xa
        self.ya = (dy * self.e * other.e) / ((dx ** 2 + dy ** 2) ** 1.5 * 4 * np.pi * par.vep * self.m)
        if self.yp < other.yp:
            self.ya = -self.ya


# main computational loop
time_interval = 0.2
total_time = 15
ts = np.arange(0, total_time + time_interval, time_interval)

# alpha particle
apm = 6.6446573357 * 10 ** -27
apc = 2 * 1.602176634 * 10 ** -19
hmax = 10000
hs = np.arange(0, hmax + 0.01, 0.01)
aps = []
for h in hs:
    aps.append(par(apm, apc, 0, 0, 2, 0, 0, h))

# atom nucleus
anm = 196.966543 * 1.660539 * 10 ** -27
anc = 79 * 1.602176634 * 10 ** -19
ans = []
cs = []
for cm in range(1, 101):
    ans.append(par(anm, cm * anc, 0, 0, 0, 0, 10, 0))
    cs.append(cm * anc)

# main computation loop

eas = []

for c in range(len(cs)):
    i = 0
    for h in hs:
        for t in ts[1:]:
            aps[i].next_position()
            aps[i].next_velocity()
            aps[i].next_acceleration(ans[c])
        print(h, "           ", np.arctan(aps[i].yv / aps[i].xv))
        if 0.01745329 > np.arctan(aps[i].yv / aps[i].xv) > 0:  # 0.01745329 radians = 1 degree
            eas.append(h)
            break
        i = i + 1

print(
    eas)  # [46.64, 67.03, 82.54, 95.58, 107.04, 117.39, 126.9, 135.75, 144.05, 151.9, 159.37, 166.5, 173.34, 179.92000000000002, 186.26, 192.4, 198.35, 204.13, 209.74, 215.21, 220.55, 225.75, 230.84, 235.83, 240.70000000000002, 245.48000000000002, 250.17000000000002, 254.78, 259.3, 263.74, 268.11, 272.42, 276.65000000000003, 280.82, 284.93, 288.98, 292.97, 296.92, 300.8, 304.64, 308.44, 312.18, 315.88, 319.54, 323.16, 326.74, 330.28000000000003, 333.78000000000003, 337.24, 340.67, 344.07, 347.43, 350.76, 354.06, 357.32, 360.56, 363.77, 366.95, 370.11, 373.24, 376.34000000000003, 379.41, 382.47, 385.49, 388.5, 391.48, 394.44, 397.37, 400.29, 403.18, 406.06, 408.91, 411.74, 414.55, 417.35, 420.13, 422.88, 425.62, 428.35, 431.05, 433.74, 436.41, 439.07, 441.71000000000004, 444.33, 446.94, 449.53000000000003, 452.11, 454.68, 457.23, 459.76, 462.28000000000003, 464.79, 467.29, 469.77, 472.24, 474.69, 477.13, 479.57, 481.98]

# plotting the angle against h
i = 0
plt.plot(eas, cs)
plt.xlabel('H (m)')
plt.ylabel('Charge (coulomb)')
plt.title('The nucleus charge against H')
plt.show()
