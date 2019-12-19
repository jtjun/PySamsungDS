BIG = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SMALL = "abcdefghijklmnopqrstuvwxyz"

def encrypt(text, key):
    result = ""
    for char in text:
        if char in BIG:
            result += BIG[(BIG.find(char)+key) % len(BIG)]
        elif char in SMALL:
            result += SMALL[(SMALL.find(char)+key) % len(SMALL)]
        else:
            result += char
    
    return result

def decrypt(text, key):
    return encrypt(text, -key)


with open('encrypted.txt') as f:
    for line in f:
        if not line.strip():
            print(line, end='')
            continue

        key = int(line[:line.find(' ')])
        line = line[line.find(' ') + 1:]
        print(decrypt(line, key), end='')
