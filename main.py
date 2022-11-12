import os
import time

def process():
    global linecount
    while True:
        lines_input = str(input(">> "))
        lines = lines_input + "\n"
        if lines == "exit-editor\n":
            break
        else:
            fo.seek(0)
            fo.writelines(lines)
        
if __name__ == "__main__":
    print("Welcome to Python-Notepad! Made with <3 by WilliamAfton-codes\n")
    
    filename_input = str(input("What would you like the file to be called?: "))
    ext_input = str(input("What would you like the extension to be? (Don't type the '.'): "))
    filename = filename_input + "." + ext_input
    fo = open(filename, "a")
    
    print("Loading text editor...")
    time.sleep(1)
    print("\nType 'exit-editor' to stop writing.")
    process()