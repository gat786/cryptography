import string as string
class CaesarCipher:
    plain_text=""
    key=0
    keys_values={}
    values_keys={}
    def __init__(self, plain_text, key):
        self.plain_text=plain_text.replace(" ","")
        self.key=key

        # making letter dictionary
        
        i=1
        for a in string.ascii_lowercase:
            self.keys_values[i]=a
            self.values_keys[a]=i
            i=i+1
        
        # for a in string.ascii_uppercase:
        #     self.keys_values[a]=i
        #     i=i+1

        # print(self.keys_values)

    def create_cipher(self):
        cipher_text=[]
        for chars in self.plain_text:
            char_num=self.values_keys[chars]
            new_num=char_num+self.key
            if new_num > 26:
                new_num=new_num-26

            cipher_text.append(self.keys_values[new_num])
        return "".join(cipher_text)

print("#### Welcome to Caesar Cipher Generator ####")
print("Enter Plain Text ")
plain_text=input("")
print("Enter Key Number ")
key=int(input())



    
a=CaesarCipher(plain_text,key)
cipher=a.create_cipher()
print("Cipher Text Generated is  ")
print(cipher)


    