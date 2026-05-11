# IkFk Auto Rig Script
## [Demonstration Video](https://youtu.be/lTkQY_oNt4U)
## [Github Page](https://github.com/Julian-Pruneda/IkFk-Arm-Rig)

This is my IkFk Auto Rig Script, which is meant to take a 3 long joint chained which is named shoulder_JNT, elbow_JNT, and wrist_JNT and rig it with fk and ik controls with a toggle between the two.
After selecting the joint chain from shoulder -> elbow -> wrist, running my program will do a couple things. To start, it will create 3 copies of the original chain, a bind chain, fk chain, and ik chain. 
Then it will rig the fk chain complete with controls, followed by the ik chain, with a single wrist control and a pole vector control as well. Next, it will create an ikfk switch on the ik wrist control to
switch between ik and fk mode. For this control, I think it would be nice to have implemented hiding the fk controls when in ik mode to give more context to the rig. 