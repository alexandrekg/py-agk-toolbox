
def run_try_else():
    try:
        print('Primeiro try')
    except:
        print('Não rodou')
    else:
        print('Executou o else também')
        print('-------------------------')


def run_try_finally_1():
    try:
        print('Run try..finally1')
    except:
        print('Não rodou')
    finally:
        print('Executou o finally também')
        print('-------------------------')

def run_try_finally_2():
    try:
        raise Exception("Run try..finally2 EXCEPTION")
    except:
        print('Run try..finally2 EXCEPTION')
    finally:
        print('Run try..finally2 FINALLY')
        print('-------------------------')

def main():
    run_try_else()
    run_try_finally_1()
    run_try_finally_2()


if __name__ == '__main__':
    main()