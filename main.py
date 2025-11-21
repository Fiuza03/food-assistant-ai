from restaurant import Restaurante
from assistant import AssistenteIA

restaurante = Restaurante("data.json")
assistente = AssistenteIA(restaurante)

print("🤖 Assistente do iFood iniciado! Digite sua pergunta (ou 'sair'):")

while True:
    pergunta = input("Cliente: ")

    if pergunta.lower() == "sair":
        print("Encerrando atendimento...")
        break

    resposta = assistente.responder(pergunta)
    print("Assistente:", resposta)
