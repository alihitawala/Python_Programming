__author__ = 'aliHitawala'

def censor(text, word):
    length = len(word)
    asterix = ''
    for i in range(length):
        asterix +='*'
    return text.replace(word, asterix)

print censor('hey hey hey', 'hey')