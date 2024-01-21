#Write a program to compute the frequency of the words from the input.
#The output should output after sorting the key alphanumerically.
#○ Eg - line = “which is better python 2 or python 3”
def program1():
    st = input().split()
    string = sorted(set(st))     # split text then store and sort as a set

    for i in string:
        print("{0}:{1}".format(i,st.count(i)))

