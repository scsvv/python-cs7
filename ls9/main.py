import os

# Function - OOP | GUI | WEB API + OPEN AI (TELEGRAM BOT) |  

# Declare Function 
# def remove_dir(path):
#     if os.path.exists(path):
#         for root, dirs, files in os.walk(path, topdown=True):
#             for name in files:
#                 os.remove(os.path.join(root, name))
#             for name in dirs:
#                 os.rmdir(os.path.join(root, name))
#         os.rmdir(path)
#         print("Success")
#     else: 
#         print("error 1")
# remove_dir("D:\Schools/Python_scripts/python-cs7/asdf")

def test1(A = None, B = None, C = None, **kwargs):
    print(A, B, C, kwargs)

def test2(*args):
    print(args)

test1(C=12, D=12, E=23, F=44)
test2(1,2,3,4,5,6,7,8,9)