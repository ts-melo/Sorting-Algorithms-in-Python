import sys

def merge(v,l,r, m):
    n1 = m - l + 2
    n2 = r-m + 1
    L = [] 
    R = [] 
    for i in range(n1-1):
        L.append(v[l + i])
    for j in range(n2-1):
        R.append(v[m + 1 + j])
    L.append(sys.float_info.max)
    R.append(sys.float_info.max)
    i=0
    j=0
    for k in range (l, r+1):
        if L[i] <= R[j]:
            v[k] = L[i]
            i += 1
        else:
            v[k] = R[j]
            j += 1

def merge_sort(v, l, r):
    if l < r:
        m = (l+r)//2
        merge_sort(v, l, m)
        merge_sort(v, m+1, r)
        merge(v,l,r,m)

def print_array(v):
    n = len(v)
    for i in range (n):
        print(v[i], end=" ")

def main():
    with open('numeros.txt', 'r') as f:
        v = [float(line.strip()) for line in f]
    print_array(v)
    merge_sort(v, 0, len(v)-1)
    print_array(v)
    
if __name__ == "__main__":
    main()