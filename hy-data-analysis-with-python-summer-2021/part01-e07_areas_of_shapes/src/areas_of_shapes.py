import math


def main():
    areas = {'triangle': lambda b, h: (b*h)/2,
             'rectangle': lambda w, h: (w*h),
             'circle': lambda r: math.pi * (r ** 2)}

    while True:
        shape = input("Choose a shape (triangle, rectangle, circle): ")

        if not shape:
            break

        if shape not in areas.keys():
            print("Unknown shape!")
            continue

        args = []
        if shape == "triangle":
            args.append(int(input("Give base of the triangle: ")))
            args.append(int(input("Give height of the triangle: ")))
        if shape == "rectangle":
            args.append(int(input("Give width of the rectangle: ")))
            args.append(int(input("Give height of the rectangle: ")))
        if shape == "circle":
            args.append(int(input("Give radius of the circle: ")))

        print(f"The area is {areas[shape](*args)}")

if __name__ == "__main__":
    main()
