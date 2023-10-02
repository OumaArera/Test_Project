def prime_checker(base, top):
    count = 0

    for num in range(base, top + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break

            else:

                print(num, end=", ")
                count += 1

    print(f"\n\nTotal is {count}")


bottom = int(input("Enter the base number "))
upper = int(input("Enter the top number "))

prime_checker(bottom, upper)