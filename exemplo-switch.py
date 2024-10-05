def main(actual_categories):
    categories = {
        0: "Aventura",
        1: "Ação",
        2: "Corrida",
        3: "Simulação"
    }
    # Usando o .get, caso não encontre no dicionário, pode ser usado como o valor default, igual no switch de outras linguagens
    result = [categories.get(mc, "Categoria não identificada") for mc in actual_categories]
    print("Categorias traduzidas: ", result)
    print("Categorias mock: ", actual_categories)
    print("--------------------------------------")

def use_case():
    main([2, 3])
    main([0])
    main([1])
    main([0, 1, 5])



if __name__ == "__main__":
    use_case()