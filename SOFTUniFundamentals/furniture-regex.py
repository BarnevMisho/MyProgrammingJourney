import re

regex = r'>>(\w+)<<(\d+[\.0-9]*)!(\d+)'
mebel = input()
total_cost = 0
bought_furniture = []

while mebel != "Purchase":
    info = re.findall(regex, mebel)
    if info:
        bought_furniture.append(info[0][0])
        total_cost += float(info[0][1]) * int(info[0][2])
    mebel = input()

print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_cost :.2f}")

