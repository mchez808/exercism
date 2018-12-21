import re
def abbreviate(words):
    words = re.sub('-', ' ', words)
    list_words = words.upper().split()
    list_initials = [word[0] for word in list_words]
    joint_initials = "".join(list_initials)
    return "".join(re.findall(r'\w', joint_initials))

