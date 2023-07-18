#encode created by Mayteetad Pukdeetho

def encode(password):
    encoded_password = ""
    split_password = list(password)
    for char in range(len(split_password)):
        split_password[char] = int(split_password[char])
        split_password[char] += 3 #encoding by adding 3
        if split_password[char] > 9: #making sure it doesn't produce '10, 11, or 12'
            split_password[char] -= 10
        split_password[char] = str(split_password[char])
        encoded_password += split_password[char]

    return encoded_password

if __name__ == '__main__':
    pass