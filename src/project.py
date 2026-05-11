from maya import cmds
from maya import OpenMaya

# make fk arm
def fk_arm():
    sel = cmds.ls(selection=True)

    controls = []
    groups = []
    for jnt in sel:
        con =  cmds.circle(name=jnt.replace('JNT', 'CON'), normal=[1,0,0])[0]
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

    arm_con = cmds.circle(name=wrist.replace('JNT', 'IK_CON'), normal=[1,0,0])[0]
    arm_grp = cmds.group(arm_con, name=wrist.replace('JNT', 'IK_GRP'))
    pv_con = cmds.circle(name=wrist.replace('JNT', 'PV_CON'), normal=[1,0,0])[0]
    pv_grp = cmds.group(pv_con, name=wrist.replace('JNT', 'PV_GRP'))
    cmds.matchTransform(arm_grp, wrist)
    shoulder_pos = cmds.xform(shoulder, q=True, ws=True, t=True)
    elbow_pos = cmds.xform(elbow, q=True, ws=True, t=True)
    wrist_pos = cmds.xform(wrist, q=True, ws=True, t=True)
    crv = cmds.curve(d=1, p=[shoulder_pos, elbow_pos, wrist_pos])
    cmds.moveVertexAlongDirection(crv + '.cv[1]', n=8)
    pv_pos = cmds.xform(crv + '.cv[1]', q=1, ws=1, t=1)
    cmds.xform(pv_grp, ws=1, t=pv_pos)
    cmds.delete(crv)
    ikh = cmds.ikHandle(startJoint=shoulder, endEffector=wrist, name=wrist.replace('JNT', 'IKH'))[0]
    cmds.parent(ikh, arm_con)
    cmds.poleVectorConstraint(pv_con, ikh)
    cmds.orientConstraint(arm_con, wrist, maintainOffset=True)

def duplicate_chain(root_joint, joint_type):
    duplicated = cmds.duplicate(root_joint, renameChildren=True)
    chain = cmds.listRelatives(duplicated[0], ad=True, type ='joint')
    chain.append(duplicated[0])
    chain.reverse()

    new_chain = []
    names = ['shoulder', 'elbow', 'wrist']
    for i, jnt in enumerate(chain):
        new_name = joint_type + '_' + names[i] + '_JNT'
        renamed = cmds.rename(jnt, new_name)
        new_chain.append(renamed)
    
    return new_chain

    

    

def main():
    sel = cmds.ls(sl=True)
    shoulder = sel[0]
    elbow = sel[1]
    wrist = sel[2]

    fk_arm(duplicate_chain('FK'))
    
    ik_arm(duplicate_chain('IK'))
