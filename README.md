# Lab Manual 3: ROS 2 Workspace Setup, Package Creation, and GitHub Introduction

## Objective
1. Set up a ROS 2 workspace.
2. Learn how to use GitHub for version control.
3. Learn how to create a new ROS 2 package.
4. Write and edit a basic node to move the turtle in a specific pattern.

---

## Part 1 & 2: Local Scripts and GitHub Version Control (Week 3 Folder)

For this lab, we are working directly in the `Week3` folder.

### Step 1: Initialize a Git Repository
```bash
cd /home/ahsan/Desktop/Week3
git init
```

### Step 2: Configure Git
```bash
git config --global user.name "A-hsanAbdullah"
git config --global user.email "2022mc61@student.uet.edu.pk"
```

### Step 3: Connect Local Repository to GitHub and Push Changes
```bash
git remote add origin https://github.com/A-hsanAbdullah/Week_3_ROS.git
git branch -M main

# Add, commit, and push all changes
git add .
git commit -m "Final commit for lab session"
git push -u origin main
```

---

## Part 3: Running the Part 5 Task Scripts

Three separate scripts have been created to fulfill the Part 5 tasks. To run them, make sure you have sourced your ROS 2 environment:
```bash
source /opt/ros/humble/setup.bash
```

Start the turtlesim node in one terminal:
```bash
ros2 run turtlesim turtlesim_node
```

In a **second terminal**, you can run any of the task scripts directly from the Week3 folder:

### Task 1: Circular and Triangular Patterns
This script moves `turtle1` in a circular pattern for a few seconds, then switches to a triangular pattern.
```bash
./task1_patterns.py
```

### Task 2: Spawn Three Turtles and Move Them
This script spawns `turtle2` and `turtle3`, and publishes different velocity commands to all three turtles simultaneously.
```bash
./task2_spawn_turtles.py
```

### Task 3: Move Turtle to a Specific Location
This script uses a proportional controller to drive the turtle to a specific coordinate `(8.0, 8.0)` by subscribing to its `pose`.
```bash
./task3_go_to_goal.py
```
