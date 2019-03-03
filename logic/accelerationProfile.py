import math
import logic.collision

class BasicProfile(object):

    def __init__(self, yint, slope):
        self.yint = yint
        self.slope = slope
        self.limit = yint / slope

    def update(self, x, y, vel, acc, profileParam):
        direction = profileParam
        accNorm = logic.collision.normalize(acc)
        dirNorm = logic.collision.normal(direction)
        similar = logic.collision.cross(accNorm, dirNorm)[2]
        newAccMag = self.int - self.slope * (1 - similar) * self.limit
        newAcc = (dirNorm[0] * newAccMag, dirNorm[1] * newAccMag)
        return newAcc

class ZeroProfile(object):

    def __init__(self):
        pass

    def update(self, x, y, vel, acc, profileParams):
        return acc

class AccelerationProfile(object):

    def __init__(self, movementState, profile):
        self.movementState = movementState
        self.profile = profile

    def updateAcceleration(self, profileParams):
        [x, y, vel, acc] = [self.movementState.x, self.movementState.y, self.movementState.vel, self.movementState.acc]
        newAcc = self.profile.update(x, y, vel, acc, profileParams)
        self.movementState.setAcceleration(newAcc)