numbers = [int(num) for num in input().split(", ")]
max_number = max(numbers)
group_length = 0
if max_number % 10 == 0:
    group_length = (max_number // 10) * 10
else:
    group_length = (max_number // 10 + 1) * 10

while group_length > 0:
    low_boundary = group_length - 10
    filtred_numbers = [number for number in numbers if number in range(low_boundary, group_length + 1)]
    print(f"Group of {group_length}'s: {filtred_numbers}")
    group_length -= 10