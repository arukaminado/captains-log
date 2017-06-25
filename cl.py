import os, sys, datetime

def main():
#this is so the user will always enter their name if logs do not exit
    if(not os.path.isfile("entries.log")):
            print("Please enter your name")
#reading, storing, writing and pretty printing
            cl_name = raw_input("Name: ")
            cl_logfile = open("entries.log", "w")
            cl_logfile.write("<< Excerpt from Personal Archives >>")
            cl_logfile.write("\n<< Personal Log, "+ cl_name + " >>\n\n")
#closing the file and exiting happily
            file.close(cl_logfile)
            sys.exit(0)
#if logs do exist, send the user to the main menu
    elif(os.path.isfile("entries.log")):
        print("a) - append a new log")
        print("v) - view logfile")
        cl_menu = raw_input("Select: ")
        if (cl_menu == 'a'):
#reading, storing, writing and pretty-printing
            cl_logentry = raw_input("Log Entry: ")
            cl_logfile = open("entries.log", "a")
            cl_logfile.write("[[CE 00.00.00]]\n\n")
            cl_logfile.write(cl_logentry + "\n\n")
#closing the file and exiting.  Happy py!
            file.close(cl_logfile)
            sys.exit(0)
        elif (cl_menu == 'v'):
            cl_logfile = open("entries.log", "r")
            file.close(cl_logfile)
            sys.exit(0)
#entry point for the program, takes user straight to main
if __name__ == "__main__":
    main()
