#imc = peso / (altura * altura)
print("academia MC valinhos")
print("--------------------")
print("Seja bem-vindos(a)!")

nome = input("me diga,por favor, o seu nome:")
idade = int(input("agora preciso que voce me informe as sua idade: "))
altura = float(input("informe o sua altura: ")) 
nascimento = 2024 - idade
peso = float(input("informe o seu peso:"))
IMC = peso / (altura * altura)

print("ola, senhor(a)", nome)
print("sua idade e: ", idade, "anos.")
print("voce nasceu em: ", nascimento)
print("seu altura e de: ", altura, "metros.")
print("seu peso e:", peso)
print("seu IMC e: {:2f} kg/m²".fomat(IMC))
                    
                  