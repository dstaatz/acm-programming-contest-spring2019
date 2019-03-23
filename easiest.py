# easiest.py


def main():
    input_ = int(input())

    while(input_ != 0):
        N = input_
        goal_sum = sum_digits(N)
        p=10

        while(True):
            p += 1

            sum_ = sum_digits(N * p)

            if (goal_sum == sum_):
                print(p)
                break
        
        input_ = int(input())


def sum_digits(i):
    # Sum the digits
    sum_ = 0
    multi = 1
    while(True):
        digit = i % (multi*10)
        i -= digit
        digit = digit // multi
        sum_ += digit
        
        multi *= 10

        if (i / multi < 1):
            break    

    return sum_


if __name__ == "__main__":
    main()