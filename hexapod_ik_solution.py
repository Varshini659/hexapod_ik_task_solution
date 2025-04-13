import math
def inverse_kinematics(x,y,z):
    L1= 5.0
    L2= 10.0
    L3= 15.0
    # horizontal distance from coxa to end effector
    R = math.sqrt(x ** 2 + y ** 2)
    if z > (L1 + L2 + L3) or R > (L2 + L3):
        raise ValueError("Target is unreachable")
    else:
        # q1 (yaw)
        q1 = math.atan2(y,x)
        alpha = round(math.degrees(q1),2)
        #vertical diplacement from 1st joint
        Z = z-L1
        #q3: Tibia movement angle
        D = (R**2 + Z**2 - L2**2 - L3**2)/(2 * L2 * L3)
        #to avoid floating errors
        D= max(min(D,1),-1)
        q3=math.acos(D)
        #q2 : Femur movement angle
        try:
            theta1 = math.atan2(Z,R)
            theta2 = math.atan2(L3 * math.sin(q3), L2 + L3 * math.cos(q3))
            q2 = theta1 - theta2
        except ZeroDivisionError:
            raise ValueError("Division by zero in femur angle calculation")
        #converting all angles from radians to degrees
        beta = round(math.degrees(q2),2)
        gamma = round(math.degrees(q3),2)
        return alpha, beta, gamma

def test_inverse_kinematics():
    target_positions = [
        (10, 10, 5),    # Test 1: typical point
        (1, 1, 1),      # Test 2: close to base
        (20, 0, 5),     # Test 3: max reach
        (40, 40, 40),   # Test 4: unreachable
        (5, 5, -20),    # Test 5: deep below plane
    ]

    for i, pos in enumerate(target_positions):
        try:
            angles = inverse_kinematics(*pos)
            print(f"Test {i+1} - Position {pos}: Angles (α, β, γ) = {angles} (target reachable)")
        except Exception as e:
            print(f"Test {i+1} - Position {pos}: Error - {e}")
test_inverse_kinematics()

