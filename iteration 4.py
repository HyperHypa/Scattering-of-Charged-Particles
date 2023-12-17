import matplotlib.pyplot as plt
import numpy as np

# moving particle and resting particle
class par: # particle class

  #vacuum electric permittivity
  vep = 8.8541878128 * 10**-12

# self, mass, electric charge, x acceleration, y acceleration, x velocity, y velocity, x position, y position
  def __init__(self, m, e, xa, ya, xv, yv, xp, yp): 
    self.m = m # (kg)
    self.e = e # (coulomb)
    self.xa = xa # (m/s^2)
    self.xas = [xa]
    self.ya = ya # (m/s^2)
    self.yas = [ya]
    self.xv = xv # (m/s)
    self.xvs = [xv]
    self.yv = yv # (m/s)
    self.yvs = [yv]
    self.xp = xp # (m)
    self.xps = [xp]
    self.yp = yp # (m)
    self.yps = [yp]
  
  def next_position(self):
    self.xp = self.xp + self.xv * time_interval
    self.xps.append(self.xp)
    self.yp = self.yp + self.yv * time_interval
    self.yps.append(self.yp)

  def next_velocity(self):
    self.xv = self.xv + self.xa * time_interval
    self.xvs.append(self.xv)
    self.yv = self.yv + self.ya * time_interval
    self.yvs.append(self.yv)
  
  def next_acceleration(self, other):
    dx = abs(self.xp - other.xp)
    dy = abs(self.yp - other.yp)
    self.xa = (dx * self.e * other.e) / ((dx**2 + dy**2)**1.5 * 4 * np.pi * par.vep * self.m)
    if self.xp < other.xp:
      self.xa = -self.xa
    self.xas.append(self.xa)
    self.ya = (dy * self.e * other.e) / ((dx**2 + dy**2)**1.5 * 4 * np.pi * par.vep * self.m)
    if self.yp < other.yp:
      self.ya = -self.ya
    self.yas.append(self.ya)

# main computational loop
time_interval = 0.2
total_time = 20
ts = np.arange(0, total_time+time_interval, time_interval)

# alpha particle
apm = 6.6446573357 * 10**-27
apc = 2 * 1.602176634 * 10**-19
hmax = 50
hs = np.arange(0, hmax+0.01, 0.01)
aps = []
for h in hs:
  aps.append(par(apm, apc, 0, 0, 2, 0, 0, h))
  
ap1 = par(apm, apc, 0, 0, 2, 0, 0, 0)
# par2 is an gold nucleus
gnm = 196.966543 * 1.660539 * 10**-27
gnc = 79 * 1.602176634 * 10**-19
gn = par(gnm, gnc, 0, 0, 0, 0, 10, 0)

# main computation loop
for t in ts[1:]:
  i = 0
  for h in hs:
    aps[i].next_position()
    aps[i].next_velocity()
    aps[i].next_acceleration(gn)
    i = i + 1

# computation loop for finding the angle
angles = []
i = 0
for h in hs:
    angle = np.degrees(np.arctan(aps[i].yv / aps[i].xv))
    if angle < 0:
      angle = 180 + angle
    elif angle == 0:
      angle = 180
    elif angle > 0:
      angle = angle
    angles.append(angle)
    i = i + 1
print(angles)

# plotting the angle against h
i = 0
plt.plot(hs, angles)
plt.ylabel('Resulting angle (°)')
plt.xlabel('H (m)')
plt.title('The resulting angle against H')
plt.show()
