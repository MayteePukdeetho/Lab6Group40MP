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

def decode(encoded_password):
	decoded_password = ""
	split_enc_pass = list(encoded_password)
	for char in range(len(split_enc_pass)):
		split_enc_pass[char] = int(split_enc_pass[char])
		split_enc_pass[char] -= 3 #decoding my subtracting 3
		if split_enc_pass[char] < 0: #making sure it doesnt produce a negative number
			split_enc_pass[char] += 10
		split_enc_pass[char] = str(split_enc_pass[char])
		decoded_password += split_enc_pass[char]

	return decoded_password

if __name__ == '__main__':
    while True:
        print('''Menu
-------------
1. Encode
2. Decode
3. Quit''')
        menu_select = int(input("Choose an option: "))
        if menu_select == 3:
            break
        elif menu_select == 1:
            password = (input("Please enter your password to encode: "))
            current_password = encode(password)
            encoded_password = current_password
            print('Your password has been encoded and stored!')
        elif menu_select == 2:
            current_password = decode(current_password)

            print(f'The encoded password is {encoded_password}, and the original password is {current_password}.')

        else:
            pass
