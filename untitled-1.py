def probleme16(n):
    puissance=2**n
    somme=0
    for x in str(puissance):
        somme+=int(x)
    return somme

assert probleme16(15) == 26

print(probleme16(1000))


f = open('listepremons.txt','r')

def alphabeticalvalue (name):
    somme=0
    for i in name:
        somme+=ord(i)-64 #pour respecter ord(A)=1
    return(somme)

assert alphabeticalvalue('COLIN') == 53

def probleme22(text):
    somme=0
    for s in text:
        names = s[1:len(s)-1].split('","')
        namesordered = sorted(names)
        for i in range(len(names)):
            somme += alphabeticalvalue(namesordered[i])*(i+1)
    return (somme)
            
print(probleme22(f))