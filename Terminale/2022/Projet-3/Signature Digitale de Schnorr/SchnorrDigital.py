from GroupeCyclique import *

#Script python qui permet d'expliquer le processus et les étapes d'une Signature Digitale de Schnorr.
#Utilise la console pour écrire de manière un peut plus ludique et compréhensible un exemple quelquonque du protocole.
#Permet la compréhension mathématique d'un exemple de Zero Knowledge Proof.

#Les réglages choisis peuvent être changés, il suffit de choisir un intervale different de la valeur p,
#Afin de changer l'ordre du Groupe Cyclique (quand plus grand p est, le plus de temps l'algorithme prendra.

print("---------------------------------------------------------------------------------- (1/10)")
print("Bob, veux prouver son identité à Alice. Il choisit donc d'utiliser une Signature Digitale de Schnorr.\n")
print("Il choisit celle-ci par:\n")
print("-Sa rapidité\n-La non-manipulation de valeurs énormes\n-Est une Preuve à Divulgation Nulle de Connaissance.\n")
input("Appuyez enter pour continuer.\n")

p = genere_premier(1000,10000,5000) #Genere un nombre premier compris entre 1000 et 10000, avec une fiabilité moyenne.
g = generateur(p)  #Un générateur de Zp

#On utilise un generateur d'un groupe Cyclique car cela implique que le Problème du Logaritme discret
#est assumé dificile en telles circonstances. Traditionnellement, on utilise un Groupe de Schnorr, qui vérifie les conditions:
#p = qr + 1 ou p et q sont premiers. Il générent Z_p(x) qui est le sousgroupe d'ordre premiers.
#C'est le groupe des multiplicatifs, des entiers modulo p.
#Mais pour faciliter l'affaire, je choisis ici un Groupe Cyclique quelquonque et non pas un Groupe de Schnorr.
#Il se peut que se groupe soit un groupe de Schnorr, bien évidemment, involontairement.)

print("---------------------------------------------------------------------------------- (2/10)")
print("Pour cela, il doit générer un nombre premier p, de sorte que le Groupe Z d'ordre p, soit Z_p, soit cyclique.")
print(f'Parmi tous les générateurs du groupe Z_p, il en choisit un aléatoire, nommé g.\n')
print(f"Il choisit donc, le nombre p: {p}, et le nombre g: {g}")
print(f"On a donc {g}, un générateur de Z_{p}.\n")

input("Appuyez enter pour continuer.\n")

secret = randint(1,p)
while gcd(secret,p) != 1:  #On cherche on cherche secret tel que secret et p soient premiers entre eux.
    secret = randint(1,p)
    
print("---------------------------------------------------------------------------------- (3/10)")    
print("Il choisit ensuite une valeur qu'il gardera en secret. Cette valeur, vérifie deux choses:")
print("Elle est comprise entre 1 et p, mais également elle est première avec p.\n") 
assert est_generateur(g,p) and gcd(secret,p) == 1  #Vérifier que les conditions sont assurés.
print(f"Le secret choisit est: {secret}")
print(f"En effet, 1 < {secret} < {p} et pgcd({secret},{p}) = 1.\n")

print(f"Rappel: p = {p}, g = {g}")
input("Appuyez enter pour continuer.\n")

print("---------------------------------------------------------------------------------- (4/10)")
print("La phase de choix de variables étant conclut, on passe maintenant à la phase de Signature.\n")

#Signature

M = 'Identifier pour régner'
y = pow(g,secret,p)  #L'utilisation de la fonction pow permet de réduire le coût en temps des opérations.
k = randint(1,p-1)
r = pow(g,k,p)  #Cela car l'algorithme pow(a,b,c) est plus efficient que (a**b) mod c pour les nombres de type int.

print(f'Bob choisit un message aléatoire: "{M}"')
print(f'Il calcule y = (g^secret) mod p = {g}^{secret} mod {p} = {y}')
print(f"De plus, il choisit une valeur aléatoire k, comprise dans l'intevalle [1,p[. Il choisit k = {k}")
print(f'Il calcule ensuite r = (g^k) mod p = {g}^{k} mod {p} = {r}\n')

print(f"Rappel: p = {p}, g = {g}, secret = {secret}")
input("Appuyez enter pour continuer.\n")

