from exceptions.exceptions import DuplicateIdError


class Repository:
    def __init__(self, path):
        self.__entities = {}
        self.__path = path

    def file_delete_entity(self, id_entity):
        """
        Deletes entity from file
        :param id_entity:
        :return:
        """
        poz = self.get_file_line_by_id(id_entity)
        with open(f'repository/save_files/{self.__path}', 'r') as file:
            file_list = file.readlines()
        with open(f'repository/save_files/{self.__path}', 'w') as file:
            for i, e in enumerate(file_list):
                if i != poz:
                    file.write(e)

    def file_output_entity(self, entity):
        '''
        Appends new entity in file
        :param entity: Object
        :return:
        '''
        with open(f'repository/save_files/{self.__path}', 'a') as file:
            entity = entity.file_format()
            file.write(entity)
            file.write("\n")

    def file_delete(self):
        '''
        Deletes contents of file
        :return:
        '''
        with open(f'repository/save_files/{self.__path}', 'w') as file:
            file.truncate(0)

    def file_input(self):
        '''
        Returns a list of lines from file
        :return:
        '''
        with open(f'repository/save_files/{self.__path}', 'r') as file:
            list = file.readlines()
            for e in range(len(list)):
                list[e] = list[e].strip()
        return list

    def file_add(self, entity):
        '''
        To be used in combination with file_input function
        Adds entity to repository
        :param entity:
        :return:
        '''
        if self.get_by_id(entity.get_id_entity()) is not None:
            raise DuplicateIdError("Exista deja o entitate cu id-ul dat !!!")
        self.__entities[entity.get_id_entity()] = entity

    def file_modify(self, entity):
        '''
        Modifies an entity in the file
        :param entity:
        :return:
        '''
        poz = self.get_file_line_by_id(entity.get_id_entity())
        backup = entity.file_format()
        with open(f'repository/save_files/{self.__path}', 'r') as file:
            list = file.readlines()
        with open(f'repository/save_files/{self.__path}', 'w') as file:
            for i, e in enumerate(list):
                if i != poz:
                    file.write(e)
                else:
                    file.write(backup)
                    file.write("\n")

    def get_file_line_by_id(self, id_entity):
        '''
        Returns the text file line where the entity is located
        :param id_entity:
        :return:
        '''
        with open(f'repository/save_files/{self.__path}', 'r') as file:
            list = file.readlines()
            for e in range(len(list)):
                elem = list[e].strip()
                elem = elem.split(" ")
                if int(elem[0]) == id_entity:
                    return e
        return None

    def get_all(self):
        '''
        returns a list of objects
        :return: list of Book class object
        '''
        return self.__entities.values()

    def get_by_id(self, id_entity):
        '''
        returns an object by id
        :param id_entity: int
        :return:
        '''
        if id_entity in self.__entities:
            return self.__entities[id_entity]
        return None

    def add(self, entity):
        '''
        adds object to repository
        :param entity: Book class object
        :return:
        '''
        if self.get_by_id(entity.get_id_entity()) is not None:
            raise DuplicateIdError("Exista deja o entitate cu id-ul dat !!!")
        self.__entities[entity.get_id_entity()] = entity
        self.file_output_entity(entity)

    def modify(self, new_entity):
        '''
        modifies object attributes with the given id
        :param new_entity:
        :return:
        '''
        if self.get_by_id(new_entity.get_id_entity()) is None:
            raise KeyError("Nu exista nici o entitate cu id-ul dat !!!")
        self.__entities[new_entity.get_id_entity()] = new_entity
        self.file_modify(new_entity)

    def delete(self, id_entity):
        '''
        deletes object with the given id
        :param id_entity:
        :return:
        '''
        if self.get_by_id(id_entity) is None:
            raise KeyError("Nu exista nici o entitate cu id-ul dat !!!")
        self.file_delete_entity(id_entity)
        self.__entities.pop(id_entity)