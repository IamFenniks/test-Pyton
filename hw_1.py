# Part I
date = str(input('Введите дату: '))
task = str(input('Добавьте задачу: '))
bs   = ' '

output = date + bs + task
print(output)
print('Part I is over')
print('')

# -------------------------------
# Part II & III
new_array = {}
i = 1
while i <= 3:
    date_ = str(input('Введите дату: '))
    task_ = str(input('Добавьте задачу: '))

    new_array[date_] = task_
    i += 1

for j in new_array:
    print(j + bs + new_array[j])

print('\nPart II is over to...\n')
