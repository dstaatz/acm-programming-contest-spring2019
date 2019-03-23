# bikegears.py

import sys

def min_gear(gear1, gear2):
    if (gear1['ratio'] < gear2['ratio']):
        return gear1
    elif (gear1['ratio'] > gear2['ratio']):
        return gear2
    else:
        if (gear1['front'] < gear2['front']):
            return gear1
        elif (gear1['front'] > gear2['front']):
            return gear2
        else:
            return gear1

def main():

    ans = []

    counts = input().split(' ')
    if (int(counts[0]) == 0 or int(counts[1]) == 0):
        return
    front_in = input().split(" ")
    back_in = input().split(" ")
    front = []
    back = []
    for n, i in enumerate(front_in):
        front.append(int(i))
    for n, i in enumerate(back_in):
        back.append(int(i))
    
    # print(front)
    # print(back)
    
    for f in front:
        for b in back:
            gear = {}
            gear['front'] = f
            gear['back'] = b
            gear['ratio'] = f/b
            ans.append(gear)

    # print(ans)

    sorted_ans = []

    items = len(ans)

    for i in range(items):
        min_ = ans[0]
        
        for gear in ans:
            min_ = min_gear(gear, min_)

        sorted_ans.append(min_)
        ans.remove(min_)

    # print(sorted_ans)
    for item in sorted_ans:
        print('(', item['front'], ',', item['back'], ')', sep='')

if __name__ == "__main__":
    main()
