# Author: Reganto
# Blog: reganto.net


from random import choice
from operator import add, mul, sub


def captcha():
    try_count = 0
    while True:
        numbers = [number for number in range(1, 5)]
        operators_functions = [add, mul, sub]
        operators_functions_litrals_map = {add: "+", mul: "*", sub: "-"}
        
        
        first_num = choice(numbers)
        second_num = choice(numbers)
        operator = choice(operators_functions)
        
        question = f"Solve Question: {first_num}{operators_functions_litrals_map.get(operator)}{second_num} = "
                   
        answer = int(input(question))        
        expected_answer = operator(first_num, second_num)
        
        if answer != expected_answer:
            try_count += 1
            print(f"try again, incorrent attempts: {try_count}")
        elif answer == expected_answer:
            return "pass"
        if try_count == 3:
            return "failed"

