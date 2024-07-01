import random

def get_numbers_ticket(min_numb, max_numb, quantity):
    list_numbers = set()
    if min_numb <1 or max_numb > 1000 or quantity < min_numb or quantity > max_numb :
        return print(f"You numbers are wrong")
    
    else:
        while quantity != len(list_numbers):
            list_numbers.add(random.randint(min_numb, max_numb))
        return print("Ваші лотерейні числа:", sorted(list_numbers))              

print(get_numbers_ticket(1, 60, 6))