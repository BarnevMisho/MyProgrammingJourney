numbers = [int(num) for num in input().split(", ")]
group = 10
max_number = max(numbers)
group_length = 0
if max_number % 10 == 0:
    group_length = max_number // 10
else:
    group_length = max_number // 10 + 1

for _ in range(group_length):
    filtred_numbers = [number for number in numbers if number <= group]
    print(f"Group of {group}'s: {filtred_numbers}")
    group += 10
    numbers = [number for number in numbers if number not in filtred_numbers]