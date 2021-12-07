import maya.cmds as cmds

#2) Select Objects, then select this statement, then Ctrl + Enter
sels = cmds.ls(selection=True)

for sel in sels:
    print(sel+'.translate')
    position = cmds.getAttr(sel+'.translate')
    pos = sel+"_Ctrl"
    print(position)
    cmds.circle(c=position[0], n=pos)

#1) Select this statement, then Ctrl + Enter
def createObj (num1):
    a = num1
    
    for i in range(a):
        cmds.polyCube()
     
createObj(3)

#3) Select whole, then select this statement, then Ctrl + Enter
sels = cmds.ls(selection=True)
a = ['pCube1', 'pCube2', 'pCube3']
b = ['Shoulder_Geo', 'Elbow_Geo', 'Wrist_Geo']
c = ['pCube1_Ctrl', 'pCube2_Ctrl', 'pCube3_Ctrl']
d = ['Shoulder_Ctrl', 'Elbow_Ctrl', 'Wrist_Ctrl']
Group1 = ['Shoulder_Geo', 'Shoulder_Ctrl']
Group2 = ['Elbow_Geo', 'Elbow_Ctrl']
Group3 = ['Wrist_Geo', 'Wrist_Ctrl']

for sel in sels:
    cmds.rename(a[0], b[0])
    cmds.rename(a[1], b[1])
    cmds.rename(a[2], b[2])
    cmds.rename(c[0], d[0])
    cmds.rename(c[1], d[1])
    cmds.rename(c[2], d[2])
    cmds.group(Group1, n="Shoulder_Ctrl_Grp")
    cmds.group(Group2, n="Elbow_Ctrl_Grp")
    cmds.group(Group3, n="Wrist_Ctrl_Grp")
    cmds.parent('Shoulder_Ctrl', 'Shoulder_Geo')
    cmds.parent('Elbow_Ctrl', 'Elbow_Geo')
    cmds.parent('Wrist_Ctrl', 'Wrist_Geo')
    cmds.move(0, 0, -1.527, 'Shoulder_Geo', absolute=True) 
    cmds.move(-2.493, 0, 0.459, 'Elbow_Geo', absolute=True) 
    cmds.move(0, 0, 2.483, 'Wrist_Geo', absolute=True) 