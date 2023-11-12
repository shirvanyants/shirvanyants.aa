def count_letters(text_):
    letter_ = {}
    for char in text_:
        if char.isalpha():
            char_lower = char.lower()
            letter_[char_lower] = letter_.get(char_lower, 0) + 1
    return letter_# TODO  Напишите функцию count_letters


def calculate_frequency(letter_):
    total_letters = sum(letter_.values())
    frequency_dict = {}
    for letter, count in letter_.items():
        frequency = count / total_letters
        frequency_dict[letter] = round(frequency, 2)
    return frequency_dict# TODO Напишите функцию calculate_frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

letter_ = count_letters(main_str)
frequency_dict = calculate_frequency(letter_)

for letter, frequency in frequency_dict.items():
    print(f"{letter}: {frequency:.2f}")
