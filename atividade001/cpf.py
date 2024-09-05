
def verificador_cpf(cpf):
    '''
    Verifica se um CPF é verdaeiro ou falso
    Usando o método dos últimos dois dígitos verificadores
    '''
    lista_numeros = []
    if cpf[3] == "." and cpf[7] == "." and cpf[11] == "-":
        print("O formato do CPF está correto")
        
        cpf = cpf.replace(".","")
        cpf = cpf.replace("-","")
        
        for i in range(0,11):
            lista_numeros.append(int(cpf[i]))
            i+=1  
        
        
        #calcular os numeros verificadores
        resultado_1 = []

        for i in range (9): 
            resultado = lista_numeros[i] * (i+1)
            resultado_1.append(resultado)
            i += 1
        resto_do_resultado_1 = sum(resultado_1)%11
        if resto_do_resultado_1 == 10: #o resto é o primeiro digito verificador
            resto_do_resultado_1 = 0


        resultado_2 = []

        for i in range(9):
            resultado = lista_numeros[i] * i+1
            resultado_2.append(resultado)
            resultado_2.append(resto_do_resultado_1*9)#primeiro numero x 9
            i += 1
        resto_do_resultado_2 = sum(resultado_2)%11
        
        if resto_do_resultado_2 == 10: #o resto é o primeiro digito verificador
            resto_do_resultado_2 = 0
            

        if resto_do_resultado_1 == int(lista_numeros[9]) and resto_do_resultado_2 == int(lista_numeros[10]):
            print("CPF é verdadeiro!!")
        else:
            print("CPF é falso!!")
                 
    else:
        print("O formato do CPF está errado")
        
cpf = str(input("Digite um CPF no formato xxx.xxx.xxx-xx: "))
verificador_cpf(cpf)
