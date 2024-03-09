usernames = input().split(", ")
valid_usernames = []

for username in usernames:
    cleaned_username = " ".join(username.strip().split())
    if not(17 > len(username) >= 3) or username != cleaned_username:
        continue
    elif username.replace("_", "").replace("-", "").isalnum():
        valid_usernames.append(username)


for current_username in valid_usernames:
    print(current_username)