from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Define the input and output filenames
input_image_filename = 'input_image.jpg'
output_image_filename = 'encrypted_image.jpg'
decrypted_image_filename = 'decrypted_image.jpg'

# Generate a random 16-byte (128-bit) encryption key
encryption_key = get_random_bytes(16)

# Create an AES cipher object with the encryption key and AES.MODE_EAX mode
cipher = AES.new(encryption_key, AES.MODE_EAX)

# Read the input image file
with open(input_image_filename, 'rb') as input_file:
    plaintext = input_file.read()

# Encrypt the image data
ciphertext, tag = cipher.encrypt_and_digest(plaintext)

# Write the encrypted image data to the output file
with open(output_image_filename, 'wb') as output_file:
    output_file.write(cipher.nonce)
    output_file.write(tag)
    output_file.write(ciphertext)

print("Image encryption complete. The encryption key is:", encryption_key.hex())

# Decryption
with open(output_image_filename, 'rb') as input_file:
    nonce = input_file.read(16)  # Read the nonce (first 16 bytes)
    tag = input_file.read(16)    # Read the tag (next 16 bytes)
    ciphertext = input_file.read()  # Read the remaining data

# Create an AES cipher object with the encryption key and AES.MODE_EAX mode
cipher = AES.new(encryption_key, AES.MODE_EAX, nonce=nonce)

# Decrypt the image data
plaintext = cipher.decrypt(ciphertext)

# Write the decrypted image data to the output file
with open(decrypted_image_filename, 'wb') as output_file:
    output_file.write(plaintext)

print("Image decryption complete.")

