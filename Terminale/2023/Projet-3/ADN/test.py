def message_to_base3(phrase):
    base3_str = ""
    for char in phrase:
        valeur_ascii = ord(char)
        representation_base3 = ""
        while valeur_ascii > 0:
            reste = valeur_ascii % 3
            representation_base3 = str(reste) + representation_base3
            valeur_ascii //= 3
        base3_str += representation_base3 + " "
    return base3_str


def convertir_en_adn(base3_sequence):
    # Correspondance entre les trits et les nucléotides
    trit_vers_nucleotide = {
        ("A", 0): "C",
        ("A", 1): "G",
        ("A", 2): "T",
        ("C", 0): "G",
        ("C", 1): "T",
        ("C", 2): "A",
        ("G", 0): "T",
        ("G", 1): "A",
        ("G", 2): "C",
        ("T", 0): "A",
        ("T", 1): "C",
        ("T", 2): "G"
    }
    
    sequences = base3_sequence.split()
    result = ""
    
    for sequence in sequences:
        ligne_actuelle = "A"  # Commencer avec la ligne 'A'

        for trit in sequence:
            index_nucleotide = int(trit)
            nucleotide = trit_vers_nucleotide[(ligne_actuelle, index_nucleotide)]
            result += nucleotide
        
            ligne_actuelle = nucleotide

        result += " " 

    return result.strip()



def adn_to_base3(adn_sequence):
    # Correspondance entre les paires de nucléotides et les trits en base-3
    nucleotide_to_trit = {
        ("A", "C"): 0,
        ("A", "G"): 1,
        ("A", "T"): 2,
        ("C", "G"): 0,
        ("C", "T"): 1,
        ("C", "A"): 2,
        ("G", "T"): 0,
        ("G", "A"): 1,
        ("G", "C"): 2,
        ("T", "A"): 0,
        ("T", "C"): 1,
        ("T", "G"): 2
    }

    sequences = adn_sequence.split()
    base3_sequences = []

    for sequence in sequences:
        base3_sequence = ""
        sequence = "A" + sequence  # La premiere lettre est definie en utilisant la collonde de A
        for i in reversed(range(len(sequence) - 1)):
            current_nucleotide = sequence[i]
            next_nucleotide = sequence[i + 1]

            if (current_nucleotide, next_nucleotide) in nucleotide_to_trit:
                trit = nucleotide_to_trit[(current_nucleotide, next_nucleotide)]
                base3_sequence = str(trit) + base3_sequence

        base3_sequences.append(base3_sequence)

    return " ".join(base3_sequences)

def base3_to_message(base3_str):
    base3_parts = base3_str.strip().split()
    phrase = ""
    for base3_repr in base3_parts:
        valeur_ascii = 0
        base3_repr = base3_repr[::-1]
        for i, chiffre in enumerate(base3_repr):
            valeur_ascii += int(chiffre) * (3 ** i)
        phrase += chr(valeur_ascii)
    return phrase

init = "saas"
print(init)
prep = message_to_base3(init)
print (message_to_base3(init))
adn = convertir_en_adn(prep)
print (adn)
b3 = adn_to_base3(adn)
print (b3)
res = base3_to_message(b3)
print (res)