# Caesar Cypher

message = "Hello Programming 2"

encryption_key = 7

encoded_message = ""

for char in message:
    #print(char, ord(char))
    new_character = chr(ord(char) + encryption_key)
    encoded_message += new_character

print(encoded_message)
decoded_message = ""

for char in encoded_message:
    new_character = chr(ord(char) - encryption_key)
    decoded_message += new_character

print(decoded_message)

key = "O75848HFID732HFWIGY7JFB"

def encode(key, string):
    encoded_message = ""
    for i in range(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr(ord(string[i]) + ord(key_c))
        encoded_message += encoded_c
    return encoded_message


def decode(key, string):
    decoded_message = ""
    for i in range(len(string)):
        key_c = key[i % len(key)]
        decoded_c = str(ord(string[i]) - ord(key_c))
        decoded_message -= decoded_c
    return decoded_message

print(encode(key, "Hello Programming 2"))
