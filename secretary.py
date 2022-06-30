documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }


def find_person(doc_no: str, docs=documents):
    for log in docs:
        if log["number"] == doc_no:
            return log.get("name")
    return 'Такого документа нет'


def find_shelf(doc, shelves=directories):
    for key, value in shelves.items():
        if doc in value:
            return key
    return 'Такого документа нет'


def make_list():
    Mylist = []
    for log in documents:
        newline = log["type"], log["number"], log["name"]
        Mylist.append(newline)
    return Mylist


def add_doc(type, number, name, shelf):
    new_log = {"type": type, "number": number, "name": name}
    documents.append(new_log)
    directories[shelf].append(new_log['number'])
    return new_log


def del_doc(doc):
    for log in documents:
        if log['number'] == doc:
            documents.remove(log)
    for value in directories.values():
        if doc in value:
            for item in value:
                if item == doc:
                    value.remove(item)
            return True
    return False


def add_shelf(shelf):
    new_key = {shelf: []}
    if shelf not in directories.keys():
        directories.update(new_key)
        print('Успешно добавлена новая полка')
        return True
    print('Такая полка уже существует')
    return False


def move_doc(doc, shelf):
    for value in directories.values():
        if doc in value:
            if shelf in directories.keys():
                for value in directories.values():
                    for item in value:
                        if doc == item:
                            value.remove(item)
                            directories[shelf].append(doc)
                            return directories[shelf]
            return False
    return False
