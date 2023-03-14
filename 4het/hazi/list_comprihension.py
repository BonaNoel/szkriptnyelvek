#!/usr/bin/env python3


def main():
    # 1 ['auto', 'villamos', 'metro'] → ['AUTO!', 'VILLAMOS!', 'METRO!']
    print("#1")
    li_1 = ['auto', 'villamos', 'metro']
    result_li_1 = [(s.upper() + '!') for s in li_1]
    print(li_1)
    print(result_li_1)

    # 2 ['aladar', 'bela', 'cecil'] → ['Aladar', 'Bela', 'Cecil']
    print('#2')
    li_2 = ['aladar', 'bela', 'cecil']
    result_li_2 = [s.capitalize() for s in li_2]
    print(li_2)
    print(result_li_2)

    # 3 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], azaz inicializáljunk egy 10-elemű listát csupa 0-val.
    print("#3")
    result_li_3 = [0 for n in range(10)]
    print(result_li_3)

    # 4 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] → [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    print("#4")
    result_li_4 = [n*2 for n in range(1, 11)]
    print(result_li_4)

    # 5 ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'] → [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] (az első listában sztringek vannak)
    print("#5")
    li_5 = [str(n) for n in range(1, 11)]
    result_li_5 = [int(s) for s in li_5]
    print(li_5)
    print(result_li_5)

    # 6 "1234567" → [1, 2, 3, 4, 5, 6, 7], vagyis van számunk sztring formátumban, s egy listába be akarjuk tenni a számjegyeit (számokként)
    print("#6")
    s6 = "123456"
    result_li_6 = [int(c) for c in s6]
    print(s6)
    print(result_li_6)

    # 7 'The quick brown fox jumps over the lazy dog' → [3, 5, 5, 3, 5, 4, 3, 4, 3], vagyis állapítsuk meg az egyes szavak hosszát
    print("#7")
    s7 = "The quick brown fox jumps over the lazy dog"
    result_li_7 = [len(w) for w in s7.split()]
    print(s7)
    print(result_li_7)

    # 8 "python is an awesome language" → ['p', 'i', 'a', 'a', 'l'], vagyis egy sztring szavainak a kezdőbetűit gyűjtsük össze egy listában
    print("#8")
    s8 = "python is an awesome language"
    result_li_8 = [w[0] for w in s8.split()]
    print(s8)
    print(result_li_8)

    # 9 'The quick brown fox jumps over the lazy dog' → [('The', 3), ('quick', 5), ('brown', 5),
    #  ('fox', 3), ('jumps', 5), ('over', 4), ('the', 3), ('lazy', 4), ('dog', 3)], vagyis a listában tuple-öket helyezzünk el a következő szerkezettel: (szó, szóhossz).
    print("#9")
    s9 = "The quick brown fox jumps over the lazy dog"
    result_li_9 = [(w, len(w)) for w in s9.split()]
    print(s9)
    print(result_li_9)

    # 10 [0, 2, 4, 6, 8], vagyis állítsuk elő egy listában a 10-nél kisebb páros számokat
    print("#10")
    result_li_10 = [n for n in range(10) if n % 2 == 0]
    print(result_li_10)

    # 11 Vegyük a 20-nál kisebb számokat s állítsuk elő ezeknek a négyzetét. Ezen négyzetszámok közül csak a párosakat hagyjuk meg ([0, 4, 16, 36, 64, 100, 144, 196, 256, 324]).
    print('#11')
    result_li_11 = [n*n for n in range(20) if n % 2 == 0]
    print(result_li_11)

    # 12 Vegyük a 20-nál kisebb számokat s állítsuk elő ezeknek a négyzetét. Ezen négyzetszámok közül csak azokat hagyjuk meg, melyeknek az utolsó számjegye "4" ([4, 64, 144, 324]).
    print('#12')
    result_li_12 = [n*n for n in range(20) if str(n*n)[-1] == '4']
    print(result_li_12)

    # 13 Gyűjtsük össze az angol ábécé nagybetűit egy listában (használjuk a chr függvényt), majd fűzzük össze az elemeket egyetlen sztringgé: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.
    print("#13")
    li_13 = [chr(n) for n in range(65, 91)]
    result_li_13 = ''.join([n for n in li_13])
    print(li_13)
    print(result_li_13)

    # 14 [' apple ', ' banana ', ' kiwi'] → ['apple', 'banana', 'kiwi'], vagyis a listában lévő szavak elejéről és végéről távolítsuk el a whitespace karaktereket
    print("#14")
    li_14 = [' apple ', ' banana ', ' kiwi']
    result_li_14 = ["".join(n.split()) for n in li_14]
    print(li_14)
    print(result_li_14)

    # 15 [1, 0, 1, 1, 0, 1, 0, 0] → "10110100", vagyis a listában lévő számjegyeket fűzzük össze egy sztringgé
    print("#15")
    li_15 = [1, 0, 1, 1, 0, 1, 0, 0]
    result_li_15 = "".join([str(n) for n in li_15])
    print(li_15)
    print(result_li_15)


if __name__ == "__main__":
    main()
