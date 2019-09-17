#!/usr/bin/env python

import random
import time

gen_file = raw_input("Generate file|.txt| with keys?  [yes/no] > ")
if gen_file == 'yes':
    name = raw_input("\nPlease name the file. > ")
    # find current file path
    import os
    path = os.path.dirname(os.path.realpath(__file__))

def matrix():
    # lists are here so they wont get called every time the function runs
    lower_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    upper_ = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
              'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numeric_ = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    digit_ = ['.', ',', '-', ':', '%', '&', '/', '#', '@']

    lists_ = ['a', 'b', 'c', 'd']

    x = 5
    y = 5

    # creation of 5x5 matrix
    a = [[0 for row in range (0, x)] for col in range (0, y)]

    for j in range (y):
        for i in range (x):
            a [j] [i] = random.choice(lists_)

    # assigning coordinates in dictionary
    dic = { 'a' : a[0][0] +'!'+ a[1][0] +'!'+ a[2][0] , 'n' : a[2][3] +'!'+ a[3][3] +'!'+ a[4][3] ,
            'b' : a[0][1] +'!'+ a[1][1] +'!'+ a[2][1] , 'o' : a[2][4] +'!'+ a[3][4] +'!'+ a[4][3] ,
            'c' : a[0][2] +'!'+ a[1][2] +'!'+ a[2][2] , 'p' : a[0][0] +'!'+ a[0][1] +'!'+ a[0][2] ,
            'd' : a[0][3] +'!'+ a[1][3] +'!'+ a[2][3] , 'q' : a[1][0] +'!'+ a[1][1] +'!'+ a[1][2] ,
            'e' : a[0][4] +'!'+ a[1][4] +'!'+ a[2][4] , 'r' : a[2][0] +'!'+ a[2][1] +'!'+ a[2][2] ,
            'f' : a[1][0] +'!'+ a[2][0] +'!'+ a[3][0] , 's' : a[3][0] +'!'+ a[3][1] +'!'+ a[3][2] ,
            'g' : a[1][1] +'!'+ a[2][1] +'!'+ a[3][1] , 't' : a[4][0] +'!'+ a[4][1] +'!'+ a[4][2] ,
            'h' : a[1][2] +'!'+ a[2][2] +'!'+ a[3][2] , 'u' : a[0][1] +'!'+ a[0][2] +'!'+ a[0][3] ,
            'i' : a[1][3] +'!'+ a[2][3] +'!'+ a[3][3] , 'v' : a[1][1] +'!'+ a[1][2] +'!'+ a[1][3] ,
            'j' : a[1][4] +'!'+ a[2][4] +'!'+ a[3][4] , 'w' : a[2][1] +'!'+ a[2][2] +'!'+ a[2][3] ,
            'k' : a[2][0] +'!'+ a[3][0] +'!'+ a[4][0] , 'x' : a[3][1] +'!'+ a[3][2] +'!'+ a[3][3] ,
            'l' : a[2][1] +'!'+ a[3][1] +'!'+ a[4][1] , 'y' : a[4][1] +'!'+ a[4][2] +'!'+ a[4][3] ,
            'm' : a[2][2] +'!'+ a[3][2] +'!'+ a[4][2] , 'z' : a[0][2] +'!'+ a[0][3] +'!'+ a[0][4] }

    corrects = 0
    for z in sorted(dic):

        checker = 0
        pass_wrd = dic[z]

        if pass_wrd.find('a') != (-1):
            corrects += 1
            checker += 1

        if pass_wrd.find('b') != (-1):
            corrects += 1
            checker += 1

        if pass_wrd.find('c') != (-1):
            corrects += 1
            checker += 1

        if pass_wrd.find('d') != (-1):
            corrects += 1
            checker += 1

        if checker < 2:
            break

    if checker < 3:
        return False

    else:

        # optimal (impossible) 78
        if corrects >= 70: 

            print '\nCorrects: %d/78 \n' % corrects

            for j in xrange (y):
                for i in xrange (x):

                    if   a[j][i] == 'a':
                        a[j][i] = random.choice(lower_)

                    elif a[j][i] == 'b':
                        a[j][i] = random.choice(upper_)

                    elif a[j][i] == 'c':
                        a[j][i] = random.choice(numeric_)

                    elif a[j][i] == 'd':
                        a[j][i] = random.choice(digit_)

            mat = ''
            for row in a:
                for val in row:
                    mat += ' | ' + val
                mat += ' |\n'
            print mat

            try:
                with open('%s/%s.txt' % (path,name), 'a') as file:
                    file.write('\nCorrects: %d/78\n' % corrects)
                    file.write(mat)
            except:
                pass

        else:
            return False


for i in xrange(2):
    count = 0
    t0 = time.time()
    while matrix() == False:
        count += 1
        pass
    print "\nIteration n' %d" % count
    print "%ds\n" % int(time.time() - t0)


