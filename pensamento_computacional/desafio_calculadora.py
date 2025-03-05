# Projeto guiado da trilha Pensamento Computacional com Python do TIC em Trilhas
# O projeto consiste em fazer uma calculadora simples através de um menu principal

def calculadora():
	while True:
		print("Calculadora Simples\n")
		print("1. Soma")
		print("2. Subtração")
		print("3. Multiplicação")
		print("4. Divisão")
		print("s. Sair")
		operacao = input("Selecione uma opção ou 's' para sair: ")

		if operacao == 's' or operacao == 'S':
			print("Obrigado por utilizar a Calculadora Simples! :)")
			break

		if operacao not in ['1', '2', '3', '4']:
			print("Opção inválida! Tente novamente.")
			print("________________________________\n")
			continue

		numero1 = float(input("Primeiro número: "))
		numero2 = float(input("Segundo número: "))

		if operacao == '1':
			resultado = numero1 + numero2
			print("O resultado da operação soma é: ", resultado)
		elif operacao == '2':
			resultado = numero1 - numero2
			print("O resultado da operação subtração é: ", resultado)
		elif operacao == '3':
			resultado = numero1 * numero2
			print("O resultado da operação multiplicação é: ", resultado)
		else:
			if numero2 == 0:
				print("Divisões por zero não são possíveis. Tente novamente.")
				print("_____________________________________________________\n")
				continue
			else:
				resultado = numero1 / numero2
				print("O resultado da operação divisão é: ", resultado)


calculadora()