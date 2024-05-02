text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""
edited_text = text.replace(",", "").replace(".", "")
wordslist = edited_text.split( )
numberslist = list(map(len, wordslist))
print("".join(map(str,numberslist)))