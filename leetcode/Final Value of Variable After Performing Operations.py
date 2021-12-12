def finalValueAfterOperations(operations) -> int:
    x = 0
    for i in range(len(operations)):
        if(operations[i] == '++X'):
            x += 1
                
        elif(operations[i] == 'X++'):
            x += 1
            
        elif(operations[i] == '--X'):
            x -= 1
            
        elif(operations[i] == 'X--'):
            x -= 1
        
    return x

operations = ["--X","X++","X++"]    
a = finalValueAfterOperations(operations)
print(a)
