### Trabslater

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
        else:
            translation = translation + "g"
    return translation


trans = translate(input("Biror so'z yozing: "))
print(trans)