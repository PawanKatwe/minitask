import random
import seaborn as sns
import matplotlib.pyplot as plt
boxkey = {}
prisonNo = range(1,101)
succeed = 0

result = []

for trial in range(1,10001):

    box_list = random.sample(prisonNo,100)

    key_list = random.sample(prisonNo,100)

    for i,j in zip(box_list, key_list):

        boxkey.update({i:j})
    n = 1
    found = 0
    for prisoner in range(1,101):
        box = prisoner
        n = 1
        key = boxkey[box]
        while n <= 50:

            if prisoner == key:
                
                #print("prisoner {} found key in box no {}".format(prisoner, box), boxkey[box])
                found += 1
                #print("Prisoner {} opened {} boxes to find key".format(prisoner,n) )

                break

            else:
                box = key
                key = boxkey[box]

                n += 1

    #print("total {} prisoners found the key".format(found))

    if found == 100:
        succeed +=1 
    else:
         pass

    #print(trial)
    result.append(round((succeed/trial)*100,2))


#print("total {} times succeed out of 100".format(succeed))

#print(result)


plt.plot(result)
plt.show()





    


