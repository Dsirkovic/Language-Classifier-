from funkcije2 import *

with open('eng.txt', 'r', encoding='utf8') as f:
    eng = f.read().lower()

with open('nl.txt', 'r', encoding='utf8') as f:
    nl = f.read().lower()

with open('tal.txt', 'r', encoding='utf8') as f:
    tal = f.read().lower()

eng_fr = freq_distr(eng)
nl_fr = freq_distr(nl)
tal_fr = freq_distr(tal)

languages = {'english': eng_fr, 'dutch': nl_fr, 'italian': tal_fr}
languages = smoothen(languages)

accurate = 0.0
all_languages = 0.0

with open('eng.test.txt', 'r', encoding='utf8') as f:
    for row in f:
        row = row.lower()
        if classify(row, languages) == 'english':
            accurate += 1
        all_languages += 1

with open('nl.test.txt', 'r', encoding='utf8') as f:
    for row in f:
        row = row.lower()
        if classify(row, languages) == 'dutch':
            accurate += 1
        all_languages += 1

with open('tal.test.txt', 'r', encoding='utf8') as f:
    for row in f:
        row = row.lower()
        if classify(row, languages) == 'italian':
            accurate += 1
        all_languages += 1


accuracy = accurate / all_languages
print('Classification accuracy: {:.5f}%'.format(accuracy * 100))
