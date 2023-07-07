import math
# Final velocity = 18kmph / 5metre/s
#acceleration = 3.5kmph/s / 1m/s^2
#intersection dist = 50m

def lane_wise(v):
    v=int(v/2)
    d=v*5 + 50
    t1=5/1   #t=v/a
    d1=0.5*1*t1*t1   #d=0.5at^2
    d2=d-d1
    t2=d2/5
    if t1+t2>30:
        return 30
    else:
        return int(t1+t2)

#v1 - vehicles in lane 1
def timer_lanes(v1,v2,v3,v4,x):
    if x==1:
        t1=lane_wise(v1)
        t2=t1+2
        t3=lane_wise(v2)+t2
        t4=lane_wise(v3)+t3
        print(f"\n1st Signal - Green : {t1} seconds")
        print(f"2nd Signal - Red   : {t2} seconds")
        print(f"3rd Signal - Red   : {t3} seconds")
        print(f"4th Signal - Red   : {t4} seconds")
    
    elif x==2:
        t2=lane_wise(v2)
        t3=t2+2
        t4=lane_wise(v3)+t3
        t1=lane_wise(v4)+t4
        print(f"1st Signal - Red   : {t1} seconds")
        print(f"2nd Signal - Green : {t2} seconds")
        print(f"3rd Signal - Red   : {t3} seconds")
        print(f"4th Signal - Red   : {t4} seconds")
    
    elif x==3:
        t3=lane_wise(v3)
        t4=t3+2
        t1=lane_wise(t4)+t4
        t2=lane_wise(v1)+t1
        print(f"1st Signal - Red   : {t1} seconds")
        print(f"2nd Signal - Red   : {t2} seconds")
        print(f"3rd Signal - Green : {t3} seconds")
        print(f"4th Signal - Red   : {t4} seconds")
    
    elif x==4:
        t4=lane_wise(v4)
        t1=t4+2
        t2=lane_wise(v1)+t1
        t3=lane_wise(v2)+t2
        print(f"1st Signal - Red   : {t1} seconds")
        print(f"2nd Signal - Red   : {t2} seconds")
        print(f"3rd Signal - Red   : {t3} seconds")
        print(f"4th Signal - Green : {t4} seconds")

# timer_lanes(36,15,8,2,1)