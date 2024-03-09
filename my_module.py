def test_function(content):
    print(f'this is an imported function with the parameter: {content}')


class Test:
    def __init__(self):
        self.name = 'My Class'
        self.value = 12

    @staticmethod
    def do_something(message):
        if message:
            print(message)
        else:
            print('hello')


test_var = 'test'

if __name__ == '__main__':
    print(__name__)
