# TASK 5: Hexapod Inverse Kinematics Solution

## Problem Overview

In this task, I implemented an inverse kinematics solution for a 3-DOF hexapod leg. The goal is to calculate the joint angles (alpha,beta ,gamma ) for the coxa, femur, and tibia based on a given 3D target foot position (x, y, z). The angles are calculated using the inverse kinematics algorithm, and the results are returned in degrees, rounded to two decimal places.

### Solution Explanation

1. **Coxa (alpha)**: The coxa angle is computed by calculating the yaw (horizontal rotation) of the leg based on the target x and y coordinates. The formula used is:

    alpha =atan2(y, x)

2. **Femur (beta)**: The femur angle is determined by solving a 2D triangle formed by the femur and tibia. The equation involves trigonometric relationships considering the vertical displacement (z) and horizontal displacement (R):

   beta = (atan2(z, R)) - (atan2(L_3 * sin(gamma), L_2 + L_3cos(gamma)))

4. **Tibia (gamma)**: The tibia angle is found using the law of cosines applied to the 2D triangle formed by the femur and tibia:

    gamma= acos({R^2 + z^2 - L_2^2 - L_3^2}/{2*L_2*L_3})

    The value is constrained to avoid floating-point errors using "max(min(D, 1), -1)".

5. **Reachability Check**: The algorithm first checks if the target is reachable by comparing the distance from the base (R) and the vertical reach (z) to the sum of the leg lengths. If the target exceeds the leg's maximum reach, it is considered unreachable.

### Function Definitions

- inverse_kinematics(x, y, z): Computes the joint angles alpha, beta, and gamma based on the target position (x, y, z).
- test_inverse_kinematics(): Runs five test cases, prints the target position, computed angles, and reachability status.

### Test Cases

1. **Test 1**: A typical point within the reachable workspace.
2. **Test 2**: A point close to the base.
3. **Test 3**: A point near the maximum reach of the leg.
4. **Test 4**: An unreachable point (distance exceeds the total leg reach).
5. **Test 5**: A point requiring a large negative z (foot positioned significantly below the coxa plane).

## Conclusion

The inverse kinematics solution computes the required joint angles based on the target position. The function correctly handles reachable and unreachable cases, and the angles are returned in degrees with proper error handling.

## Files Submitted

- hexapod_ik_solution.py: Python code for inverse kinematics solution.
- Task_5.md: Markdown file explaining the solution.
- Inverse_kinematics_derivation.jpeg - an image containing my final calculations and derivations
