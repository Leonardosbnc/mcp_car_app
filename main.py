import sqlite3
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel
from typing import List


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


@mcp.resource("carros://list")
def get_carros() -> CarsResponse:
    conn = sqlite3.connect("database.db")
    try:
        sql = "SELECT ano, cor, marca, tipo_combustivel, modelo, tipo_cambio, nome, quilometragem, num_portas, motorizacao, preco FROM carros;"
        result = conn.execute(sql)
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

        cars_list = []
        for row in result:
            data = {}
            for idx, key in enumerate(columns):
                data[key] = row[idx]
            cars_list.append(data)

        return {"carros": cars_list}
    except Exception as e:
        return {"err": f"Error: {str(e)}"}
