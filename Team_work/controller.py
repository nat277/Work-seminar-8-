import  model, view

def start():
    view.greetings()
    while True:

        view.menu() 
        activ = input("Выберите действие от 1 до 6: ")
        print()

      
        if activ == '1':
           view.display_contacts(data) #все контакты
        elif activ == '2':
            data = input('Введите ФИО: ')
            model.search_contacts(data) #поиск контактов
        elif activ== '3':
            data = input('Введите ФИО: ')
            model.add_contact(data) #добавить контакт
        elif activ == '4': 
            data = input('какой контакт хотите изменить ?: ')
            model.change_contacts(data) # изменить контакт
        elif activ == '5': 
            data = input('Кого хотите удалить?: ')
            model.del_contacts(data) # удалить контакт
        elif activ ==  '6':   #выход
            pass
            break
        else:
            print("неправильный выбор.")

        if __name__ == "__main__":
            start()


