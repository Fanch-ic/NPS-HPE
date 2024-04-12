# Programme de décodoge des codes erreurs retournés par les commutateurs HPE sur le serveur NPS
#
#	-	CIRISI Cherbourg	-
#
#Fonctionnement :
#Code erreur en décimal à convertir en binaire sur 32 bits
#
#Découpage : 4 bits (bourrage) - 4 bits/4 bits/8 bits (interface x/y/z) - 12 bits (id vlan)
#
#Suivi des mises à jour
#
#1.0 - 10/04/2024 : création
#
#

import os

print("******************************************************")
print("\n\tProgramme de decodage des codes erreurs \n\tretournes par un commutateur HPE \n\tsur le serveur NPS")
print("\n******************************************************\n\n")

code = int(input("code erreur : "))

tableau = []
i = 0
while (i < 32):
    tableau.insert(i,0)
    i+=1

i = 0
while (code > 0):
	tableau.insert(i,code%2)
	code = code//2
	i+=1
	
print(" ")	
	
i = 31
print ("Valeur en binaire : ", end="")
while (i >= 0):
    print(tableau[i], end="")
    i-=1
	
print (" ")
print (" ")

i=27
print("Interface (binaire) : ", end="")
while (i > 11):
    if (i == 23) or (i == 19):
        print(" / ", end="")
    print(tableau[i], end="")
    i-=1

i=11
vlan=0
print(" ")
print("VLAN Id (binaire) : ", end="")
while (i >= 0):
    print(tableau[i], end="")
    vlan=vlan+(tableau[i]*(2**i))
    i-=1

print(" ")
print (" ")

i=27
j=0
print("Interface : ", end="")
while (i >= 24):
    j=j+(tableau[i]*(2**(i-24)))
    i-=1
    
print(j,"/ ", end="")
    
i=23
j=0
#print("Interface : ", end="")
while (i >= 20):
    j=j+(tableau[i]*(2**(i-20)))
    i-=1

print(j,"/ ", end="")

i=19
j=0
#print("Interface : ", end="")
while (i >= 12):
    j=j+(tableau[i]*(2**(i-12)))
    i-=1

print(j)

print("VLAN Id : ", vlan)

print (" ")
#print("FIN")

os.system("pause")
