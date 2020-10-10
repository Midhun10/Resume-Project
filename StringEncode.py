# i/o : HHHPPSDAAA
# o/p : 3H2P1S1D3A

def encode():
    usrinput = input("Enter a string")
    dict = {}
    for i in usrinput:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    result = ''.join(str(v) + str(k) for k, v in dict.items())
    print(result)


encode()
