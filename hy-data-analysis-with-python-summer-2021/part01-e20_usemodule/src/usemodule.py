
# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle

def main():
    # Call the functions from here
    print(triangle.hypothenuse(10, 10))
    print(triangle.area(10, 10))
    print(triangle.__version__)
    print(triangle.__author__)

if __name__ == "__main__":
    main()
