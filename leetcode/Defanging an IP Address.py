def defangIPaddr(address: str) -> str:
    b = str()
    for i in range(len(address)):      
        if(address[i] != "."):
            b += address[i]
        else:
            b += "[.]" 
    return b

address = str(input())
a = defangIPaddr(address)
print(a)