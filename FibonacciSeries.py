import time


def fiboIter(n):
    prevNum = 0
    currentNum = 1
    for i in range(1, n):
        prePrevNum = prevNum
        prevNum = currentNum
        currentNum = prevNum + prePrevNum
    return currentNum


def fiboRecur(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fiboRecur(n-1) + fiboRecur(n-2)


if __name__ == "__main__":
    num = int(input("Enter a number"))
    init = time.time()
    print(f"Using Recusions Value of fibo({num}) is {fiboRecur(num)}")
    # print(f"Using Iteration Value of fibo({num}) is {fiboIter(num)}")
    print(f"It took {time.time() - init} seconds")
