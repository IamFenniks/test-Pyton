HELP = """
    help - напечатать справку по программе;
    add  - добавить задачу в список (запрашиваем у пользователя);
    show - показать все добавленные задачи;
    exit - выйти из программы.
"""
tasks = []
run = True
today = []
tomorrow = []
other = []

while run:
    command = str(input('Введите команду: '))
    
    if command == 'help':
        print(HELP)
    elif command == 'show':
        print(tasks)

    elif command == 'add':
        taskDay = str(input('Введите день выполнения задачи: '))
        task = str(input('Введите название задачи: '))
        if taskDay == 'Сегодня':
            today.append(task)
        elif taskDay == 'Завтра':
            tomorrow.append(task)
        else:
            other.append(task)
        tasks.append(task)
        print('Задача добавлена.', tasks)

    elif command == 'exit':
        print('Спасибо за использование! До свидания!')
        break
    else:
        print('Неизвестная задача..')
        # run = False
        break
print('Чао!\n')
    