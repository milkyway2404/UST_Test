with open("C:/Miguel/UST_Repository/UST_pythonProject/Inputs/program1.txt", 'r') as f:
    data = f.read()
    print(data)

#Write a program to compute the frequency of the words from the input.
#The output should output after sorting the key alphanumerically.
#○ Eg - line = “which is better python 2 or python 3”
def program1():
    #st = input().split()
    st = data.split()
    string = sorted(set(st))     # split text then store and sort as a set

    for i in string:
        print("{0}:{1}".format(i,st.count(i)))

program1()



