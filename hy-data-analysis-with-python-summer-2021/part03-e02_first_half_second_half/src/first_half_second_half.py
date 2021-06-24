
import numpy as np

def first_half_second_half(a):
    _, m = a.shape
    cut = int(m/2)
    final = np.sum(a[:, 0:cut], axis=1) > np.sum(a[:, cut:], axis=1)
    return a[final]

def main():
    a = np.array([[1, 3, 4, 2],
                  [2, 2, 1, 2],
                  [1, 3, 4, 2],
                  [2, 2, 1, 2]])
    print(first_half_second_half(a))

if __name__ == "__main__":
    main()
