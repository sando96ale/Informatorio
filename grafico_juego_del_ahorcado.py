'''

 +----+ 
 |    |
 |    O   
 |   /|\  
 |   / \  
 === 

 '''


def mostrar_grafico(intentos):
    if intentos == 6:
        print('''
 +----+ 
 |    |   
 |    
 |   
 |  
 === 
''')
    elif intentos == 5:
        print('''
 +----+ 
 |    |   
 |    O   
 | 
 |  
 === 
''')
    elif intentos == 4:
        print('''
 +----+ 
 |    |   
 |    O   
 |    |
 | 
 === 
''')
    elif intentos == 3:
        print('''
 +----+ 
 |    |   
 |    O   
 |   /| 
 | 
 === 
''')
    elif intentos == 2:
        print('''
 +----+ 
 |    |   
 |    O   
 |   /|\  
 | 
 === 
''')
    elif intentos == 1:
        print('''
 +----+ 
 |    |   
 |    O   
 |   /|\  
 |   /
 === 
''')
    elif intentos == 0:
        print('''
 +----+ 
 |    |        
 |    O   
 |   /|\  
 |   / \  
 === 
''')
