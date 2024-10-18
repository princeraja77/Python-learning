import os
import shutil

original_folder="/workspaces/Python-learning/Python 3 fundamentals/here"
destination_folder="/workspaces/Python-learning/Python 3 fundamentals/there"
file_format={
    "Image":[".jpg",".png",".gif"],
    "Documents":[".pdf",".doc",".txt"],
    "Archives":[".rar",".zip"]
}
for entry in os.scandir(original_folder):
    org_path=os.path.join(original_folder,entry.name)
    frmt=os.path.splitext(entry.name)[1]
    for folder in file_format:
        if frmt in file_format[folder]:
            des_fol=os.path.join(destination_folder,folder)
            if not os.path.exists(des_fol):
                os.mkdir(des_fol)
            des_path=os.path.join(des_fol,entry.name)
            shutil.move(org_path,des_path)

    


