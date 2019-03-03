from logic.collision import rotate_around_point_highperf
from entities.projectile import Projectile
import math

class Gun(object):

    def __init__(self, entity, projectileSkin, size, hType, fireRate):
        self.entity = entity
        self.projectileSkin = projectileSkin
        self.hType = hType
        self.fireRate = fireRate
        self.fireCooldown = -1

    def tickCooldown(self):
        self.fireCooldown = (self.fireCooldown + 1) % self.fireRate
        return self.fireCooldown == 0


    def fireProjectile(self, velMag, damage):
        if(self.tickCooldown):
            topCenter = (self.entity.movement.x + self.entity.size[0] // 2, self.entity.movement.y - self.entity.size[1])
            topCenter = rotate_around_point_highperf(topCenter, self.entity.rotation, (self.entity.movement.x, self.entity.movement.y))
            rotationRad = math.radians(-1 * self.entity.rotation)
            vel = (math.cos(rotationRad) * velMag, math.sin(rotationRad) * velMag)
            projectile = Projectile(self.projectileSkin, self.size, self.hType, topCenter[0], topCenter[1], vel, 0, damage)
            return projectile
        else:
            return None


