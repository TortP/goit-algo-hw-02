import queue
import random
import time

# Створюємо чергу для заявок
requests_queue = queue.Queue()

def generate_request():
    # Генеруємо випадковий номер заявки
    request_id = random.randint(1000, 9999)
    # Додаємо заявку до черги
    requests_queue.put(f"Заявка №{request_id}")
    print(f"Створено заявку №{request_id}")

def process_request():
    if not requests_queue.empty():
        # Отримуємо заявку з черги
        request = requests_queue.get()
        print(f"Обробляється {request}")
        # Імітуємо процес обробки
        time.sleep(2)  # Затримка на 2 секунди
        print(f"{request} успішно оброблена")
    else:
        print("Черга порожня, немає заявок для обробки.")

def main():
    while True:
        # Генеруємо нову заявку
        generate_request()
        # Намагаємося обробити заявку
        process_request()

        # Перевіряємо, чи хоче користувач вийти з програми
        user_input = input("Продовжити роботу? (так/ні): ").strip().lower()
        if user_input == 'ні':
            print("Роботу завершено.")
            break

# Запуск програми
main()
