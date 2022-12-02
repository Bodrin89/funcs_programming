

def open_file(file):
    """Функция открытия файла"""
    with open(file, 'r', encoding='utf-8') as f:
        return f.readlines()