print("---------------------------------------------------------------------------------- (5/10)")
print("Bob doit utiliser une fonction de hachage. Celle-ci, renvoie un nombre, associé a un élément passé en paramètre.")
print("Aucun autre élément peut être associé a cet élément par la même fonction de hachage.")
#En réalité il est possibible, mais la probabilité reste petite. Quand plus grande la chaine de characteres, la moindre chance est.
print("Il choisit donc la fonction H de hachage, comme étant sha-256.\n")
#Après avoir appliqué la fonction sha256, le processus est irreversible.

input("Appuyez enter pour continuer.\n")
print("---------------------------------------------------------------------------------- (6/10)")
print("Il doit donc calculer e = H(r||M) mod (p-1).")
print("r||M correspond a une concaténation de chaines de characteres, r étant un nombre, il le transforme en un string.")

e = hachage(r,M) % (p-1)
s = (k - secret*e) % (p-1)

print(f'e = H(r||M) mod (p-1) = H("{str(r)+M}") mod {p-1} = {e}')
print(f"Il calcule également s = (k - secret*e) mod (p-1) = ({k} - {secret}*{e}) mod {p-1} = {s}\n")
print(f'La signature est le pair (s: {s}, e: {e})\n')

print(f'Rappel: p = {p}, g = {g}, secret = {secret}, M = "{M}", y = {y}, k = {k}, r = {r}')
input("Appuyez enter pour continuer.\n")

print("---------------------------------------------------------------------------------- (7/10)")
print("La phase de signature est conclue.")
print(f"Bob garde pour soit les valeurs, secret = {secret} et k = {k}")
print(f'Alice connait les variables publiques, g: {g}, p: {p}, y: {y}, M: "{M}", r: {r}')
print(f"Mais également la clé de signature générée par Bob: (e,s) = ({e},{s})\n")


#Verification
r2 = ((g**s)*(y**e)) % p
e2 = hachage(r2,M) % (p-1)

print(f"Elle calcule maintenant la valeur r2 = ((g^s)*(y^e)) mod p = (({g}^{s})*({y}^{e})) mod {p} = {r2}")
print(f'Elle calcule maintenant, grace a r2, e2 = H(r2||M) mod (p-1) = H("{str(r2)+M}") mod ({p-1}) = {e2}\n')

print(f'Rappel: p = {p}, g = {g}, secret = {secret}, M = "{M}", y = {y}, k = {k}, r = {r}, e = {e}, s = {s}')
input("Appuyez enter pour continuer.\n")

print("---------------------------------------------------------------------------------- (8/10)")
print(f'La signature est vérifiée si e = e2. En effet, e = {e}, e2 = {e2}. e est bien égal a e2.')
print(f'Or si e = H(r||M) mod (p-1) et e2 = H(r2||M) mod (p-1),')
print(f'On estime donc que cela implique r = r2. En effet, r = {r} et r2 = {r}. r = r2.\n')

input("Appuiez enter pour continuer.\n")

print("---------------------------------------------------------------------------------- (9/10)")
print("Mais pour quelle raison cela est-elle une Preuve à Divulgation Nulle de Connaissance?")
print("Bob prouve a Alice qu'il connait 'secret' sans lui transmettre cette information.")
print("Ce protocole peut facilement être utilisé pour augmenter la fiabilité et sureté des informations qui circulent dans l'Internet.")
print("Il peut en effet designer une identification dans un site, banque, application, entre autres.")
print("Où secret est le mot de passe, il est sécurisé et on ne le diffuse pas dans l'Internet.\n")

input("Appuiez enter pour continuer.\n")

print("---------------------------------------------------------------------------------- (10/10)")
print("Mais, comment r = r2?\n")
print("Attention, j'ignore les operations modulaires dans les étapes suivantes")
print("(car les maths vont fonctionner pareil sans la modularité). --> Si a = b, (a % c) = (b % c).\n")

print(f'Comme vu avant, r2 = (g^s)*(y^e), et r = g^k.')
print("On a aussi s = (k - secret*e) et y = g^secret. si on remplance r2 par ces valeurs, on obtient:")
print("r2 = (g^s)*(y^e) = (g^(k-secret*e))*((g^secret)^e) = (g^(k-secret*e))*(g^(secret*e)) \
= g^(k -(secret*e) + (secret*e)) = g^k = r")
print("On a donc effectivement r2 = r.")
print("----------------------------------------------------------------------------------")