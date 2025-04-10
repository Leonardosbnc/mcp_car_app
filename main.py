import sqlite3
import json
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel
from typing import List, Optional


class Car(BaseModel):
    ano: int
    cor: str
    marca: str
    tipo_combustivel: str
    modelo: str
    tipo_cambio: str
    nome: str
    quilometragem: int
    num_portas: int
    motorizacao: str
    preco: int


class CarsResponse(BaseModel):
    carros: List[Car]


mcp = FastMCP("MCP Server")


columns = [
    "ano",
    "cor",
    "marca",
    "tipo_combustivel",
    "modelo",
    "tipo_cambio",
    "nome",
    "quilometragem",
    "num_portas",
    "motorizacao",
    "preco",
]


@mcp.prompt("carros")
def get_carros(
    nome: Optional[str] = None,
    marca: Optional[str] = None,
    modelo: Optional[str] = None,
    ano_minimo: Optional[int] = None,
    ano_maximo: Optional[int] = None,
    tipo_combustivel: Optional[str] = None,
    tipo_cambio: Optional[str] = None,
    quilometragem: Optional[int] = None,
    num_portas: Optional[int] = None,
    motorizacao: Optional[str] = None,
    preco_minimo: Optional[int] = None,
    preco_maximo: Optional[int] = None,
) -> CarsResponse:
    conn = sqlite3.connect("database.db")
    try:
        sql = "SELECT ano, cor, marca, tipo_combustivel, modelo, tipo_cambio, nome, quilometragem, num_portas, motorizacao, preco FROM carros WHERE 1=1"

        if nome is not None:
            sql += f" AND nome like '%{nome}%'"
        if marca is not None:
            sql += f" AND marca = '{marca}'"
        if modelo is not None:
            sql += f" AND modelo = '{modelo}'"
        if ano_minimo is not None:
            sql += f" AND ano >= {ano_minimo}"
        if ano_maximo is not None:
            sql += f" AND ano <= {ano_maximo}"
        if tipo_cambio is not None:
            sql += f" AND tipo_cambio = '{tipo_cambio}'"
        if tipo_combustivel is not None:
            sql += f" AND tipo_combustivel = '{tipo_combustivel}'"
        if quilometragem is not None:
            sql += f" AND quilometragem <= {quilometragem}"
        if num_portas is not None:
            sql += f" AND num_portas = {num_portas}"
        if motorizacao is not None:
            sql += f" AND motorizacao = '{motorizacao}'"
        if preco_minimo is not None:
            sql += f" AND preco >= {preco_minimo}"
        if preco_maximo is not None:
            sql += f" AND preco <= {preco_maximo}"

        result = conn.execute(f"{sql};")
        cars_list = []
        for row in result:
            data = {}
            for idx, key in enumerate(columns):
                data[key] = row[idx]
            cars_list.append(data)

        return json.dumps({"carros": cars_list})
    except Exception as e:
        return json.dumps({"err": f"Error: {str(e)}"})
