pokemons = [int(pokemon) for pokemon in input().split()]
sum_removed_elements = 0
while pokemons != []:
    removed_value = 0
    index= int(input())
    if index < 0:
        pokemons[0], removed_value = pokemons[-1], pokemons[0]
    elif index >= len(pokemons):
        pokemons[-1], removed_value = pokemons[0], pokemons[-1]
    else:
        removed_value = pokemons.pop(index)
    pokemons = list(map(lambda x: x + removed_value if x <= removed_value else x - removed_value, pokemons))

    sum_removed_elements += removed_value

print(sum_removed_elements)
