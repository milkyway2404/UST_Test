def program3():
    l, u, p, d = 0, 0, 0, 0

    #s = "R@m@_f0rtu9e$"

    password_list = [str(password_list) for password_list in input("Enter multiple passwords: ").split(",")]
    print("List of passwords is: ", password_list)
    for s in password_list:
        capitalalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        smallalphabets="abcdefghijklmnopqrstuvwxyz"
        specialchar="$#@"
        digits="0123456789"
        if (len(s) >= 12):
            for i in s:
                # counting lowercase alphabets
                if i in smallalphabets:
                    l += 1
                # counting uppercase alphabets
                if i in capitalalphabets:
                    u += 1
                # counting digits
                if i in digits:
                    d += 1
                # counting the mentioned special characters
                if i in specialchar:
                    p += 1
        if l >= 1 and u >= 1 and p >= 1 and d >= 1 and l+p+u+d == len(s):
            print(s, " Is Valid Password")
        else:
            print(s, " Is Invalid Password")
