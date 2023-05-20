# mock_username_1="scsvv"
# mock_password_1="123"
# for i in range(3): 
#     _tmp_username=input("Enter username: ")
#     _tmp_password=input("Enter: password: ")
#     if ((mock_username_1==_tmp_username) and (mock_password_1==_tmp_password)) :
#         print("Вы вошли в аккаунт")
#         break
#     print(f"try #{i}")      
# else : 
#     print("Вам выдан бан")

mock = {
    "scsvv":"123", 
    "xawav": "124", 
    "scv": "125"
}

for i in range(3):
    username = input("Enter username: ")
    psswd = input("enter password: ")
    if username in set(mock.keys()): 
        if mock[username] == psswd:
            print("login is succsessful")
            break
    print("username or password is not correct")
    continue


