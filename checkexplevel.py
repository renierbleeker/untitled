str = "Medior Software Tester bij Volant Groep in Gouda"

find_words = ["Junior","Medior","Senior"]

def find_str(s, char):
    index = 0

    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return index

            index += 1

    return -1

for i in find_words:
    result = find_str(str, i)
    if result == 0:
        explevel = i
        break
    else:
        explevel = "not found"
