import time

def countdown(minutes, label):
    seconds = minutes * 60
    print(f"\n{label} started for {minutes} minutes")

    while seconds > 0:
        mins = seconds // 60
        secs = seconds % 60
        print(f"{mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        seconds -= 1

    print(f"\n{label} finished!")

def pomodoro():
    study = 25
    short_break = 5

    while True:
        countdown(study, "Study")
        countdown(short_break, "Break")

        cont = input("Continue? (y/n): ")
        if cont.lower() != "y":
            break

def main():
    while True:
        print("\n1. Normal timer")
        print("2. Pomodoro mode")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            minutes = int(input("Minutes: "))
            countdown(minutes, "Timer")
        elif choice == "2":
            pomodoro()
        elif choice == "0":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
