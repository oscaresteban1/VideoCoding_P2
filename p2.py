from os import system, rename, path

# input a file path and check if it exists
def open_file():
    file = input()
    while not path.exists(file):
        print("this file does not exist. Please try again")
        file = input()
    return file

# check if the input and output file paths have the same name
def return_output(file):
    output = input()
    while file == output:
        print("choose a new name!")
        output = input()
    return output

def choose_exercise():
    stop = False

    while stop is False:
        print("choose an option 1 to 4 or 0 to exit:")
        option = input()

        if option == "1":
            # ex1: extract metadata and save it as a .txt
            system("ffmpeg -i BBB.mp4 -f ffmetadata BBB_metadata.txt")
            f = open("BBB_metadata.txt", "r")
            print("\nmetadata text:")
            print(f.read())

        elif option == "2":
            # ex2: rename a file
            print("file name: ")
            file = open_file()
            print("new name: ")
            newname = return_output(file)

            rename(file, newname)
            print("successfully renamed!")

        elif option == "3":
            # ex3: resize any video input
            print("file name: ")
            file = open_file()
            print("Resolution as M:N: ")
            new_resolution = input()
            print("output filename: ")
            output = return_output(file)

            command = "ffmpeg -i " + file + " -vf scale=" + new_resolution + " " + output
            system(command)
            print("successfully resized!")

        elif option == "4":
            # ex4: output video with another codec
            print("file name: ")
            file = open_file()
            print("codec to use (make sure you write it properly): ")
            codec = input()
            print("new file name: ")
            output = return_output(file)

            command = "ffmpeg -i " + file + " -c:a " + codec + " " + output
            system(command)
            print("done!")

        elif option == "0":
            stop = True

        else:
            print("please choose a valid option!")


# ex5: select exercise
choose_exercise()
