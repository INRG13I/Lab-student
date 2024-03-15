def test_add_book():
    test_book_repository = Repository('test_save_file')
    test_book_service = BookService(test_book_repository)
    test_book_service.add_entity(test_book_service.create_book(0, 'Hello', 'World', '!'))
    test_book_repository.file_delete()
    assert len(test_book_service.get_all_entities()) == 1


def test_delete_book():
    test_book_repository = Repository('test_save_file')
    test_book_service = BookService(test_book_repository)
    test_book_service.add_entity(test_book_service.create_book(0, 'Hello', 'World', '!'))
    test_book_service.delete_entity(0)
    test_book_repository.file_delete()
    assert len(test_book_service.get_all_entities()) == 0


def test_get_book_by_id():
    test_book_repository = Repository('test_save_file')
    test_book_service = BookService(test_book_repository)
    test_book_service.add_entity(test_book_service.create_book(0, 'Hello', 'World', '!'))
    test_book_repository.file_delete()
    assert test_book_service.get_entity_by_id(1) is None


def test_update_book():  # todo: find out how to get value out of object to assert it
    test_book_repository = Repository('test_save_file')
    test_book_service = BookService(test_book_repository)
    test_book_service.add_entity(test_book_service.create_book(0, 'Hello', 'World', '!'))
    test_book_service.update_entity(test_book_service.create_book(0, 'Hi', 'Its me', 'A random guy'))
    test_book_repository.file_delete()
