
import numpy as np

def get_rows(a):
    return [row for row in a[::1,]]

def get_columns(a):
    return [row for row in a.T[::1,]]

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))

if __name__ == "__main__":
    main()
