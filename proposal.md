# Title
IkFk Arm Rig
## Repository
https://github.com/Julian-Pruneda/IkFk-Arm-Rig.git

## Description
Will take a 3 joint chain that is named Shoulder, Elbow, and Wrist and create an rig with an Ik and an Fk switch. This will make creating arm rigs easier in the future.

## Features
- Ik Arm
	Will take the join chain and create an Ik handle from the shoulder to the wrist. Will also create a control and a new attribute to switch between Ik and Fk
- Fk arm
	Will create 3 controls for each joint that will control each of them with forward kinematics. Will only work when Fk mode is toggled
- Ik Pivot
	Will create a curve at each joint and move the normal of the elbow and create a control for the pivot of the Ik handle. 

## Challenges
- Using Maya commands in python
- Importing code into Maya
- Fully understanding how an IkFk arm should work

## Outcomes
Ideal Outcome:
- Upon running the program, a 3 joint arm will be fully rigged with an Ik Fk toggle.

Minimal Viable Outcome:
- Can create an Ik arm or and Fk arm, but not adding a toggle for each

## Milestones

- Week 1
  1. Goal 1: Make code for Ik arm rig
  2. Goal 2: Make code for placing Ik control

- Week 2
  1. Goal 1: Make code to create Fk arm rig
  2. Goal 2: Make code to create Ik pivot control

- Week N (Final)
  1. Goal 1: Make code that will add toggle between Ik and Fk
  2. Goal 2: Put all pieces together to make final product
