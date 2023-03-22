import string


def caesar_cipher(plaintext, shift):
    alphabet = string.ascii_uppercase
    ciphertext = ""
    for char in plaintext:
        if char in alphabet:
            index = (alphabet.index(char) + shift) % 26
            ciphertext += alphabet[index]
        else:
            ciphertext += char
    return ciphertext


def vigenere_cipher(plaintext, key):
    alphabet = string.ascii_uppercase
    key = key.upper()
    key_len = len(key)
    key_pos = 0
    ciphertext = ""
    for char in plaintext:
        if char in alphabet:
            shift = alphabet.index(key[key_pos]) % 26
            index = (alphabet.index(char) + shift) % 26
            ciphertext += alphabet[index]
            key_pos = (key_pos + 1) % key_len
        else:
            ciphertext += char
    return ciphertext


def playfair_cipher(plaintext, key):
    alphabet = string.ascii_uppercase.replace("J", "")
    key = key.upper().replace("J", "I")
    key_len = len(key)
    key_pos = 0
    grid = ""
    for char in key + alphabet:
        if char not in grid:
            grid += char
    grid_len = len(grid)
    if grid_len < 25:
        for char in alphabet:
            if char not in grid:
                grid += char
    ciphertext = ""
    plaintext = plaintext.upper().replace("J", "I")
    plaintext_len = len(plaintext)
    plaintext_pos = 0
    while plaintext_pos < plaintext_len:
        char1 = plaintext[plaintext_pos]
        if char1 not in alphabet:
            plaintext_pos += 1
            continue
        char2 = plaintext[plaintext_pos + 1] if plaintext_pos + 1 < plaintext_len else "X"
        if char2 not in alphabet:
            plaintext_pos += 2
            continue
        if char1 == char2:
            char2 = "X"
            plaintext_pos -= 1
        row1, col1 = divmod(grid.index(char1), 5)
        row2, col2 = divmod(grid.index(char2), 5)
        if row1 == row2:
            ciphertext += grid[row1 * 5 + (col1 + 1) % 5]
            ciphertext += grid[row2 * 5 + (col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += grid[((row1 + 1) % 5) * 5 + col1]
            ciphertext += grid[((row2 + 1) % 5) * 5 + col2]
        else:
            ciphertext += grid[row1 * 5 + col2]
            ciphertext += grid[row2 * 5 + col1]
        plaintext_pos += 2
    return ciphertext


# Example usage:
plaintext = "HELLO WORLD"
shift = 3
key = "CRYPTO"
playfair_key = "KEYWORD"

caesar_ciphertext = caesar_cipher(plaintext, shift)
vigenere_ciphertext = vigenere_cipher(plaintext, key)
playfair_ciphertext = playfair_cipher(plaintext, playfair_key)

print("Caesar ciphertext:", caesar_ciphertext)
print("vigenere ciphertext:", vigenere_ciphertext)
print("playfair ciphertext:", playfair_ciphertext)
