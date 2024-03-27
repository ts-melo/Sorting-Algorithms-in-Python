def bubble_sort(v):
    n = len(v)
    for i in range (n-1):
        swapped = False
        for j in range (n-1-i):
           if v[j] > v[j+1]:
               v[j], v[j+1] = v[j+1], v[j]
               swapped = True
        if not swapped:
            break

def print_array(v):
    n = len(v)
    for i in range (n):
        print(v[i], end=" ")

def main():
    with open('numeros.txt', 'r') as f:
        v = [float(line.strip()) for line in f]
    
    print_array(v)
    print("\n")
    bubble_sort(v)
    print_array(v)

if __name__  == "__main__":
    main()