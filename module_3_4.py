def single_root_words(root_word, *non_root_words):
    any_words = []
    root_word_lower = root_word.lower()
    for i in non_root_words:
        non_root_words_lower = i.lower()
        if root_word_lower in non_root_words_lower or non_root_words_lower in root_word_lower:
            any_words.append(i)

    return any_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)