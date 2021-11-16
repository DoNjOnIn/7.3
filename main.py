import random


def print1(A, i, j):
    if i < len(A):
        if j < len(A[i]):
            print(A[i][j], end=' ')
            print1(A, i, j + 1)
        else:
            print()
            print1(A, i + 1, 0)
    else:
        return

def sumn(A,i,j,s):
    s+=A[i][j]
    if j+1<len(A[i]):
        return sumn(A,i,j+1,s)
    else:
        return s

def find_neg(A,n,i,j):
    if i<n:
        if j<n:
            if A[i][j]<0:
                print('S('+str(i+1)+')='+str(sumn(A,i,0,0)))
                find_neg(A, n, i+1, 0)
            else:
                find_neg(A, n, i,j+1)
        else:
            find_neg(A,n,i+1,0)

def find(A,n,i,j):
    if i<n:
        if j<n:
            if A[i][j]==A[j][i]:
                if j==n-1:
                    print('k='+str(i+1))
                    find(A, n, i+1, 0)
                find(A, n, i , j+1)
            elif i < n:
                find(A, n, i + 1, 0)
        elif i<n:
            find(A, n, i + 1, 0)
    elif i ==n:
        print('Немає таких рядків')

def create(A,low,high,i,j):
    if i < len(A):
        if j < len(A[i]):
            A[i][j] = random.randint(low, high)
            create(A,low,high,i,j+1)
        create(A,low,high,i+1,0)
    return


def main():
    n = int(input('К-сть рядків\стовпців?='))
    low = int(input('Low='))
    high = int(input('High='))
    A = [[0] * n for i in range(n)]
    create(A, low, high, 0, 0)
    print1(A,0,0)
    find(A,n,0,0)
    find_neg(A,n,0,0)

if __name__ == '__main__':
    main()