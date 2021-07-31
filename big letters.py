'''
printing patters of alhabet from a to e
'''

def big_letters(i):
    patterns = {1:'  *  ',
                2:'*   *',
                3:'*****',
                4:' *** ',
                5:'**** ',
                6:' * * ',
                7:'  ***',
                8:' ****',
                9:'*    '
                }
    letters={'a':[1,2,3,2,2],
             'b':[3,2,5,2,3],
             'c':[3,9,9,9,3],
             'd':[5,2,2,2,5],
             'e':[3,9,3,9,3]
        }
    for i in letters[i]:
        print(patterns[i])

big_letters('a')
