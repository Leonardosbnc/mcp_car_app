import sqlite3


class Carro:
    def __init__(
        self,
        ano,
        cor,
        marca,
        tipo_combustivel,
        modelo,
        tipo_cambio,
        nome,
        quilometragem,
        num_portas,
        motorizacao,
        preco,
    ):
        self.ano = ano
        self.cor = cor
        self.marca = marca
        self.tipo_combustivel = tipo_combustivel
        self.modelo = modelo
        self.tipo_cambio = tipo_cambio
        self.nome = nome
        self.quilometragem = quilometragem
        self.num_portas = num_portas
        self.motorizacao = motorizacao
        self.preco = preco

    def create(self):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        sql = f"INSERT INTO carros(ano, cor, marca, tipo_combustivel, modelo, tipo_cambio, nome, quilometragem, num_portas, motorizacao, preco) VALUES ('{self.ano}', '{self.cor}', '{self.marca}', '{self.tipo_combustivel}', '{self.modelo}', '{self.tipo_cambio}', '{self.nome}', '{self.quilometragem}', '{self.num_portas}', '{self.motorizacao}', '{self.preco}');"
        try:
            cursor.execute(sql)
        except Exception as e:
            print(f"ERROR: {e}")
        finally:
            conn.commit()
            conn.close()
