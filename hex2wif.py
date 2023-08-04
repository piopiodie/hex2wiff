import hashlib
import binascii
import base58

# The extracted string from the file
private_key_hex = "YOUR_HEX_STRING_HERE"

# The prefix for a mainnet WIF private key
prefix = "80"

# Adding the prefix to the private key
extended_key = prefix + private_key_hex

# Calculating the first checksum
first_checksum = hashlib.sha256(binascii.unhexlify(extended_key)).hexdigest()

# Calculating the second checksum
second_checksum = hashlib.sha256(binascii.unhexlify(first_checksum)).hexdigest()[:8]

# Adding the checksum to the extended key
wif_key = extended_key + second_checksum

# Converting the WIF key from hexadecimal to base58
wif_key_base58 = base58.b58encode(binascii.unhexlify(wif_key))

# Writing the WIF key to a file
with open("wif_key.txt", "w") as f:
    f.write(wif_key_base58.decode())
