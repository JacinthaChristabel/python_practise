angle_1,angle_2,angle_3 = map(int, input("Enter 3 angles with space between them: ").split())

if (angle_1+angle_2+angle_3)==180 and angle_1>0 and angle_2>0 and angle_3 >0:
    print("Valid Triangle")
else:
    print("Not Valid Triangle")