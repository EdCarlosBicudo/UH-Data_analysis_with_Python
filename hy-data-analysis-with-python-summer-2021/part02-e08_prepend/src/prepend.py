

class Prepend(object):

    def __init__(self, prefix):
        self.prefix = prefix

    def write(self, text):
        print(self.prefix + text)

def main():
    p = Prepend('+++ ')
    p.write('text')

if __name__ == "__main__":
    main()
