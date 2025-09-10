import string

def cifrador_vigenere(mens, chave):
    alfabeto = string.ascii_uppercase
    pos_chave = [alfabeto.index(c) for c in chave if c in alfabeto]
    tam_chave = len(pos_chave)
    result = []

    j = 0
    for m in mens:
        if m in alfabeto:
            c = pos_chave[j % tam_chave]
            nova_pos = (alfabeto.index(m) + c) % 26
            result.append(alfabeto[nova_pos])
            j += 1
        else:
            result.append(m)
    return "".join(result)

def decifrador_vigenere(cifrado, chave):
    alfabeto = string.ascii_uppercase
    pos_chave = [alfabeto.index(c) for c in chave if c in alfabeto]
    tam_chave = len(pos_chave)
    result = []

    j = 0
    for c in cifrado:
        if c in alfabeto:
            k = pos_chave[j % tam_chave]
            nova_pos = (alfabeto.index(c) - k) % 26
            result.append(alfabeto[nova_pos])
            j += 1
        else:
            result.append(c)
    return "".join(result)