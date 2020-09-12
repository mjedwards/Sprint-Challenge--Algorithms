'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# def count_th(word, count=0):
#     print(word)
   
#     # TBC
#     if not word:
#         return

#     if 'th' not in word:
#         return 0

#     if 'th' in word:
#        return word.count('th')
 
def count_th(word):
    print(word)
   
    # TBC
    if word == '':
        return

    if 'th' not in word:
        return 0

    if word[0 : len('th')] == 'th':
       return count_th(word[len('th') - 1:]) + 1
    
    return count_th(word[len('th') - 1:])
 
