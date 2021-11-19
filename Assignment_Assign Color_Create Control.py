import maya.cmds as cmds

def createControls (num1, num2):
    a = num1
    b = num2
    
    for i in range(a, b):
        newControl = cmds.CreateNURBSCircle()
              
createControls(0, 3)

def newGroups (num1, num2):
    a = num1
    b = num2
    c = 'nurbsCircle1'
    d = 'nurbsCircle2'
    e = 'nurbsCircle3'
    f = 'Elbow_Ctrl_Grp'
    h = 'Wrist_Ctrl_Grp'
     
    for i in range(a, b):
        G1 = cmds.group(c, n='Shoulder_Ctrl_Grp')
        G2 = cmds.group(d, n='Elbow_Ctrl_Grp')
        G3 = cmds.group(e, n='Wrist_Ctrl_Grp')
        Re1 = cmds.rename(c, 'Shoulder_Ctrl')
        Re2 = cmds.rename(d, 'Elbow_Ctrl')
        Re3 = cmds.rename(e, 'Wrist_Ctrl')
        Pa1 = cmds.parent (f, 'Shoulder_Ctrl')
        Pa2 = cmds.parent(h, 'Elbow_Ctrl')
           
newGroups (0, 1)

def Colors (red, blue, yellow):
    newGroups()
    x = red
    y = blue
    z = yellow

    for i in range(x, y, z):
        

Colors(0, 1, 2) 