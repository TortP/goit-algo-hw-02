import queue
import random

# Створюємо чергу для нових заявок і чергу для заявок "в роботі"
new_requests = queue.Queue()
in_progress_requests = queue.Queue()

def generate_new_requests():
    """Генерує нову заявку і додає її до черги нових заявок."""
    request_id = random.randint(1000, 9999)
    new_requests.put(f"Заявка №{request_id}")
    print(f"Створено нову заявку №{request_id}")

def process_new_request():
    """Обробляє нову заявку."""
    if not new_requests.empty():
        # Отримуємо першу заявку з черги нових заявок
        request = new_requests.get()
        print(f"Отримана {request}.")
        
        # Запитуємо у користувача, чи вирішена проблема
        user_input = input(f"Ви хочете закрити {request}? (так/ні): ").strip().lower()
        
        if user_input == 'так':
            print(f"{request} успішно закрита.")
        else:
            # Переміщаємо заявку в чергу "в роботі"
            in_progress_requests.put(request)
            print(f"{request} переміщено до черги 'в роботі'.")
    else:
        print("Немає нових заявок для обробки.")

def process_in_progress_requests():
    """Перевіряє всі заявки з черги 'в роботі', чи є нові дані, і пропонує обробити їх."""
    if not in_progress_requests.empty():
        for _ in range(in_progress_requests.qsize()):
            # Отримуємо першу заявку з черги "в роботі"
            request = in_progress_requests.get()
            print(f"Перевіряємо заявку {request}, що знаходиться в роботі.")
            
            # Імітуємо отримання нових даних (50% шанс отримати нові дані)
            new_data_received = random.choice([True, False])

            if new_data_received:
                print(f"Отримані нові дані по заявці {request}.")
                
                # Запитуємо у користувача, чи вирішена проблема
                user_input = input(f"Ви хочете закрити заявку {request}? (так/ні): ").strip().lower()
                
                if user_input == 'так':
                    print(f"{request} успішно закрита.")
                else:
                    # Заявка залишається в черзі "в роботі"
                    in_progress_requests.put(request)
                    print(f"{request} залишається в черзі 'в роботі'.")
            else:
                # Немає нових даних, заявка повертається до черги "в роботі"
                in_progress_requests.put(request)
                print(f"Немає нових даних по заявці {request}. Заявка залишається в черзі 'в роботі'.")
    else:
        print("Немає заявок у черзі 'в роботі'.")

def main():
    """Основний цикл програми."""
    while True:
        # Генеруємо нові заявки
        generate_new_requests()

        # Обробляємо нову заявку
        process_new_request()

        # Автоматично перевіряємо всі заявки з черги "в роботі"
        if not in_progress_requests.empty():
            print("Перевіряємо всі заявки з черги 'в роботі'...")
            process_in_progress_requests()

        # Запитуємо у користувача, чи хоче він продовжити роботу
        user_input = input("Продовжити роботу? (так/ні): ").strip().lower()
        if user_input == 'ні':
            print("Роботу завершено.")
            break

# Запуск програми
main()
