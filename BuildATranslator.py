# All vowels --> g
# e.g. dog --> dgg, cat --> cgt

# Sajat algoritmus, egyszerubb, az eredeti else agati is hasznal
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                letter = "G"
            else:
                letter = "g"  # 'g' is jo, altalaban ugy tunik.
        translation = translation + letter
    return translation

print(translate(input("Input a phrase to translate: ")))
