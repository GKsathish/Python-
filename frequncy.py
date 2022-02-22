def findfrequency(line):
    line=line.lower()
    unique_char=set(line)
    unique_char.discard(' ')
    sorted_char=sorted(unique_char)
    for char in sorted_char:
        msg="{}:{}"
        print(msg.format(char,line.count(char)))
line=input()
findfrequency(line)