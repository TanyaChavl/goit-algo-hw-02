from queue import Queue
import random

class Client:
    def __init__(self, name):
        self.name = name
        self.questions = random.randint(1, 8)

class CallCenter:
    def __init__(self):
        self.clients = Queue()
        
    # Створення нової заявки
    def generate_request(self, client):
        self.clients.put(client)
    
    # Робота з заявками
    def process_request(self):
        if self.clients.empty():
            print("Черга пуста.")
        else:
            while not self.clients.empty():
                current_client = self.clients.get()
                print(f"Приймаю заявку від клієнта {current_client.name} яка включає {current_client.questions} кількість питань.")

# Створення екземпляру CallCenter
call_center = CallCenter()

# Генерація нових заявок і додавання їх до черги
for i in range(6):
    call_center.generate_request(Client(f"Client - #{i + 1}"))

# Обробка заявок
call_center.process_request()
