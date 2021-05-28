# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = set('аеёиоуыэюя') #{'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э','ю', 'я'}
print(sum(letter in vowels for letter in word.lower()))


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split():
    print(word[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
words_len = [len(word) for word in sentence.split()]
print(sum(words_len)/len(words_len))