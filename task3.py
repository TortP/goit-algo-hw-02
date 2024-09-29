def check_brackets(string):
    # Стек для зберігання відкритих дужок
    stack = []
    
    # Відповідність відкритих та закритих дужок
    matching_brackets = {')': '(', '}': '{', ']': '['}
    
    # Перевіряємо кожен символ у рядку
    for char in string:
        # Якщо це відкрита дужка, додаємо її в стек
        if char in '({[':
            stack.append(char)
        
        # Якщо це закрита дужка, перевіряємо відповідність
        elif char in ')}]':
            if stack and stack[-1] == matching_brackets[char]:
                stack.pop()  # Видаляємо відповідну відкриту дужку
            else:
                return "Несиметрично"  # Невідповідні дужки

    # Якщо стек порожній, всі дужки мають пари
    if not stack:
        return "Симетрично"
    else:
        return "Несиметрично"  # Є незакриті дужки

# Запитуємо рядок у користувача через input()
input_string = input("Введіть рядок з дужками для перевірки: ")

# Перевіряємо рядок і виводимо результат
result = check_brackets(input_string)
print(f"Результат: {result}")
