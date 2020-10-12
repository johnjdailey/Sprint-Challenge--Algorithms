#count_th.py



'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurrences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    if not word:
        return 0

    if word.startswith("th"):
        return 1 + count_th(word[2:])
    else:
        return count_th(word[1:])
