c = 0
h = input("Digite alguma coisa: ").lower()
for x in h:
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
        c = c + 1

print(c)
