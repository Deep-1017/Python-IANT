import os

cwd = os.getcwd() 
# print("Current working directory before changing:", cwd) 

# new_dir = os.chdir("../")
# print("Current working directory after changing:", os.getcwd())


# if not os.path.exists("data"):
#     os.mkdir("data") 

# os.remove("data")

os.rename("data", "Days")
    
for i in range(0, 50):
    folder_name = f"Days/Day {i+1}"
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        
data_list = os.listdir("Days")
print(data_list)
