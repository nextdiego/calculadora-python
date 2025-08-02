def soma(a, b):
    """
    Realiza a soma de dois números.
    
    Parâmetros:
    a (int/float): Primeiro número
    b (int/float): Segundo número
    
    Retorna:
    int/float: Resultado da soma
    """
    return a + b

def potencia(a, b):
    """
    Realiza a potencialização de um número a pela potencia b.
    
    Parâmetros:
    a (int/float): Primeiro número
    b (int/float): Segundo número (potencia)
    
    Retorna:
    int/float: Resultado da potencialização
    """
    return a ** b

def restoDivisao(a, b):
    '''
    Realiza a operação de resto de divisao entre dois numeros.
    parâmetros:
    a(int/float):primeiro número
    b(int/float):segundo numero
    retorna:
    int/float: Resultado da soma
    '''
    return a % b
    

def sub(a, b):
    """
    Realiza a subtração de dois números.
    
    Parâmetros:
    a (int/float): Primeiro número
    b (int/float): Segundo número
    
    Retorna:
    int/float: Resultado da subtração
    """
    return a - b

if __name__ == "__main__":
    print("Teste da função soma:")
    print(f"2 + 3 = {soma(2, 3)}") 
    print(f"5.5 + 4.5 = {soma(5.5, 4.5)}") 
    print(f'2 + 2 = {soma(2, 2)}')
    print('que galerinha massa, façam essa conta:')
    print(f'100 + 100 = {soma(100, 100)}')
    print(f' 3 + 10 = {soma(3,10)}') 
    print("vamo genteee (menos ana e seu tema branco)")


def divisao(a, b):
    """
    Realiza a divisao de dois números exatos.
    
    Parâmetros:
    a (int/int): Primeiro número
    b (int/int): Segundo número
    
    Retorna:
    int/int: Resultado da 
    """
    return a // b

if __name__ == "__main__":
    print("Teste da divisao:")
    print(f"10 // 5 = {divisao(10, 5)}") 
    print(f"45 // 9 = {divisao(45, 9)}") 
    print(f'2 // 2 = {divisao(2, 2)}')
    print('Espero que seja aprovado!')
    print("Teste função potencialização:")
    print(f'5 elevando a 3 potencia: {potencia(5,3)}')
    print('estou sofrendo bullying!!!!!!!')
    print("Teste da função subtração:")
    print(f"2 - 3 = {sub(2, 3)}") 
    print(f"5.5 - 4.5 = {sub(5.5, 4.5)}")
    print(f'10 - 7 = {sub(10, 7)}')
    print(f"resto divisão {restoDivisao(5,2)}")