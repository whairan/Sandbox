def even(n):
    count = 0
    for i in range(n):
        if i % 2 == 0:
            count +=1
            print(i)
        else: 
            print(f"number {i}is odd")
    print(f"we have {count} even numbers between {0, n}")

even(int(input()))
