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
    pass
