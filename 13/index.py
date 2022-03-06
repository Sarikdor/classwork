# 123
vowels = ['a', 'e', 'i', 'o', 'u']

human_text = input('Enter your text here: ')
words = human_text.split(' ')
pig_text_world = []
for word in words:
    if word[0].lower() in vowels:
        pig_world = word + 'way'
        pig_text_world.append(pig_world)
        continue
    end_lts = []
    for letter in word:
        if not(letter in vowels):
            end_lts.append(letter.lower())
            
        else: break
    pig_world = word[len(end_lts): ] + ''.join(end_lts) + 'ay'
    pig_text_world.append(pig_world)
print(' '.join(pig_text_world))