
import  model, view

def start():
    view.greetings()
    while True:
        
        view.menu() 
        activ = input("Выберите действие от 1 до 6,где 1. вывести все контакты: 2. поиск контактов: 3. добавить контакт: 4. изменить контакт: 5. удалить: 6. выход: ")
        print()

        activ = input('Действие: ') 
        if activ == '1':
           view.display_contacts(data) #все контакты
        elif activ == '2':
            data = input('Введите ФИО: ')
            model.search_contacts(data) #поиск контактов
        elif activ== '3':
            data = input('Введите ФИО: ')
            view.add_contact(data) #добавить контакт
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

    
       

