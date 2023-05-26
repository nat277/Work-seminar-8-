
def read_file_to_dict(phonebook):                                                         # перевод файла в словарь
    with open(phonebook.txt, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    headers = ['Фамилия', 'Имя', 'Номер телефона']
    contact_list = []
    for line in lines:
        line = line.strip().split()
        contact_list.append(dict(zip(headers, line)))
    return contact_list


def read_file_to_list(phonebook):                                                          # перевод файла в список
    with open(phonebook.txt, 'r', encoding='utf-8') as file:
        contact_list = []
        for line in file.readlines():
            contact_list.append(line.split())
    return contact_list

def print_contacts(contact_list: list):                                                   # вывод на экран
    for contact in contact_list:
        for key, value in contact.items():
            print(f'{key}: {value:12}', end='')
        print()

def show_contacts(phonebook):                                                             # показать контакты
    list_of_contacts = sorted(read_file_to_dict(file_name), key=lambda x: x['Фамилия'])
    print_contacts(list_of_contacts)
    print()
    return list_of_contacts

def search_parameters():                                                                # выбор параметра поиска
    print('По какому полю выполнить поиск?')
    search_field = input('1 - по фамилии\n2 - по имени\n3 - по номеру телефона\n')
    print()
    search_value = None
    if search_field == '1':
        search_value = input('Введите фамилию для поиска: ')
        print()
    elif search_field == '2':
        search_value = input('Введите имя для поиска: ')
        print()
    elif search_field == '3':
        search_value = input('Введите номер для поиска: ')
        print()
    return search_field, search_value

def search_contacts(contact_list):                                                      # поиск контакта
    search_field, search_value = search_parameters()
    search_value_dict = {'1': 'Фамилия', '2': 'Имя', '3': 'Номер телефона'}
    found_contacts = []
    for contact in contact_list:
        if contact[search_value_dict[search_field]] == search_value:
            found_contacts.append(contact)
    if len(found_contacts) == 0:
        print('Контакт не найден!')
    else:
        print_contacts(found_contacts)
    print()

def get_new_number():                                                                   # создание контакта
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = input('Введите номер телефона: ')
    return last_name, first_name, phone_number

def add_contacts(phonebook):                                                                 # добавление контакта
    data = ' '.join(get_new_number())
    with open(phonebook.txt, 'a', encoding='utf-8') as file:
        file.write(f'{data}\n')

def search_for_change(contact_list: list):                                               # поиск для изменения или удаления
    search_field, search_value = search_parameters()
    search_result = []
    for contact in contact_list:
        if contact[int(search_field) - 1] == search_value:
            search_result.append(contact)
    if len(search_result) == 1:
        return search_result[0]
    elif len(search_result) > 1:
        print('Найдено несколько контактов')
        for i in range(len(search_result)):
            print(f'{i + 1} - {search_result[i]}')
        num_count = int(input('Выберите номер контакта, который нужно изменить/удалить: '))
        return search_result[num_count - 1]
    else:
        print('Контакт не найден')
    print()

def change_contacts(phonebook):                                                         # Изменение контакта
    contact_list = read_file_to_list(phonebook)
    number_to_change = search_for_change(contact_list)
    contact_list.remove(number_to_change)
    print('Какое поле вы хотите изменить?')
    field = input('1 - Фамилия\n2 - Имя\n3 - Номер телефона\n')
    if field == '1':
        number_to_change[0] = input('Введите фамилию: ')
    elif field == '2':
        number_to_change[1] = input('Введите имя: ')
    elif field == '3':
        number_to_change[2] = input('Введите номер телефона: ')
    contact_list.append(number_to_change)
    with open(phonebook.txt, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)

def del_contacts(phonebook):                                                            # Удаление контакта
    contact_list = read_file_to_list(phonebook)
    number_to_change = search_for_change(contact_list)
    contact_list.remove(number_to_change)
    with open(phonebook.txt, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)

