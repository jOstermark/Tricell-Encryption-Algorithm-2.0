import random

def print_menu(user_message:str):
    print("------------------------------------")
    print("Tricell Encryption Terminal")
    print(f'Your message is "{user_message}"')
    print("1. Add new message")
    print("2. Add set of key values")
    print("3. Encrypt")
    print("4. Decrypt")
    print("5. Exit")
    print()

def get_choice(promt:str) -> str:
    choice = input(f"{promt}")
    return choice

def encryption_algorithms(key:int, letter:str, decrypt:bool) -> str:
    ASCII_value = ord(letter)
    if decrypt == False:
        encrypted_letter = ((((ASCII_value - 32) + key) % 95) + 32)
        return chr(encrypted_letter)
    else: 
        decrypt_letter = ((((ASCII_value - 32) - key) % 95) + 32)
        return chr(decrypt_letter)

def encrypt_or_decrypt_message(user_message:str, key_values:list, decrypt:bool = False) -> str:
    encrypted_message = ""
    index = 0
    if decrypt == True:
        user_message = un_salt(user_message)
    for letters in user_message:
        encrypted_message += encryption_algorithms(key_values[index], letters, decrypt)
        index = (index + 1) % len(key_values)
    if decrypt == False:
      encrypted_message = salt(encrypted_message)
    return encrypted_message

def salt(encrypted_message:str) -> str:

    first_block_length = random.randint(5,20) -4
    split_location = random.randint(1, len(encrypted_message)-1)
    user_message_1 = encrypted_message[:split_location]
    user_message_2 = encrypted_message[split_location:]
    middle_block_length = random.randint(5,20)
    middel_start = first_block_length + 4 + len(user_message_1)
    middel_end = middel_start + middle_block_length
    last_block_length = random.randint(5,20)
    saltet_message = chr(first_block_length+36) + chr(middel_start+32) +chr(middel_end+32)+chr(last_block_length+32) + generate_random_string(first_block_length) + user_message_1 + generate_random_string(middle_block_length) + user_message_2 + generate_random_string(last_block_length)
    return saltet_message

def un_salt(encrypted_message:str) -> str:

    first_block_length = ord(encrypted_message[0]) -32
    middel_start = ord(encrypted_message[1]) -32
    middel_end = ord(encrypted_message[2]) -32
    last_block_length = ord(encrypted_message[3]) -32
    message_part_1 = encrypted_message[first_block_length:middel_start]
    message_part_2 = encrypted_message[middel_end:-last_block_length]
    un_salt = message_part_1 + message_part_2
    return un_salt

def generate_random_string(lenght:int) -> str:
    random_string = ""
    for i in range(0,lenght):
        random_string = random_string + chr(random.randint(32, 126))
    return random_string

def main():
    



if __name__ == "__main__":
    main()
