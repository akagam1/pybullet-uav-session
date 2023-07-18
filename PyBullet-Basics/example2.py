import numpy as np
import pybullet as p
import time
import pybullet_data

DURATION = 10000
ALPHA = 0.01

physicsClient = p.connect(p.GUI)  # or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath())  # optionally
print("data path: %s " % pybullet_data.getDataPath())
p.setGravity(0, 0, -10)
planeId = p.loadURDF("plane.urdf")
cubeStartPos = [0, 0, 0.3]
cubeStartOrientation = p.getQuaternionFromEuler([0, 0, 0])
boxId = p.loadURDF("sphere_small.urdf", cubeStartPos, cubeStartOrientation, globalScaling=10)
gemId = p.loadURDF("r2d2.urdf", [
                   2, 2, 0.6],  p.getQuaternionFromEuler([0, 0, 0]))
for i in range(DURATION):
    p.stepSimulation()
    time.sleep(1./240.)
    gemPos, gemOrn = p.getBasePositionAndOrientation(gemId)
    boxPos, boxOrn = p.getBasePositionAndOrientation(boxId)

    force = ALPHA * (np.array(gemPos) - np.array(boxPos))
    p.applyExternalForce(objectUniqueId=boxId, linkIndex=-1,
                         forceObj=force, posObj=boxPos, flags=p.WORLD_FRAME)


p.disconnect()
