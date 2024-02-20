from collections import deque

def is_palindrome(s):
    # Перетворення рядка до нижнього регістру та видалення всіх небуквених символів
    s = ''.join(filter(str.isalnum, s)).lower()

    # Створення двосторонньої черги з символів рядка
    char_deque = deque(s)
    
    while len(char_deque) > 1:

        # Порівняння і видалення символів з обох кінців
        if char_deque.popleft() != char_deque.pop():
            return False
        
    return True


test_strings = ["Racecar", "радар", "No lemon, no melon", "фішка", "Hello", "A man, a plan, a canal, Panama", "око"]

# Перевірка кожного рядка, чи є він паліндромом
palindrome_results = {s: is_palindrome(s) for s in test_strings}
print(palindrome_results)
