import random

def get_numbers_ticket(min_numb, max_numb, quantity):
    list_numbers = set()
    if min_numb <1 or max_numb > 1000 or min_numb>max_numb or (max_numb-min_numb) < quantity:
        print(f"You numbers are wrong")
        return[]
        
    else:
        while quantity != len(list_numbers):
            list_numbers.add(random.randint(min_numb, max_numb))
            numbers = sorted(list_numbers)
        return numbers
   

lottery_numbers = get_numbers_ticket(10,15,5)        
print("Ваші лотерейні числа:", lottery_numbers)