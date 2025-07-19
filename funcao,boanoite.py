def bem_vindo():
    user=input('Qual seu nome? ')
    print(f'\nBem vindo, {user}, nós vamos calcular seu salário liquido, considerando imposto de renda por faixa')
    def salario ():
        qtt_HR= float(input('Quantas horas por dia você trabalha? '))
        valor_HR= float(input('Qual o valor da sua hora? '))
        dias_uteis = int(22)
        salario_bruto = float(qtt_HR*valor_HR*dias_uteis)
        if salario_bruto<1500:
            aliquota = 0
        elif salario_bruto<1800:
            aliquota = 0.15
        elif salario_bruto<2500:
            aliquota = 0.20
        else:
            aliquota=0.3
        salario_liquido = salario_bruto-float((salario_bruto*aliquota))    
        print(f'Seu salario liquido este mes será R${salario_liquido:.2f} reais. Faço bom proveito!')
    salario()   

bem_vindo()

