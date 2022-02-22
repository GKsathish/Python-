def anogram(a, b):
    c = [0]* ord("z")+[0]
    for i in a:
        c[ord(i)] += 1;
    for i in b:
        c[ord(i)] -= 1;
    for i in c:
        if i != 0:
            return False;
    return True;


def main():
    n = int(input())
    for i in range(n):
        a, b = input().split()
        print('YES' if anogram(a, b) else 'NO', end=' ')

main()
