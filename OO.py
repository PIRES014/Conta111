numero = 123
titular = "kiki"
saldo = 105.5
limite = 1000.0

conta = {"numero":123, "titular":"kiki",
         "saldo":105.5, "limite":1000.0 

}

print(conta["titular"])
print(conta["limite"])

def criar_conta(numero, titular, saldo,Limite): 
    conta = {"numero":numero, "titular":titular,
              "saldo":saldo, "limite":limite
              
 }
  return conta

 conta = criar_conta(345, "Everton", 200.0, 1000.0)
 print(conta["limite"])

 def depositar (conta, valor):
     conta["saldo"] += valor

     def saque(conta, valor):
        conta["saldo"] -= valor

        def extrato():
            print(f"Seu saldo atual é{conta["saldo"]}")

depositar(conta, 250.0)
extrato(conta)

saque(conta, 400.0)
extrato(conta)            
