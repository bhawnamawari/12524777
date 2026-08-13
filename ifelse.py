speed_sound=343.2
speed=float(input("enter current speed of uour aircraft"))
mach=speed/speed_sound
if mach >1.0:
    print("The aircraft is flying at supersonic speed.")
else:
    print("The aircraft is flying at subsonic speed.")
