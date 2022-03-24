def letter_count(text, letter):
    count = 0
    for x in letter:
        if x == text:
            count += 1
    return count


letter = input("Введите предложение: ")
text = input("Введите букву: ")

print(letter_count(text, letter))
