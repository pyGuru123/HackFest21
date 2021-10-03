def cipher(txt, n):
    e_txt = ""
    for i in txt:
        if(i == " "):
            e_txt = e_txt+i
        elif(i.isupper()):
            e_txt = e_txt+chr((ord(i)+n-65) % 26+65)
        else:
            e_txt = e_txt+chr((ord(i)+n-97) % 26+97)
    return(e_txt)


inputText = input("ENTER TEXT : ")

n = int(input("ENTER SHIFT : "))
encoded = cipher(inputText, n)
print(encoded)
