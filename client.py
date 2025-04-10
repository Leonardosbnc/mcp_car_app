import json
from rich.console import Console
from rich.table import Table
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


server_params = StdioServerParameters(
    command="mcp",
    args=["run", "server.py"],
    env=None,
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            console = Console()

            console.print(
                "[bold]Ola![/bold] Sou o agente virtual [bold cyan]LeoSBNC[/bold cyan]."
            )
            console.print("Como posso ajudar?")
            input("-> ")
            console.print(
                "[bold]Entendi![/bold] Vou fazer algumas perguntas para entender quais critérios devo utilizar para melhor atende-lo..."
            )

            args = {}
            console.print("Qual o nome do veículo? ('ENTER' para pular)")
            nome = input("-> ")
            if len(nome) > 0:
                args["nome"] = nome
            console.print("Qual a marca? ('ENTER' para pular)")
            marca = input("-> ")
            if len(marca) > 0:
                args["marca"] = marca
            console.print("Qual o modelo? ('ENTER' para pular)")
            modelo = input("-> ")
            if len(modelo) > 0:
                args["modelo"] = modelo
            console.print("A partir de qual ano? ('ENTER' para pular)")
            ano_minimo = input("-> ")
            if len(ano_minimo) > 0:
                args["ano_minimo"] = ano_minimo
            console.print("Até qual ano?  ('ENTER' para pular)")
            ano_maximo = input("-> ")
            if len(ano_maximo) > 0:
                args["ano_maximo"] = ano_maximo
            console.print("Qual o tipo de combustivel? ('ENTER' para pular)")
            tipo_combustivel = input("-> ")
            if len(tipo_combustivel) > 0:
                args["tipo_combustivel"] = tipo_combustivel
            console.print("Qual o tipo de cambio? ('ENTER' para pular)")
            tipo_cambio = input("-> ")
            if len(tipo_cambio) > 0:
                args["tipo_cambio"] = tipo_cambio
            console.print("Qual quilometragem maxima? ('ENTER' para pular)")
            quilometragem = input("-> ")
            if len(quilometragem) > 0:
                args["quilometragem"] = quilometragem
            console.print("Quantas portas? ('ENTER' para pular)")
            num_portas = input("-> ")
            if len(num_portas) > 0:
                args["num_portas"] = num_portas
            console.print("Qual a motorizacao? ('ENTER' para pular)")
            motorizacao = input("-> ")
            if len(motorizacao) > 0:
                args["motorizacao"] = motorizacao
            console.print("A partir de qual preco? ('ENTER' para pular)")
            preco_minimo = input("-> ")
            if len(preco_minimo) > 0:
                args["preco_minimo"] = preco_minimo
            console.print("Qual valor maximo? ('ENTER' para pular)")
            preco_maximo = input("-> ")
            if len(preco_maximo) > 0:
                args["preco_maximo"] = preco_maximo * 100
            prompt = await session.get_prompt("carros", arguments=args)
            carros = json.loads(prompt.messages[0].content.text)["carros"]

            if len(carros) == 0:
                console.print("[bold red]Nenhum carro encontrado.[/bold red]")
                return

            table = Table(title="Carros")

            table.add_column("Nome", style="magenta")
            table.add_column("Marca")
            table.add_column("Modelo")
            table.add_column("Cor")
            table.add_column("Ano")
            table.add_column("Tipo Combustivel")
            table.add_column("Tipo Cambio")
            table.add_column("Motorizacao")
            table.add_column("Quilometragem")
            table.add_column("Numero de portas")
            table.add_column("Preco")

            for carro in carros:
                table.add_row(
                    str(carro["nome"]),
                    str(carro["marca"]),
                    str(carro["modelo"]),
                    str(carro["cor"]),
                    str(carro["ano"]),
                    str(carro["tipo_combustivel"]),
                    str(carro["tipo_cambio"]),
                    str(carro["motorizacao"]),
                    f"{carro['quilometragem']} km",
                    str(carro["num_portas"]),
                    f"R${carro['preco']/100}",
                )

            console.print(table)


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
