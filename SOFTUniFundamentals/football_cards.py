card = input()
team_A = 11
team_B = 11
booked_players = card.split()
booked_players_A = []
booked_players_B = []
terminated = False

for i in range(len(booked_players)):
    if "A" in booked_players[i]:
        if booked_players[i][2:] not in booked_players_A:
            booked_players_A.append(booked_players[i][2:])
            team_A -= 1
    elif "B" in booked_players[i]:
        if booked_players[i][2:] not in booked_players_B:
            booked_players_B.append(booked_players[i][2:])
            team_B -= 1
    if team_A < 7 or team_B < 7:
        terminated = True
        break

print(f"Team A - {team_A}; Team B - {team_B}")
if terminated:
    print("Game was terminated")
