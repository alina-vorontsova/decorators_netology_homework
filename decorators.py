import datetime

# декоратор-логгер
def decorator(some_function):

    def new_function(*args, **kwargs):
        result = some_function(*args, **kwargs)
        with open('logs.txt', 'a', encoding='utf-8') as file:
            file.write(f'Дата, время: {datetime.datetime.now()} - Функция: {some_function} - Аргументы: {args} и {kwargs} - Возвращаемое значение: {result}' + '\n')
        
        return result 
    
    return new_function

# декоратор-логгер с параметром – путь к логам      
def parameterized_decorator(path_to_file):
    
    def decorator(some_function):

        def new_function(*args, **kwargs):
            result = some_function(*args, **kwargs)
            with open(path_to_file, 'a', encoding='utf-8') as file:
                file.write(f'Дата, время: {datetime.datetime.now()} - Имя функции: {some_function} - Аргументы: {args} и {kwargs} - Возвращаемое значение: {result}' + '\n')
            return result 
        
        return new_function
    
    return decorator