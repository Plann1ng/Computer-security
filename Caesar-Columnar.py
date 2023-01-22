import os
import math

# Read the file


def reader(string):
    with open(string, mode="r", encoding="utf-8") as file:
        file = file.read().split()
        return file

# Encryption Caeser cipher
# Did not managed to use "   '  " since it get's mixed with the string


def enc_ceasar(key, plain):
    # reading the file inside the function
    text = reader(plain)
    # Alphabet to take the shifted index and some other additional characters
    alpha = 'abcdefghjiklmnopqrstuvwxyz,.:*-()" '
    output = ''
    for word in text:
        for letter in word:
            # Check the index of the current letter
            letter = letter.lower()
            index = alpha.find(letter)
            # Use the key for the cipher index
            cypherpos = (index+key) % 34
            # Append to empty string
            output += alpha[cypherpos]
        output += " "
    return output

# Decryption Caeser cipher
# Did not managed to use "   '  " since it get's mixed with the string


def dec_ceasar(key, plain):
    # reading the file inside the function
    text = reader(plain)
    # Alphabet to take the shifted index and some other additional characters
    alpha = 'abcdefghjiklmnopqrstuvwxyz,.:*-()" '
    output = ''
    for word in text:
        for letter in word:
            # Check the index of the current letter
            letter = letter.lower()
            index = alpha.find(letter)
            # Reverse the method
            position = (index - key) % 34
            # Append to empty string
            output += alpha[position]
        output += " "
    return output

# Save manipulated text to the file


def saver(output, save):
    # Please before opening give file name in your current working directory
    # or change your directory to the file's directory
    text_file = open(f'{save}.txt', "w")
    new = ''
    counter = 0
    output = output.split()
    for word in output:
        counter += len(word)
        new += word
        new += " "
        # Used counter in order to avoid saving the whole
        # text to one line in the .txt file
        if counter >= 99:
            new += '\n'
            counter = 0
    output_main = text_file.writelines(new)
    return

# NOTE Transposition


# Encryption

# Matrix builder
def enc_matrix(width, message):
    r = 0
    c = 0
    # 2D matrix
    matrix = [[]]

    for position, character in enumerate(message):
        # Adding each character
        matrix[r].append(character)
        # keeping track of character count
        c += 1
        # For case when index is out of range
        if c >= width:
            c = 0
            r += 1
        matrix.append([])

    return matrix

# Encryption main
def encrypt(message, key):
    # Building up the matrix
    matrix = enc_matrix(len(key), message)
    # getting ordered key
    keywordSequence = key_sequence(key)

    ciphertext = ""
    # Getting position of the key
    for num in range(len(keywordSequence)):
        position = keywordSequence.index(num+1)
        # Adding adding the letters back to the one word
        for row in range(len(matrix)):
            if len(matrix[row]) > position:
                # Row stands for the list inside
                # the list and position stands for the index
                ciphertext += matrix[row][position]
    return ciphertext

# Deccryption


# Key order
def key_sequence(key):
    sequence = []
    # iterate over the position and characters
    for position, character in enumerate(key):
        # Getting previous position time letters
        previousLetters = key[:position]
        newNumber = 1
        # iterating over the previous characters and
        # indexes as the variable names show
        for previousindex, prev_char in enumerate(previousLetters):
            # if previous index was bigger than the current index taking
            # previous index to the current index place and iterate again
            if prev_char > character:
                sequence[previousindex] += 1
            # append ordered
            else:
                newNumber += 1
        sequence.append(newNumber)
    return sequence


# Another matrix which takes lenght of key as row lenght and
# len(message)/ len(key) for collumn
def empty(width, height, length):
    matrix = []
    totalAdded = 0
    # 2D matrix
    for r in range(math.ceil(height)):
        matrix.append([])
        for c in range(width):
            if totalAdded >= length:
                return matrix
            matrix[r].append('')
            totalAdded += 1
    return matrix
