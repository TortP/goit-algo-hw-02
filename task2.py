from collections import deque

def is_palindrome(input_string):
    # 1. Приводимо рядок до нижнього регістру і видаляємо пробіли
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())
    
    # 2. Створюємо двосторонню чергу і додаємо всі символи
    char_deque = deque(cleaned_string)
    
    # 3. Порівнюємо символи з обох кінців
    while len(char_deque) > 1:
        # Витягуємо символи з початку і кінця черги
        front = char_deque.popleft()
        back = char_deque.pop()
        
        # Якщо символи не однакові, рядок не є паліндромом
        if front != back:
            return False
    
    # Якщо всі символи однакові, то це паліндром
    return True

# Тестуємо функцію
test_string = input("Введіть рядок для перевірки: ")
if is_palindrome(test_string):
    print(f"Рядок '{test_string}' є паліндромом.")
else:
    print(f"Рядок '{test_string}' не є паліндромом.")
