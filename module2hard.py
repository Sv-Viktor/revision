a = 20
s = ''
for b in range(1, 21):
    for c in range(b+1, 21):
        if a % (b + c) == 0:
            s = s + str(b) + str(c)
            print('b:', b, 'c:', c)

print(s)
