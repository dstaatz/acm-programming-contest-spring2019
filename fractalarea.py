# fractalarea.py

pi = 3.141592653589793

def calc(r, n):
    if n == 0:
        return 0
    return r**2 + (calc(r/2, n-1)*3)

def main():
    count = int(input())
    for i in range(count):
        input_ = input().split(" ")
        r = int(input_[0])
        n = int(input_[1])

        area = r**2
        area += calc(r/2, n-1) * 4

        print(area * pi)

if __name__ == "__main__":
    main()
