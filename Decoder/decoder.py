class Decoder:

    alphabet = "abcdefghijklmnopqrstuvwxyz "

    def decode(self, code, key):
        key = str(key)
        lock = ""
        for i in range(0, len(code)):
            code[i] = code[i] - int(key[i % len(key)])
            lock += self.alphabet[code[i] - 1]
        return lock

    def coder(self, word, key):
        key = str(key)
        code = []
        for i in range(0, len(word)):
            code.append(self.alphabet.find(word[i]) + int(key[i % len(key)]) + 1)

        return code


def main():
    deco = Decoder()
    while True:
        print("Хотите ли вы закодировать сообщение(1) или раскодировать существующее(2)?")
        a = input("Введите соответствующее число (для выхода введите любое другое число): ")
        if a == "1":
            word = input("\nВведите слово или фразу: ")
            key = input("\nВведите ключ: ")
            print("\nВаш код: ", deco.coder(word, key))
        elif a == "2":
            arr = []
            print("\nВводите элементы кода по одному за раз, для прекращения введите 0")
            inp = int(input())
            while inp != 0:
                arr.append(inp)
                inp = int(input())
            key = input("\nВведите ключ: ")
            print("\nВаше сообщение: ", deco.decode(arr, key))
        else:
            return 0


if __name__ == '__main__':
    main()
