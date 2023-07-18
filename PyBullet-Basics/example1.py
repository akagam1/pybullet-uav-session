import pybullet as p
import time
import pybullet_data
from math import pi

physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
startPos = [0,0,1]
startOrientation = p.getQuaternionFromEuler([0,0,0])
boxId = p.loadURDF("r2d2.urdf",startPos, startOrientation)
#newModel = p.loadURDF("sphere_small.urdf",[0,2,0.6],startOrientation, globalScaling=20)
#set the center of mass frame (loadURDF sets base link frame) startPos/Ornp.resetBasePositionAndOrientation(boxId, startPos, startOrientation)
curr_time = 0
freq = 1/240

for i in range (10000):
    curr_time = i*freq
    #p.resetBasePositionAndOrientation(newModel,[0,2-1*curr_time,0.1],startOrientation)
    p.stepSimulation()
    time.sleep(1./240.)
cubePos, cubeOrn = p.getBasePositionAndOrientation(boxId)
print(cubePos,cubeOrn)
p.disconnect()

