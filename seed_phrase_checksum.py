# tool for checking a 12 word seed phrase (for crypto wallets)
# execute the script and enter your 12 words (even though the last word is incorrect)
# the tool will tell you the correct last words index

# PLS CREATE THE 12 WORD RANDOMLY
# PLS EXECUTE THIS SCRIPT ON A SAFE, AIR GAPPED MACHINE

import hashlib

def checksum12words(data):
    if len(data) != 12:
        print("ERROR: Need 12 words numbers as input")
        return

    def binstr(s, l=8):
        return bin(s)[2:].zfill(l)

    def tohex(bytes_list):
        return ''.join([hex(x)[2:].zfill(2) for x in bytes_list])

    # convert data to binary and create byte array
    bytes_list = [binstr(x - 1, 11) for x in data]  # convert 0 based index to binary
    bin_str = ''.join(bytes_list)
    byte_list = [int(bin_str[i:i+8], 2) for i in range(0, len(bin_str), 8)]  # split into 8 bit chunks and convert to int

    if len(byte_list) != 17:
        print("ERROR: Something is wrong, check your input")
        return

    byte_list.pop()  # remove 17th byte (wrong checksum byte)
    print("Entropy is:", tohex(byte_list))

    sha256 = hashlib.sha256(bytes(byte_list)).digest()
    if len(sha256) != 32:
        print("ERROR: Wrong SHA256")
        return

    # get checksum from the first byte of the hash
    cs = binstr(sha256[0]).zfill(8)[:4]
    bits = binstr(byte_list[15]) + cs

    if len(bits) != 12:
        print("ERROR: Wrong final word bits")
        return

    print("Your 12th word index is:", 1 + int(bits[1:], 2))


def get_user_input():
    user_input = input("Enter the 12 words as comma-separated numbers (e.g. 1, 2, 3, ..., 12): ")

    data = [int(x.strip()) for x in user_input.split(",") if x.strip().isdigit()]
    if len(data) != 12:
        print("ERROR: You must enter exactly 12 words.")
    else:
        checksum12words(data)

get_user_input()

