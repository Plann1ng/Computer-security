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
