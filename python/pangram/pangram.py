def is_pangram(sentence):
    sent_set = set(sentence.lower())
    alphaset = set('abcdefghijklmnopqrstuvwxyz')
    return alphaset.issubset(sent_set)
