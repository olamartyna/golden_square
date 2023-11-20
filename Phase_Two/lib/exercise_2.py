def encode(text, key):
    #print(f": {}")
    #print("encode function")
    cipher = make_cipher(key)
    #print(f"    * cipher: {cipher}")
    # cipher = ['a', 's', 'e', 'c', 'r', 't', 'k', 'y', 'd', 'f', 'g', 'h', 'i', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'u', 'v', 'w', 'x', 'z', '{']
    
    ciphertext_chars = []
    #print(f"    * ciphertext_chars: {ciphertext_chars}")
    for i in text:
        ciphered_char = chr(65 + cipher.index(i))
        #print(f"    * for letter {i} in text - ciphered_char: {ciphered_char}")
        ciphertext_chars.append(ciphered_char)

    return "".join(ciphertext_chars)


def decode(encrypted, key):
    cipher = make_cipher(key)
    print(f"    * cipher: {cipher}")
    plaintext_chars = []
    for i in encrypted:
        plain_char = cipher[ord(i) - 65]
        print(f"Encrytd letter {i}")
        print(f"plain_char {plain_char}")
        plaintext_chars.append(plain_char)

    return "".join(plaintext_chars)


def make_cipher(key):
    #print("** make_cipher function")
    #print(f"    ** key: {key}")
    alphabet = [chr(i + 96) for i in range(1, 28)]
    #print(f"    ** alphabet: {alphabet}")
    #print(f"    ** len of alphabet: {len(alphabet)}")
    cipher_with_duplicates = list(key) + alphabet
    #print(f"    ** cipher_with_duplicates: {cipher_with_duplicates}")
    cipher = []
    #print(f"    ** cipher: {cipher}")

    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])
    #print(f"    ** cipher: {cipher}")
    return cipher

# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
print(f"""
 Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
  Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
""")

print(f"""
 Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
Expected: theswiftfoxjumpedoverthelazydog
  Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
""")
