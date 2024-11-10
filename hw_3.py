def count_letter (list, l):
    result = 0
    for word in list:
        for letter in word:
            if letter == l:
                result += 1
    return result

list = ['python', 'c++', 'c', 'scala', 'java']

r = count_letter(list, 'c')
print(r)