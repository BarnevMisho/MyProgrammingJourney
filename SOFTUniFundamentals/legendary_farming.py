materials = [word.lower() for word in input().split()]
legendary_dict = {"shards": 0, "fragments": 0, "motes": 0}
junk_dict = {}
legendary_item = ""

for index in range(0, len(materials), 2):
    material = materials[index + 1]
    quantity = int(materials[index])
    if material in legendary_dict.keys():
        legendary_dict[material] += quantity
    else:
        if material not in junk_dict.keys():
            junk_dict[material] = 0
        junk_dict[material] += quantity

    if legendary_item == "":
        if legendary_dict["shards"] >= 250:
            legendary_item = "Shadowmourne"
            legendary_dict["shards"] -= 250
        elif legendary_dict["fragments"] >= 250:
            legendary_item = "Valanyr"
            legendary_dict["fragments"] -= 250
        elif legendary_dict["motes"] >= 250:
            legendary_item = "Dragonwrath"
            legendary_dict["motes"] -= 250


print(f"{legendary_item} obtained!")
for key, value in legendary_dict.items():
    print(f"{key}: {value}")
for key, value in junk_dict.items():
    print(f"{key}: {value}")



