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
total_time = 12
ts = np.arange(0, total_time+time_interval, time_interval)

# ap1 is an alpha particle
apm = 6.6446573357 * 10**-27
apc = 2 * 1.602176634 * 10**-19
ap1 = par(apm, apc, 0, 0, 2, 0, 0, 3)

# par2 is an gold nucleus
gnm = 196.966543 * 1.660539 * 10**-27
gnc = 79 * 1.602176634 * 10**-19
gn = par(gnm, gnc, 0, 0, 0, 0, 10, 0)

for t in ts[1:]:
  ap1.next_position()
  ap1.next_velocity()
  ap1.next_acceleration(gn)

print(ap1.e)
# plotting the path of both particles
plt.plot(ap1.xps, ap1.yps)
plt.plot(10,0,'ro') 
plt.xlabel('X')
plt.ylabel('Y')
plt.title('The path of both particles in 2D')
plt.show()

'''
# plotting 2d
fig, axs = plt.subplots(2,3)

axs[0,0].plot(ts, ap1.xps)
axs[0,0].set_xlabel('time (s)')
axs[0,0].set_ylabel('X position (m)')
axs[0,0].set_title('X postion and time')
axs[0,0].legend(['Particle 1', 'Particle 2'])

axs[1,0].plot(ts, ap1.yps)
axs[1,0].set_xlabel('time (s)')
axs[1,0].set_ylabel('Y position (m)')
axs[1,0].set_title('Y postion and time')
axs[1,0].legend(['Particle 1', 'Particle 2'])

axs[0,1].plot(ts, ap1.xvs)
axs[0,1].set_xlabel('time (s)')
axs[0,1].set_ylabel('X velocity (m/s)')
axs[0,1].set_title('X velocity and time')
axs[0,1].legend(['Particle 1', 'Particle 2'])

axs[1,1].plot(ts, ap1.yvs)
axs[1,1].set_xlabel('time (s)')
axs[1,1].set_ylabel('Y velocity (m/s)')
axs[1,1].set_title('Y velocity and time')
axs[1,1].legend(['Particle 1', 'Particle 2'])

axs[0,2].plot(ts, ap1.xas)
axs[0,2].set_xlabel('time (s)')
axs[0,2].set_ylabel('X acceleration (m//$s^2$)')
axs[0,2].set_title('X acceleration and time')
axs[0,2].legend(['Particle 1', 'Particle 2'])

axs[1,2].plot(ts, ap1.yas)
axs[1,2].set_xlabel('time (s)')
axs[1,2].set_ylabel('Y acceleration (m//$s^2$)')
axs[1,2].set_title('Y acceleration and time')
axs[1,2].legend(['Particle 1', 'Particle 2'])

fig.tight_layout()
plt.show()
'''