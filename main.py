import os
import os.path
import time

def process():
    global linecount
    while True:
        lines_input = str(input(">> "))
        lines = lines_input + "\n"
        if lines == "exit-editor\n":
            break
        else:
            fo.writelines(lines)
        
if __name__ == "__main__":
    print("Welcome to Python-Notepad! Made with <3 by WilliamAfton-codes\n")
    
    filename_input = str(input("What would you like the file to be called?: "))
    print("Don't type the '.' in the extension")
    ext_input = str(input("What would you like the extension to be? (Leave blank to default to .txt): "))
    if ext_input == "":
        ext_input = "txt"
    else:
        pass
    filename = filename_input + "." + ext_input
    
    file_exists = os.path.exists(filename)
    if file_exists == True:
        print("A file with this name in this directory already exists, Python-Notepad will add text to the end")
    
    fo = open(filename, "a")
    
    print("Loading text editor...")
    time.sleep(1)
    print("\nType 'exit-editor' to stop writing.")
    process()
