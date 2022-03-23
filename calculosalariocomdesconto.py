# calculo salario com desconto

n1=float(input('Informe o ganho por hora: R$').replace(',','.'))
n2=int(input('Insira a Quantidade de Horas Trabalhadas: '))

salbruto = round(n1*n2,2)
ir = salbruto * 0.11
inss = salbruto * 0.08
sind = salbruto * 0.05
salliq = round(salbruto - (ir + inss + sind),2)

print('-------------------Calculo Salarial--------------------')
print('- Salário Bruto: R$%.2f'%salbruto)
print('----------------------Descontos------------------------')
print('- IR: R$%.2f'%ir)
print('- INSS: R$%.2f'%inss)
print('- Sindicato: R$%.2f'%sind)
print('------------------------Total--------------------------')
print('- Liquido: R$%.2f'%salliq)
print('--------------------------------------------------------')

# Renato Barbosa
