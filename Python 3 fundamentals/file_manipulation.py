import os
original_lacation=os.path.join(os.path.dirname(os.path.abspath(__file__)),"here")
print(original_lacation)
destination_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)),"there")
if not os.path.exists(destination_folder):
    os.mkdir(destination_folder)
for entry in os.scandir(original_lacation):
    org_loc=os.path.join(original_lacation,entry.name)
    des_loc=os.path.join(destination_folder,entry.name)
    if entry.is_file():
        os.rename(org_loc,des_loc)

