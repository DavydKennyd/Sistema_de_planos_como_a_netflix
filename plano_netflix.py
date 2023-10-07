#criando uma classe para o cliente da netflix
class Clientes:
    def __init__(self,nome,email,plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ["basic","premium"]
        if plano in self.lista_planos:
            self.plano = plano
        else:
            print('Plano inválido.')
        self.plano = plano

    def Mudar_plano(self,novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print("Plano inválido")



Clientes = Clientes("Davyd","davyd@gmail","basic")
print(Clientes.plano)

#botão de upgrade
Clientes.Mudar_plano("blala")
print(Clientes.plano)