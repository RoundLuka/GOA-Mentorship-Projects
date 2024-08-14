"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. 
Leave punctuation marks untouched.

Test Cases:
'Pig latin is cool' -> 'igPay atinlay siay oolcay'
'This is my string' -> 'hisTay siay ymay tringsay'
"Ultima necat" -> 'ltimaUay ecatnay'
"Lux in tenebris lucet" -> 'uxLay niay enebristay ucetlay'
"Cucullus non facit monachum" -> 'ucullusCay onnay acitfay onachummay'
"""

# Solution

def mutate(string):
    result = []
    words = string.split()

    for word in words:
        if word[0].isalpha():
            result.append(word[1:] + word[0] + "ay")
        else:
            result.append(word)
    return " ".join(result)

# Test cases

print(mutate('Pig latin is cool'))
print(mutate('This is my string'))
print(mutate("Ultima necat" ))
print(mutate("Lux in tenebris lucet"))
print(mutate("Cucullus non facit monachum"))