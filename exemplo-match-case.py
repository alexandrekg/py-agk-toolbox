
def use_case():
    command = "Hello"
    # syntax error
    # case "Hello"

    match command:
        # esse caso funciona porquê está dentro de um match
        case "Hello":
            print('Hello to you too!')
        case "Goodbye, World!":
            print('See you later!')
        case other:
            print('No match found')


if __name__ == "__main__":
    use_case()