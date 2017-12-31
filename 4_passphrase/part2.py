# alternative solution would sort each letter of a word 
total = 0

with open("input") as f:
    content = [x.strip() for x in f.readlines()]

    for line in content:
        passphrase = [] # instead of words add dictionaries resembling words
        valid = True
        words = line.split(" ")
        for word in words:
            meta_word = {}
            for letter in word:
                if letter in meta_word:
                    meta_word[letter] += 1 
                else:
                    meta_word[letter] = 1

            if meta_word in passphrase:
                valid = False
                break
            else:
                passphrase.append(meta_word)

        if valid:
            total += 1

print (total)

