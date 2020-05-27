import random
alphabets= """abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'"""

def encrypt(message):
    global shift_generator
    encrypted=[]
    embeded=[]

    for shift in message:
        shift_generator = random.randint(1, 26)
        print("Shift: ", shift_generator)
        if shift  in alphabets and shift.isalpha() and alphabets.index(shift)!=-1:
            old_position=alphabets.index(shift)
            new_position=old_position+shift_generator
            encrypted+=alphabets[old_position : new_position+1]
        else:encrypted += list(shift)
        return encrypted[-1]




def decrypt(encrypted):
    decrypted=[]
    for shift in encrypted:
        if shift in alphabets and shift.isalpha():
            old_position = alphabets.index(shift)
            new_position = old_position - shift_generator
            decrypted += alphabets[new_position]

            return decrypted

if "__name__==main":
    message = input("Type message: ")
    encryption=encrypt(message)
    print("Encrypted Message: ", encryption, end="")
    print("Decrypted Message: ",decrypt(encryption), end="")



