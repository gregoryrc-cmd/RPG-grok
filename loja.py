"""Regras da loja do jogo."""


def buscar_item(catalogo, nome):
    nome = nome.strip().casefold()
    for item in catalogo:
        if item["nome"].casefold() == nome:
            return item
    return None


def mostrar_catalogo(catalogo):
    if not catalogo:
        print("Catálogo vazio.")
        return
    for numero, item in enumerate(catalogo, start=1):
        print(f"{numero}. {item['nome']:<20} {item['tipo']:<12} {item['preco']} moedas")


def mostrar_inventario(heroi):
    print(f"{heroi['nome']} tem {heroi['ouro']} moedas.")
    if len(heroi["inventario"]) == 0:
        print("Inventário vazio.")
    for nome, quantidade in heroi["inventario"].items():
        print(f"  {quantidade} x {nome}")


def comprar(heroi, catalogo, nome, quantidade=1):
    item = buscar_item(catalogo, nome)
    if item is None:
        return "Esse item não existe na loja."
    if quantidade < 1:
        return "Quantidade inválida."
    custo = item["preco"] * quantidade
    if heroi["ouro"] < custo:
        return f"Ouro insuficiente: custa {custo} e você tem {heroi['ouro']}."
    heroi["ouro"] -= custo
    nome_item = item["nome"]
    heroi["inventario"][nome_item] = heroi["inventario"].get(nome_item, 0) + quantidade
    return f"Comprou {quantidade} x {nome_item} por {custo} moedas."


def vender(heroi, catalogo, nome, quantidade=1):
    item = buscar_item(catalogo, nome)
    if item is None:
        return "Esse item não existe na loja."
    nome_item = item["nome"]
    tem = heroi["inventario"].get(nome_item, 0)
    if quantidade < 1 or quantidade > tem:
        return f"Você só tem {tem} x {nome_item}."
    restante = tem - quantidade
    if restante == 0:
        del heroi["inventario"][nome_item]
    else:
        heroi["inventario"][nome_item] = restante
    valor = (item["preco"] // 2) * quantidade
    heroi["ouro"] += valor
    return f"Vendeu {quantidade} x {nome_item} por {valor} moedas."
