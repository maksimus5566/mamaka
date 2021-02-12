condition = True
while condition:

    user_choice = input("Please choose:\n1. Check ID\n2. Choose to verify your ID code: \n0. Exit\n-->")
    #возможность для пользователя сделать выбор
    if user_choice == "1":

        condition2 = True
        while condition2:
            try:
                user_id = input("Please enter your Estonian national ID: ")
                user_id = str(int(user_id))
                if len(user_id) != 11:
                    if len(user_id) > 11:
                        print("Code you entered is longer than 11 digits")
                        raise UserWarning
                    elif len(user_id) < 11:
                        print("Code you entered is shorter than 11 digits")
                        raise UserWarning
            except ValueError:
                print("Text you entered is not numeric!")
                print("Please try again")
            except:
                print("Please try again!")
            else:
                gender_id = user_id[0]
                birth_year = user_id[1:3]
                birth_month = user_id[3:5]
                birth_day = user_id[5:7]
                birth_region = int(user_id[7:10])
                chech_num = user_id[10]
                #gender controll
                if int(gender_id) % 2 == 0:
                    gender = "Female"
                else:
                    gender = "Male"

                #century control
                if gender_id == "1" or gender_id == "2":
                    birth_cent = "18"
                elif gender_id == "3" or gender_id == "4":
                    birth_cent = "19"
                elif gender_id == "5" or gender_id == "6":
                    birth_cent = "20"

                # Region Control
                if birth_region in range(1, 10):
                    region = "Kuressaare laigla"
                elif birth_region in range(11, 20):
                    region = "Tartu Ülikooli Naistekliinik"
                elif birth_region in range(21, 151):
                    region = "Ida-Tallinna Keskhaigla"
                else:
                    region = "unknown region"

                print("Your national ID number is: " + user_id)
                print("You are:" + gender)
                print("Your date of birth is " + birth_day + "." + birth_month + "." + birth_cent + birth_year)
                print("You were born in: " + region)
                condition2 = False
##########################################################################################
        condition3 = True
        while condition3:
            try:
                if user_choice == "2":
                    id_code = input("Please enter your ID_code here: ")
                elif user_choice == "0":
                    print("Thank you and see you next time. ")
                    exit()
                elif user_choice == "2":
                    id_code = input("Please enter your ID_code here: ")
                    control = 1 * int(id_code[0]) + 2 * int(id_code[1]) + 3 * int(id_code[2]) + 4 * int(
                        id_code[3]) + 5 * int(id_code[4]) + 6 * int(id_code[5]) + 7 * int(id_code[6]) + 8 * int(
                        id_code[7]) + 9 * int(id_code[8]) + 1 * int(id_code[9])
                    # print(control)
                    check = control % 11
                    # print(check)
                    if check < 10 and check == int(id_code[-1]):
                        print("Code you entered is valid! ")
                    else:
                        control = 3 * int(id_code[0]) + 4 * int(id_code[1]) + 5 * int(id_code[2]) + 6 * int(
                            id_code[3]) + 7 * int(id_code[4]) + 8 * int(id_code[5]) + 9 * int(id_code[6]) + 1 * int(
                            id_code[7]) + 2 * int(id_code[8]) + 3 * int(id_code[9])
                        # print(control)
                        check = control % 11
                        # print(check)
                        if check < 10 and check == int(id_code[-1]):
                            print("Code you entered is valid!")
                            if check >= 10:
                                print('Your ID code control number is 0')
                    condition3 = True
                else:
                    print("Oops, something went wrong. ")
                    quit("Program stopped! Please check your ID number.")
##########################################################################################
    if user_choice == "2":
        id_code = input("Please enter your ID_code here: ")
    elif user_choice == "0":
        print("Thank you and see you next time. ")
        exit()
    elif user_choice == "2":
        id_code = input("Please enter your ID_code here: ")
        control = 1 * int(id_code[0]) + 2 * int(id_code[1]) + 3 * int(id_code[2]) + 4 * int(id_code[3]) + 5 * int(
            id_code[4]) + 6 * int(id_code[5]) + 7 * int(id_code[6]) + 8 * int(id_code[7]) + 9 * int(
            id_code[8]) + 1 * int(id_code[9])
        # print(control)
        check = control % 11
        # print(check)
        if check < 10 and check == int(id_code[-1]):
            print("Code you entered is valid! ")
        else:
            control = 3 * int(id_code[0]) + 4 * int(id_code[1]) + 5 * int(id_code[2]) + 6 * int(id_code[3]) + 7 * int(
                id_code[4]) + 8 * int(id_code[5]) + 9 * int(id_code[6]) + 1 * int(id_code[7]) + 2 * int(
                id_code[8]) + 3 * int(id_code[9])
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

    if user_choice == "0":
        print("Program has finished working.")
        exit() #если написать в скобках сообзение, оно выведет ошибку как1, но она не влияет ниначто
    else:
        print("Choice is out of range.")

#что такое while
# counter = 0
# while counter < 100:
#     print("I can't stop!!! " + str(counter) + " times")
#     counter += 1

######   WHYLE   #######
# condition = True
# counter = 4

# while condition and counter > 0:
#     user_input = input("Please enter your id code: ")
#     if len(user_input) != 11:
#         if counter != 0:
#             print("Please try again")
#         counter -= 1
#     else:
#         print(user_input)
#         condition = False
#     if counter == 0:
#         print("Please, try latter")



# cond = True
# while cond:
#
#     user_input = input("Please enter your id code: ")
#     if len(user_input) != 11:
#         print("Error, try again")
#         continue
#     else:
#         print(user_input)
#         cond = False
#     print("Hello")

# user_id = input("Please enter your ID: ")
# try:
#     user_id = int(user_id)
#     if len(user_id) != 11:
#         raise UserWarning
# except TypeError:
#     print("ERROR")
# except UserWarning:
#     print("Not 11 digits long")
# except:
#     print("The code you entered is not numbers")
# else:
#     print(user_id)
# finally:
#     print("Program stopped working")