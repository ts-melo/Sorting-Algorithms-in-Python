def max_heapify(v, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and v[l] > v[largest]:
        largest = l
    if r < n and v[r] > v[largest]:
        largest = r
    if largest != i:
        v[i], v[largest] = v[largest], v[i]
        max_heapify(v, n, largest)

def build_max_heap(v):
    n = len(v)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(v, n, i)

def heap_sort(v):
    build_max_heap(v)
    n = len(v)
    for i in range(n - 1, 0, -1):
        v[i], v[0] = v[0], v[i]  # Swap
        max_heapify(v, i, 0)

def main():
    with open('numeros.txt','r') as f:
        v = [float(line.strip()) for line in f]
    print(v)
    heap_sort(v)
    print(v)
    
if __name__ == "__main__":
    main()
