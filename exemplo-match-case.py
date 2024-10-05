
def use_case():
    command = "Hello"
    # syntax error
    case "Hello"

    match command:
        # esse caso funciona porquê está dentro de um match
        case "Hello":
            print('Hi')


if __name__ == "__main__":
    use_case()