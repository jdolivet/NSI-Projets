m = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#c = ["f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e"]
c = [0] * 26
c[21] = "a"
c[22] = "b"
c[23] = "c"
c[24] = "d"
c[25] = "e"

for i in range(len(m) - 5):
    c[i] = m[i + 5]

def encryptC(normal):
    code = ""
    for i in range(len(normal)): # On cherche combien il y a de nombre de lettre dan le mot/normal
        lettre = normal[i]
        position = -1


        for j in range(len(m)): #cherche cette lettre dans l’alphabet m
            if m[j] == lettre: #stocke la lettre courante
               position = j #mémorise l’indice (position) si la lettre est trouvée
               break

        if position != -1:
           code = code + c[position]
        else:
            code = code + lettre

    return code


def decodeC(code):
    normal = ""
    for i in range(len(code)): # On cherche combien il y a de nombre de lettre dan le mot codé
        lettre = code[i]
        position = -1

        for j in range(len(c)): #cherche cette lettre dans l’alphabet c
            if c[j] == lettre: #stocke la lettre courante
               position = j #mémorise l’indice (position) si la lettre est trouvée
               break
        if position != -1:
           normal = normal + m[position]
        else:
            normal = normal + lettre

    return normal
