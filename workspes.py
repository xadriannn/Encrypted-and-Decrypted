from cryptography.fernet import Fernet

#ey = Fernet.generate_key()

#with open('mykey.key', 'wb') as mykey:
    #mykey.write(key)

with open('mykey.key', 'rb') as mykey:
    key= mykey.read()

print(key)

#Encrypted File
#f = Fernet(key)

#with open('config.csv', 'rb') as original_file:
    #original = original_file.read()

    #encrypted = f.encrypt(original)

    #with open('enc_config.csv','wb')as encrypted_file:
        #encrypted_file.write(encrypted)

        #ADRIAN SYAH PUTRA
        #227006048
        #KEAMANAN INFORMASI

#Decrypted File
f = Fernet(key)

with open('enc_config.csv', 'rb')as encrypted_file:
    encrypted = encrypted_file.read()

    decrypted = f.decrypt(encrypted)

    with open('dec_config.csv', 'wb')as decrypted_file:
        decrypted_file.write(decrypted)