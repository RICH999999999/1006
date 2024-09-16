calls = 0
#Функция для подсчета вызовов
def count_calls():
    global calls
    calls += 1
#Функция string_info
def string_info(s):
    count_calls()
    return (len(s), s.upper(),s.lower())
#Функция is_contains
def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    list_to_search = [x.lower() for x in list_to_search]
    return string in list_to_search
#Пример выполнения программы
print(string_info("Capybara"))
print(string_info("Armageddon"))
print(is_contains("Urban", ["ban", "BaNaN", "urBAN"]))
print(is_contains("cycle", ["recycling", "cyclic"]))
print(calls)