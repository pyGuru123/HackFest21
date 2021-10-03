LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(string, shift=1):
    '''
    Caesar Cypher shifts the letters by the given shift, for example, if key=1
    then, a becomes b, be becomes c, and c becomes d, etc
    '''
    assert 1<=shift<26
    words = string.split() #Splitting by spaces
    words_list = []
    for word in words:
        current_word = ''
        for letter in word:
            letter = letter.upper()
            index = LETTERS.index(letter)+shift
            current_word += LETTERS[index%26]
        words_list.append(current_word)
    return ' '.join(words_list)

def decrypt(string, shift):
    words = []
    for word in string.split():
        print(f'Current word: {word}')
        current_word = ''
        for letter in word:
            index = LETTERS.index(letter)
            current_word += LETTERS[index-shift]
        words.append(current_word)
    return ' '.join(words)


def main():
    choice = int(input("1) To Encrypt a String\n2) To Decrypt a string\nYour Choice: "))
    if choice == 1:
        string = input("Enter the string you want to encrypt: ")
        shift = int(input("Enter the value of shit: "))
        print(encrypt(string, shift))
    elif choice == 2:
        string = input("Enter the string you want to decrypt: ")
        shift = int(input("Enter the value of shit: "))
        print(decrypt(string, shift))
    else:
        print("Wrong Choice!")


if __name__ == "__main__":
    main()