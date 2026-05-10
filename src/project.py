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

def ik_arm():
    sel = cmds.ls(sl=True)
    shoulder = sel[0]
    elbow = sel[1]
    wrist = sel[2]

    arm_con = cmds.circle(name=wrist.replace('JNT', 'CON'))
    arm_grp = cmds.group(arm_con[0], name=wrist.replace('JNT', 'GRP'))
    pv_con = cmds.circle(name=wrist.replace('JNT', 'PV_CON'))
    pv_grp = cmds.group(pv_con[0], name=wrist.replace('JNT', 'PV_GRP'))
    cmds.matchTransform(arm_grp, wrist)
    shoulder_pos = cmds.xform(shoulder, q=True, ws=True, t=True)
    elbow_pos = cmds.xform(elbow, q=True, ws=True, t=True)
    wrist_pos = cmds.xform(wrist, q=True, ws=True, t=True)
    crv = cmds.curve(d=1, p=[shoulder_pos, elbow_pos, wrist_pos])
    cmds.moveVertexAlongDirection(crv + '.cv[1]', n=8)
    pv_pos = cmds.xform(crv + '.cv[1]', q=1, ws=1, t=1)
    cmds.xform(pv_grp, ws=1, t=pv_pos)
    cmds.delete(crv)
    ikh = cmds.ikHandle(startJoint=shoulder, endEffector=wrist, name=wrist.replace('JNT', 'IKH'))
    cmds.parent(ikh[0], arm_con)
    cmds.poleVectorConstraint(pv_con, ikh[0])
    cmds.orientConstraint(arm_con, wrist, maintainOffset=True)

def main():
    fk_arm()

