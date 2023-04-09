poem = input("Введите стихотворение, слова в фразе разделите дефисами, а фразы между собой - пробелами: ")
parts = poem.split()

total_vowel = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
lst = [sum(x in total_vowel for x in poem) for poem in parts]

res = "Парам пам-пам" if len(set(lst)) == 1 else "Пам парам"
print(res)