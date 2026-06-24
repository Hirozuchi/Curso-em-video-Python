word_tpl = ('Papel','Programa', 'Coca', 'Paralelepipedo', 'Vigia','Ima', 'Duelo', 'Viagem')
vowels = ['a', 'i', 'u', 'e', 'o', ]
for word in word_tpl:
    vowel_word = []
    for vowel_in_word in vowels:
        if vowel_in_word in word.lower():
            vowel_word.append(vowel_in_word)
    if vowel_word:
        print(f'A Palavra {word}, tem as vogais: {vowel_word}')