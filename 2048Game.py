import os
import time
import random
# print("hello")
# time.sleep(2)
# os.system('cls')
mat=[
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]
def new_gen(mat):
    while True:
        r=random.randint(0,len(mat)-1)
        c=random.randint(0,len(mat[0])-1)
        if mat[r][c]==0:
            mat[r][c]=random.choice([2,4])
            break
def output():
    for row in mat:
        print(row)
    print("########################")

def down(mat):
    for i in range(len(mat[0])):
        f=0
        s=f+1
        while s<len(mat):
            while f<len(mat) and mat[f][i]==0:
                f+=1
            s=f+1
            while s<len(mat) and mat[s][i]==0:
                s+=1
            if s>=len(mat):
                break
            if mat[f][i]==mat[s][i]:
                mat[s][i]=2*mat[s][i]
                mat[f][i]=0
                f=s+1
                s=f+1
            else:
                f=s
            
        for j in range(len(mat)-1):
            if mat[j+1][i]==0:
                mat[j+1][i]=mat[j][i]
                mat[j][i]=0

def right(mat):
    for i in range(len(mat)):
        f=0
        s=f+1
        while s<len(mat[0]):
            while f<len(mat[0]) and mat[i][f]==0:
                f+=1
            s=f+1
            while s<len(mat[0]) and mat[i][s]==0:
                s+=1
            if s>=len(mat):
                break
            if mat[i][f]==mat[i][s]:
                mat[i][s]=2*mat[i][s]
                mat[i][f]=0
                f=s+1
                s=f+1
            else:
                f=s
        for j in range(len(mat[0])-1):
            if mat[i][j+1]==0:
                mat[i][j+1]=mat[i][j]
                mat[i][j]=0
        
def left(mat):
    for i in range(len(mat)):
        f=len(mat[0])-1
        s=f-1
        while s>=0:
            while f>=0 and mat[i][f]==0:
                f-=1
            s=f-1
            while s>=0 and mat[i][s]==0:
                s-=1
            if s<0:
                break
            if mat[i][f]==mat[i][s]:
                mat[i][s]=2*mat[i][s]
                mat[i][f]=0
                f=s-1
                s=f-1
            else:
                f=s
        for j in range(len(mat[0])-1,0,-1):
            if mat[i][j-1]==0:
                mat[i][j-1]=mat[i][j]
                mat[i][j]=0
def up(mat):
    for i in range(len(mat[0])):
        f=len(mat)-1
        s=f-1
        while s>=0:
            while f>=0 and mat[f][i]==0:
                f-=1
            s=f-1
            while s>=0 and mat[s][i]==0:
                s-=1
            if s<0:
                break
            if mat[f][i]==mat[s][i]:
                mat[s][i]=2*mat[s][i]
                mat[f][i]=0
                f=s-1
                s=f-1
            else:
                f=s
            
        for j in range(len(mat)-1,0,-1):
            if mat[j-1][i]==0:
                mat[j-1][i]=mat[j][i]
                mat[j][i]=0

while True:
    new_gen(mat)
    output()
    choice=input("enter your choice :\n")
    if choice=='u':
        up(mat)
    elif choice=='d':
        down(mat)
    elif choice=='l':
        left(mat)
    elif choice=='r':
        right(mat)
    os.system('cls')

