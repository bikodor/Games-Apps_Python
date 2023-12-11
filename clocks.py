import time

hours =0
minutes = 0
seconds = 0


while True:
    time.sleep(1)
    seconds += 1
    if seconds == 60:
        seconds = 0
        minutes += 1

    if minutes == 60:
        minutes = 0
        hours += 1

    if hours == 25:
        hours = 1



    print(f"{hours}: {minutes}: {seconds}")