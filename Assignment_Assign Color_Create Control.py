import maya.cmds as cmds

def Color():
    sels = cmds.ls(selection=True)
    
    for sel in sels:
        Col = cmds.color(sels, rgb=(1, 0, 0))
        cmds.curve(Col)

Color()

def Match():
    sels = cmds.ls(selection=True)
    
    for sel in sels:
        Cir = cmds.circle()
        cmds.parent(Cir, sel)
        Grp = cmds.group(empty=True)
        Grp = cmds.rename(Grp, sel + "_Grp")
        Grp = cmds.parent(sel, Grp)
        
        newPos = cmds.xform(sel, q=True, rp=True, ws=True) 
        newRot = cmds.xform(sel, q=True, ro=True, ws=True)
        cmds.xform(Grp, t=newPos, ws=True) 
        cmds.xform(Grp, ro=newRot, ws=True)
        cmds.xform(Cir, t=newPos, ws=True)
        cmds.xform(Cir, ro=newRot, ws=True) 
        
        cmds.rename(sel+"_Geo")
           
Match()