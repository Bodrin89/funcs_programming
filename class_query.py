

class Query:

    @classmethod
    def filter(cls, value, file):
        """Фильтрация по значению"""
        return filter(lambda x: value in x, file)

    @classmethod
    def map(cls, value, data):
        """Вывод данных по номеру колонки"""
        return map(lambda x: x.split(' ')[int(value)], data)

    @classmethod
    def unique(cls, value, data):
        return set(data)

    @classmethod
    def sort(cls, value, data):
        """Сортировка"""
        reversed = value == 'asc'
        return sorted(data, reverse=reversed)

    @classmethod
    def limit(cls, value, data):
        """Лимит выводимых строк"""
        return data[:int(value)]

