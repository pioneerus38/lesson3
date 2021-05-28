try:
    with open('referat.txt', 'r', encoding='utf-8') as test_file:
        text = test_file.read()
        print(f'Длина строки, символов: {len(text)}')
except FileNotFoundError:
    print("Файл referat.txt не найден!")

try:
    with open('referat.txt', 'r', encoding='utf-8') as test_file:
        words_sum = 0
        for line in test_file:
            words_sum += len(line.split())
        print(f'Количество слов: {words_sum}')
except FileNotFoundError:
    print("Файл referat.txt не найден!")
    
try:
    with open('referat.txt', 'r', encoding='utf-8') as input_file:
        with open('referat2.txt', 'w', encoding='utf-8') as output_file:
            for line in input_file:
                result_line = line.replace(".", "!")
                print(result_line.replace("\n", ""))
                output_file.write(result_line) 
            print("Файл referat2.txt cохранен.")                     
except FileNotFoundError:
    print("Файл referat.txt не найден!")
