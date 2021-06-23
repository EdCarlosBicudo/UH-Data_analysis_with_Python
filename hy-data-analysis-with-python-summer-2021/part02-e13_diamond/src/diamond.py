
import numpy as np

def diamond(n):
    se = np.eye(n, dtype=int)
    sd = np.eye(n, dtype=int)[:,::-1][:,:-1]
    s = np.concatenate((sd, se), axis=1)
    i = s[::-1][1:]
    d = np.concatenate((s,i))
    return d

def main():
    print(diamond(5))

if __name__ == "__main__":
    main()
