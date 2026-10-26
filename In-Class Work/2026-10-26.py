def has_duplicate_letters(word):
    result = False
    for i in range(0, len(word) - 1):
        for j in range(i+1, len(word)):
            if word[i] == word[j]:
                result = True
    return result


has_duplicate_letters(['e', 'e'])
