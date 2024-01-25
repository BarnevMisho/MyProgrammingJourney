single_string_of_integers = input()
count_of_beggars = int(input())
turns_list = single_string_of_integers.split(", ")
turns_list_integer = []
for i in turns_list:
    turns_list_integer.append(int(i))
all_turns = []
start_index = 0
while start_index < count_of_beggars:
    sum_for_each_beggar = 0
    for i in range(start_index,len(turns_list_integer),count_of_beggars):
        sum_for_each_beggar += turns_list_integer[i]

    all_turns.append(sum_for_each_beggar)
    start_index += 1
    
print(all_turns)