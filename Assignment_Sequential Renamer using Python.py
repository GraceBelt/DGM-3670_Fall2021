import maya.cmds as cmds

def createJnts (a, b):
    for i in range (a, b):
        newJnt = cmds. joint()
createJnts(0, 10)

cmds.rename ('joint1', 'Leg_0001_Jnt')
cmds.rename ('joint2', 'Leg_0002_Jnt')
cmds.rename ('joint3', 'Leg_0003_Jnt')
cmds.rename ('joint4', 'Leg_0004_Jnt')
cmds.rename ('joint5', 'Leg_0005_Jnt')
cmds.rename ('joint6', 'Leg_0006_Jnt')
cmds.rename ('joint7', 'Leg_0007_Jnt')
cmds.rename ('joint8', 'Leg_0008_Jnt')
cmds.rename ('joint9', 'Leg_0009_Jnt')
cmds.rename ('joint10', 'Leg_0010_Jnt')  