import pandas as pd
import numpy as np
import glob
import os

df = pd.read_csv('Aword.csv')


def horizontal(x, y, yi, tot):
    global charr
    global df
    word = ''
    for i in range(y, y + 1):
        for j in range(yi, yi + 1):
            for u in range(i, tot):
                for v in range(j, tot):
                    word += charr[u][v]
                    if len(word) > 2:
                        if not df[df['words'] == word].empty:
                            print(word)
                        else:
                            pass
                break


def vertical(x, y, yi, tot):
    global charr
    global df
    word = ''
    for i in range(y, y + 1):
        for j in range(yi, yi + 1):
            for u in range(i, tot):
                for v in range(j, tot):
                    word += charr[v][u]
                    if len(word) > 2:
                        if not df[df['words'] == word].empty:
                            print(word)
                        else:
                            pass
                break
        break


def slant_a(x, y, yi, tot):
    global charr
    global df
    tempword = ''
    word = ''
    u = 0
    if (y == tot - 1):
        return ()
    for i in range(y, y + 1):
        for j in range(yi, yi + 1):
            if (j == tot - 1):
                return ()
            # print('i,j=', i, j)
            while True:
                for f in range(i, y + 1):
                    for g in range(j, yi + 1):
                        for u in range(f + 1, tot):
                            for v in range(1, tot):
                                # Forming Relation
                                for cond in range(0, tot):
                                    #print('cond=', cond)
                                    if (abs(f - u) == cond and abs(g - v) == cond):
                                        # print('f,g=', f, g, ' u,v=', u, v)
                                        # print("debug ", abs(f - u), abs(g - v))
                                        tempword += charr[u][v]
                                        word = charr[f][g] + tempword
                                        if len(word) > 2:
                                            if not df[df['words'] == word].empty:
                                                print(word)
                                            else:
                                                pass
                if (u == tot - 1):
                    break


n = int(input("Order of Square Mat: "))
chararr = np.chararray((n,n), unicode=True)
for i in range(0,n):
    for j in range(0,n):
        chararr[i][j]=str(input())
print(chararr)
charr=chararr

for m in range(0,n):
    for mi in range(0,n):
        horizontal(chararr[m][mi], m, mi, n)
        vertical(chararr[m][mi],m,mi,n)
        slant_a(chararr[m][mi],m,mi,n)
