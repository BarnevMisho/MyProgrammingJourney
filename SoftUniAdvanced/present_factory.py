from collections import deque

materials = [int(x) for x in input().split()]
magic_values = deque([int(x) for x in input().split()])

present_table = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

presents = {}

while materials and magic_values:
    if materials[-1] * magic_values[0] in present_table:
        magic = magic_values.popleft()
        material = materials.pop()
        if present_table[magic * material] not in presents:
            presents[present_table[magic * material]] = 0
        presents[present_table[magic * material]] += 1
    elif materials[-1] * magic_values[0] < 0:
        magic = magic_values.popleft()
        material = materials.pop()
        materials.append(material + magic)
    elif materials[-1] * magic_values[0] > 0:
        magic_values.popleft()
        materials[-1] += 15
    elif materials[-1] == 0 and magic_values[0] == 0:
        magic_values.popleft()
        materials.pop()
    elif materials[-1] == 0:
        materials.pop()
    elif magic_values[0] == 0:
        magic_values.popleft()

succeeded = ("Doll" in presents and "Wooden train" in presents) or \
            ("Bicycle" in presents and "Teddy bear" in presents)
print("The presents are crafted! Merry Christmas!" if succeeded else "No presents this Christmas!")
if materials:
    output_materials = ", ".join([str(x) for x in materials[::-1]])
    print(f"Materials left: {output_materials}")
if magic_values:
    output_magic_values = ", ".join([str(x) for x in magic_values])
    print(f"Magic left: {output_magic_values}")
for key in sorted(presents):
    print(f"{key}: {presents[key]}")