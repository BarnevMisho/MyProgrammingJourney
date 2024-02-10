events = input().split("|")
initial_energy = 100
initial_coins = 100
events_full_list = []
day_completed = True

for i in events:
    events_full_list.append(i.split("-"))

for j in range(len(events_full_list)):
    gained_energy = 0

    if events_full_list[j][0] == "rest":
        if initial_energy + int(events_full_list[j][1]) <= 100:
            gained_energy = int(events_full_list[j][1])
            initial_energy += gained_energy
        else:
            gained_energy = 100 - initial_energy
            initial_energy = 100
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {initial_energy}.")

    elif events_full_list[j][0] == "order":
        if initial_energy >= 30:
            earned_coins = int(events_full_list[j][1])
            initial_coins += earned_coins
            initial_energy -= 30
            print(f"You earned {earned_coins} coins.")
        else:
            if initial_energy < 50:
                initial_energy += 50
            else:
                initial_energy = 100
            print("You had to rest!")

    else:
        if initial_coins >= int(events_full_list[j][1]):
            initial_coins -= int(events_full_list[j][1])
            print(f"You bought {events_full_list[j][0]}.")
        else:
            print(f"Closed! Cannot afford {events_full_list[j][0]}.")
            day_completed = False
            break

if day_completed:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")