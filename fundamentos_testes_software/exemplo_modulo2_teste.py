# Reprodução do código exibido durante a trilha para experenciar sua execução
# Código exposto por Carlos Santana, professor da trilha

import unittest

def login(usuario,senha):
	if usuario == "teste" and senha == "teste123":
		return True

	return False

class TestLogin(unittest.TestCase):

	def test_login_sucess(self):
		usuario = "teste"
		senha = "teste123"

		resultado_login = login(usuario,senha)
		self.assertTrue(resultado_login)

	def test_login_error_wrong_pass(self):
		usuario = "teste"
		senha = "123"

		resultado_login = login(usuario,senha)
		self.assertFalse(resultado_login) #retorna verdadeiro, pois o resultado esperado é falso

if __name__ == '__main__':
	unittest.main()
