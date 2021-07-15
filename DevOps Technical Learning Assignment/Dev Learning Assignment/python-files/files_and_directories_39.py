from pathlib import Path

# absolute path starting from the root of directory
# c:\program files\microsoft
# mac > /user/local/bin
# path = Path(
#     "ecommerce_package"
# )  # if you dont pass an argument, it will reference the current directory.
# print(path.exists())
# path.mkdir("emails") #makes a directory
# path.rmdir("emails") #removes a directory

path = Path()
for file in path.glob("*"):
    print(file)
# iterate over all spreadsheets in a directory. this method serach for files and driectories in the current path. pass a string that defines a search pattern. * means everything. optionally add an extension *.*... *.* gives us files only no directories... *.py


# relative path starting from the current directory.
