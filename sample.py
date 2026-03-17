import time as t
import sys
from datetime import datetime

def get_valid_time():
    while True:
        user_input = input("Set alarm (HH:MM:SS): ")

        try:
            alarm_time = datetime.strptime(user_input, "%H:%M:%S").time()
            return alarm_time

        except ValueError:
            print("❌ Invalid format. Use HH:MM:SS (24-hour)")

def alarm(alarm_time):
    print("⏳ Alarm set...")

    while True:
        now = datetime.now().time()

        # trigger when current time passes alarm time
        if now >= alarm_time:
            print("\n⏰ WAKE UP 🔥🔥🔥")
            for _ in range(3):
                print("\a", end="", flush=True)
                t.sleep(0.5)
            break

        # show live clock
        sys.stdout.write(f"\rCurrent Time: {now.strftime('%H:%M:%S')}")
        sys.stdout.flush()

        t.sleep(1)


def timer(seconds):
    while seconds >= 0:
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        s = seconds % 60

        sys.stdout.write(f"\r{hours:02}:{minutes:02}:{s:02}")
        sys.stdout.flush()

        t.sleep(1)
        seconds -= 1

    print("\n⏰ Timer ended!")


alarm_time = get_valid_time()
seconds = int(input("Set timer in seconds: "))

alarm(alarm_time)
timer(seconds)