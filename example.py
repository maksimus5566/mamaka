# id_code = input("Please enter your national ID code:")
# y = ("yes")
# n = ("no")
# if len(str(id_code)) == 11:
#    print("Your ID code is:" + id_code)
# elif len(id_code) > 11:
#    print("Code you entered is longer that 11 digits")
# else:
#    print("Code you entered is shorter that 11 digits")
# if id_code[0] == 5:
#        print("Your are male")
# elif id_code[0] == 6:
#        print("Your are female")
# while True:
#     answer = input("Do you want to continue?:")
#     if answer.lower() == "y":
#         print("ok, carry on then")
#     elif answer.lower() == "n":
#         print("Have a good day!")
#         exit()

# id_code = input("Please print your ID code for a check: ")
# if len(id_code) == 11:
#     print(id([0] * 1 + [1] * 2 + [2] * 3 + [3] * 4 + [4] * 5 + [5] * 6 + [6] * 7 + [7] * 8 + [8] * 9 + [9] * 1)// 11)
#     print(id)
user_choice = input("Please choose 1 to input your ID: \nChoose 2 to verify your ID code: \nChoose 0 to exit the program: ")
if user_choice == "2":
    id_code = input("Please enter your ID_code here: ")
elif user_choice == "0":
    print("Thank you and see you next time. ")
    exit()
elif user_choice == "2":
    id_code = input("Please enter your ID_code here: ")
    control = 1 * int(id_code[0]) + 2 * int(id_code[1]) + 3 * int(id_code[2]) + 4 * int(id_code[3]) + 5 * int(id_code[4]) + 6 * int(id_code[5]) + 7 * int(id_code[6]) + 8 * int(id_code[7]) + 9 * int(id_code[8]) + 1 * int(id_code[9])
    # print(control)
    check = control % 11
    # print(check)
    if check < 10 and check == int(id_code[-1]):
        print("Code you entered is valid! ")
    else:
        control = 3 * int(id_code[0]) + 4 * int(id_code[1]) + 5 * int(id_code[2]) + 6 * int(id_code[3]) + 7 * int(id_code[4]) + 8 * int(id_code[5]) + 9 * int(id_code[6]) + 1 * int(id_code[7]) + 2 * int(id_code[8]) + 3 * int(id_code[9])
        # print(control)
        check = control % 11
        # print(check)
        if check < 10 and check == int(id_code[-1]):
            print("Code you entered is valid!")
            if check >= 10:
                print('Your ID code control number is 0')
else:
    print("Oops, something went wrong. ")
    exit("Program stopped! Please check your ID number.")