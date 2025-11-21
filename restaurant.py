import json

class Restaurante:
    def __init__(self, arquivo_json):
        with open(arquivo_json, "r", encoding="utf-8") as f:
            dados = json.load(f)

        self.nome = dados["nome"]
        self.horario = dados["horario"]
        self.endereco = dados["endereco"]
        self.cardapio = dados["cardapio"]

    def listar_pizzas(self):
        return [item["nome"] for item in self.cardapio]

    def pizza_sem_lactose(self):
        return [item["nome"] for item in self.cardapio if item["sem_lactose"]]

    def pizza_sem_gluten(self):
        return [item["nome"] for item in self.cardapio if item["sem_gluten"]]
