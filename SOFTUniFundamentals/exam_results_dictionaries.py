results = {}
submissions = {}
command = input().split("-")
banned_students = []

while len(command) != 1:

    if len(command) == 3:
        username, language, points = command
        if username not in results.keys():
            results[username] = []
        results[username].append(int(points))
        if language not in submissions.keys():
            submissions[language] = 0
        submissions[language] += 1

    if len(command) == 2:
        username, status = command
        banned_students.append(username)

    command = input().split("-")

print("Results:")
for key, value in results.items():
    if key not in banned_students:
        print(f"{key} | {max(value)}")
print("Submissions:")
for key, value in submissions.items():
    print(f"{key} - {value}")