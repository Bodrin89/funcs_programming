

class Query:

    @staticmethod
    def filter(value, file):
        """Фильтрация по значению"""
        return filter(lambda x: value in x, file)

    @staticmethod
    def map(value, data):
        """Вывод данных по номеру колонки"""
        return map(lambda x: x.split(' ')[int(value)], data)

    @staticmethod
    def unique(value, data):
        return set(data)

    @staticmethod
    def sort(value, data):
        """Сортировка"""
        reversed = value == 'asc'
        return sorted(data, reverse=reversed)

    @staticmethod
    def limit(value, data):
        """Лимит выводимых строк"""
        return data[:int(value)]

