message = input("Enter the message:")
alphabet='abcdefghijklmnopqrstuvwxyz'
key=6
encrypt=''
decrypt=''


for i in message:
    position=alphabet.find(i)
    newposition=(position+6)%26
    encrypt+=alphabet[newposition]
print(encrypt)


for i in encrypt:
    pos=alphabet.find(i)
    newpos=(pos-6)%26
    decrypt+=alphabet[newpos]
print(decrypt)