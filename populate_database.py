import factory
import random

from server.carro import Carro
from server.utils import marcas, modelos, cambio, combustivel, motorizacao


def create_carro():
    carro_data = Carro(
        ano=factory.Faker("year"),
        cor=factory.Faker("color"),
        marca=random.choice(marcas),
        modelo=random.choice(modelos),
        tipo_combustivel=random.choice(combustivel),
        tipo_cambio=random.choice(cambio),
        nome=factory.Faker("first_name"),
        quilometragem=int(random.random() * 100),
        num_portas=random.choice([2, 3, 4]),
        motorizacao=random.choice(motorizacao),
        preco=int(random.random() * 1000),
    )
    carro_data.create()


for _ in range(100):
    create_carro()
