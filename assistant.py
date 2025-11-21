import os
from openai import OpenAI

class AssistenteIA:
    def __init__(self, restaurante):
        self.restaurante = restaurante
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


    def gerar_contexto(self):
        pizzas = ", ".join(self.restaurante.listar_pizzas())
        sem_lactose = ", ".join(self.restaurante.pizza_sem_lactose())
        sem_gluten = ", ".join(self.restaurante.pizza_sem_gluten())

        contexto = f"""
        Você é um atendente virtual do restaurante {self.restaurante.nome}.
        Horário: {self.restaurante.horario}
        Endereço: {self.restaurante.endereco}

        Pizzas disponíveis: {pizzas}
        Pizzas sem lactose: {sem_lactose}
        Pizzas sem glúten: {sem_gluten}
        """
        return contexto

    def responder(self, pergunta):
        contexto = self.gerar_contexto()

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": contexto},
                {"role": "user", "content": pergunta}
            ]
        )

        return response.choices[0].message.content
