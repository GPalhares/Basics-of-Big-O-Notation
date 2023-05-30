def multiply_array(numbers):
    result = 1
    for number in numbers:
        result *= number
    print(result)
    return result

meu_array = [1, 2, 3, 4, 5]

multiply_array(meu_array)

# Complexidade 0(n) ou Complexidade linear, pois a cada elemento novo no array,
# a complexidade aumenta Linearmente, no exemplo tera 5 iterações