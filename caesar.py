def caesar(message, key):
    result = ""
    alpha = string.ascii_lowercase
    for x in message:
        temp = x
        ind = alpha.find(x.lower())
        if(ind >= 0):
            temp = alpha[(ind + key) % 26]

        if(x.isupper()):
            temp = temp.upper()
        result += temp
    return result
