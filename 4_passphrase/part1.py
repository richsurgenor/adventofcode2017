# superior solution would use a set and compare length

total = 0

with open("input") as f:
    content = [x.strip() for x in f.readlines()]

    for line in content:
        passphrase = []
        words = line.split(" ")
        valid = True
        for word in words:
            if word in passphrase:
                valid = False
                break
            else:
                passphrase.append(word)

        if valid:
            total += 1
        else:
            valid = True

print(total)
