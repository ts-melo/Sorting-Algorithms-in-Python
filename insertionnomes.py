#insertionnomes
def insertion(v):
    n = len(v)
    for i in range (1,n):
        key = v[i]
        j = i-1
        while j >= 0 and v[j]>key:
            v[j+1] = v[j]
            j -= 1
        v[j+1] = key

def print_array(v):
    n = len(v)
    for i in range (n):
        print(v[i], end=" ")

def main():
    with open('nomes.txt', 'r') as f:
        v = [line.strip() for line in f]
    print_array(v)
    print("\n")
    insertion(v)
    print_array(v)
if __name__ == "__main__":
    main()