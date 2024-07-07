import random

def generate_random_list(n):
    return [random.randint(1,100) for _ in range(n)]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence

def find_maximum_value(arr):
    max_value = arr[0]
    for num in arr:
        if num > max_value:
            max_value = num
    return max_value

def calculate_average(arr):
    total = sum(arr)
    return total / len(arr)

def is_prime_number(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) +1):
        if num % i == 0:
            return False
    return True

def generate_random_string(length):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
    return ''.join(random.choice(letters) for _ in range(length))


def main():
    n = 23

    random_list = generate_random_list(n)
    print("Original List:", random_list)
    
    sorted_list = bubble_sort(random_list)
    print("Sorted List:", sorted_list)
    
    fib_list = fibonacci_sequence(n)
    print("Fib List:", fib_list)
    
    max_value = find_maximum_value(random_list)
    print("Max Value:", max_value)

    calc_average = calculate_average(random_list)
    print("Average Value:", calc_average)

    prime_num = is_prime_number(n)
    print("Is", n, "a Prime Number:", prime_num)

    rand_string = generate_random_string(n)
    print("Random String:", rand_string)


if __name__ == "__main__":
    main()