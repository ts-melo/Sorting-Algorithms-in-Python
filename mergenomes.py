def mergenomes(v,l,m,r):
    n1 = m - l + 2
    n2 = r - m +1
    L = [] * n1
    R = [] * n2
    
    for i in range(n1-1):
        L.append( v[l+i])
    for j in range(n2-1):
        R.append(v[m + 1 + j])
    i=j=0
    k=l
    
    while i<len(L) and j<len(R):
        if L[i] <= R[j]:
            v[k] = L[i]
            i += 1
        else:
            v[k] = R[j]
            j += 1
        k +=1
    
    while i < len(L):
        v[k] = L[i]
        i += 1
        k+=1
    while j < len(R):
        v[k] = R[j]
        j += 1
        k+=1
def merge_sort(v, l, r):
    if l < r:
        m = (l+r)//2
        merge_sort(v, l, m)
        merge_sort(v, m+1, r)
        mergenomes(v,l,m,r)

def print_array(v):
    n = len(v)
    for i in range (n):
        print(v[i], end=" ")
    print("\n")
def main():
    with open('nomes.txt', 'r') as f:
        nomes = [line.strip() for line in f]
    print(nomes)
    merge_sort(nomes,0,len(nomes)-1)
    print(nomes)

if __name__ == "__main__":
    main()