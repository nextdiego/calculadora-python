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