def task5_1(s):
    '''
    Дана строка символов. Определить количество букв «н», расположенных после первой запятой

    :param s: вводимая строка
    :return: None
    '''
    i = s.find(',')  # индекс первой запятой

    # Если запятая найдена, обрабатываем строку после нее
    if i != -1:
        s2 = s[i + 1:]
        count_n = s2.count('н')  # Считаем количество 'н'
    else:
        count_n = 0  # Если запятой нет, количество 'н' равно 0

    return count_n


def task5_2(text):
    '''
    Дан текст из слов, разделенных знаками препинания. Определить, какое из
    слов встречается в строке раньше: с максимальным количеством гласных или согласных букв.

    :param text: вводимый текст
    :return:
    '''

    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    consonants = "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"

    # Разделяем текст на слова и удаляем знаки препинания
    words = []
    for word in text.split():
        words.append(word.strip('.,!?;:'))


    max_v_word = ""         # слова с максимальным количеством гласных
    max_c_word = ""         # слова с максимальным количеством согласных
    max_v_count = 0         # Счетчик для максимального количества гласных
    max_c_count = 0         # Счетчик для максимального количества согласных

    # Проходим по каждому слову в списке
    for word in words:
        v_count = 0
        c_count = 0

        # Проходим по каждому символу в слове
        for char in word:
            if char in vowels:       # Если символ - гласная, увеличиваем счетчик гласных
                v_count += 1
            elif char in consonants: # Если символ - согласная, увеличиваем счетчик согласных
                c_count += 1

        # Если текущее количество гласных больше максимального, обновляем максимальное значение
        if v_count > max_v_count:
            max_v_count = v_count
            max_v_word = word

        # Если текущее количество согласных больше максимального, обновляем максимальное значение
        if c_count > max_c_count:
            max_c_count = c_count
            max_c_word = word

    if words.index(max_v_word) < words.index(max_c_word):
        print(f"Слово с максимальным количеством гласных: {max_v_word}")
    else:
        print(f"Слово с максимальным количеством согласных: {max_c_word}")


def task5_3(text, k, char):
    '''
    В каждом слове текста k-ю букву заменить заданным символом. Если k больше длины слова, корректировку не выполнять

    :param text: вводиымй текст
    :param k: номер буквы для замены
    :param char: на что заменить
    :return new_text: новый текст
    '''

    words = text.split()
    new_words = []

    for word in words:
        if k <= len(word):                                          # Проверяем, если номер буквы меньше или равен длине слова
            modified_word = word[:k - 1] + char + word[k:]          # Заменяем k-ю букву на заданный символ
            new_words.append(modified_word)                         # Добавляем измененное слово в список
        else:
            new_words.append(word)                                  # Добавляем оригинальное слово в список без изменений

    new_text = ' '.join(new_words)  # Объединяем измененные слова в одну строку
    return new_text


def task5_4(text):
    '''
    Рассортировать слова русского текста по возрастанию доли гласных букв
    (отношение количества гласных к общему количеству букв в слове).

    :param text: вводимый текст
    :return: None
    '''
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    words = text.split()

    # Создаем списки для хранения долей гласных и слов
    vowel_ratios = []
    sorted_words = []

    # Проходим по каждому слову
    for word in words:
        total_letters = len(word)
        vowel_count = 0

        # Проходим по каждой букве в слове
        for letter in word:
            if letter in vowels:  # Если буква гласная
                vowel_count += 1  # Увеличиваем счетчик гласных

        # Вычисляем долю гласных и добавляем в список
        if total_letters > 0:           # Проверяем, что слово не пустое
            ratio = vowel_count / total_letters
            vowel_ratios.append(ratio)
            sorted_words.append(word)

    # Сортируем слова по доле гласных
    for i in range(len(vowel_ratios)):
        for j in range(len(vowel_ratios) - 1):
            if vowel_ratios[j] > vowel_ratios[j + 1]:
                # Меняем местами доли
                vowel_ratios[j], vowel_ratios[j + 1] = vowel_ratios[j + 1], vowel_ratios[j]
                # Меняем местами слова
                sorted_words[j], sorted_words[j + 1] = sorted_words[j + 1], sorted_words[j]

    for word in sorted_words:
        print(word)


def task5_5(snils):
    '''
    Номер СНИЛС: Написать регулярное выражение, определяющее является ли
    данная строка номером СНИЛС в формате XXX-XXX-XXX XX.
    - Правильные примеры: 123-456-789 10, 987-654-321 11
    - Неправильные примеры: 123-456-789, 123-456-789-10, 12345678910, 123-456-789 101

    :param snils: вводимый снилс
    :return: None
    '''
    import re

    # Регулярное выражение для проверки формата СНИЛС
    pattern = r'^\d{3}-\d{3}-\d{3} \d{2}$'
    # Проверяем, соответствует ли введенный номер регулярному выражению
    if re.match(pattern, snils):
        print(f"{snils}: корректный номер СНИЛС")
    else:
        print(f"{snils}: некорректный номер СНИЛС")

def task5_6():
    '''
    Строки, содержащие двоичную запись числа, кратного 3. Пример строк,
    которые подходят: «0», «10010». Пример строк, которые не подходят:
    «00101», «Not a number», «1 1», «0 0»

    :param: None
    :return l:
    '''
    import re

    pattern = re.compile(r'^[01]+$')

    l = []

    while True:
        s = input("Введите строку (или 'exit' для выхода): ")
        if s.lower() == 'exit':
            break
        if pattern.match(s):
            decimal_value = int(s, 2)
            if decimal_value % 3 == 0:
                l.append(s)

    return l

def task5_7(s):
    '''
    Заменить все вхождения «**» в заданном математическом выражении на
    Python на символ «^»

    :param s: вводимая строка
    :return s2: переделанная строка
    '''
    import re

    s2 = re.sub(r'\*\*', '^', s)

    return s2





