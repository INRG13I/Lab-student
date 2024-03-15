class DuplicateIdError(Exception):
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return f'\u001b[31mDuplicate error: {self.__message}'