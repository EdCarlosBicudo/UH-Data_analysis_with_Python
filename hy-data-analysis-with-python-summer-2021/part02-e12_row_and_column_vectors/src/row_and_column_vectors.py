
import numpy as np

def get_row_vectors(a):
    _, m = a.shape
    return [row.reshape(1,m) for row in a[::1,]]

def get_column_vectors(a):
    n, _ = a.shape
    return [row.reshape(n,1) for row in a.T[::1,]]

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Row vectors:", get_row_vectors(a))
    print("Column vectors:", get_column_vectors(a))

if __name__ == "__main__":
    main()
