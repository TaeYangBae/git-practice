#test python env
def print_hello():
    animals = ['dog','cat','hamster','tiger'] # in one line
    foods = [
            'ham',
            'cheese',
            'Pizza'

    ] # w/o trailling comma
    names = [
            'John',
            'Jane',
            'Gil-Dong',
            'sun',
    ] #w/ trailing comma
    for f_name in names:
        print(f'hello, {f_name}')


if __name__ == '__main__':
    print_hello()
