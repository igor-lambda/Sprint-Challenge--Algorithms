'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    print(word)
    if word[:2] == "th":
        return 1 + count_th(word[1:])
    elif not word:
        return 0 
    else:
        return 0 + count_th(word[1:])

    

if __name__ == "__main__":
    count_th("width")