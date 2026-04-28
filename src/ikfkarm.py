from maya import cmds
from maya import OpenMaya

# make fk arm
def fk_arm():
    sel = cmds.ls(selection=True)
    controls = []
    groups = []

    for jnt in sel:
        con =  cmds.circle(name=jnt.replace('JNT', 'CON'), normal=[1,0,0])
        grp = cmds.group(con, name=jnt.replace('JNT', 'GRP'))
        cmds.matchTransform(grp, jnt)
        cmds.parentConstraint(con, jnt, maintainOffset = True)
        controls.append(con)
        groups.append(grp)

    for i in range(1, len(groups)):
        cmds.parent(groups[i], controls[i-1])



def main():
    fk_arm()

