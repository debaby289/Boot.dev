# Chapter 2: Filesystems

## Key concepts

root
  └── Users
        └── wagslane

- pwd: "/Users/wagslane"
- "/" represents the root directory 
- "Users" is the name of the directory inside the root directory
- "wagslane" is the name of a directory inside the Users directory

vehicles
├── cars
│   ├── fords
│   │   ├── mustang.txt
│   │   └── focus.txt

- When inside the top-level vehicles directory, the relative path to the mustang.txt file is: cars/fords/mustang.txt
- Absolute path to the mustang.txt file is: /vehicles/cars/fords/mustang.txt

- Grep
    
    You might be used to nice graphical interfaces that allow you to search for text in files, usually with ctrl+f or cmd+f

    You can also search multiple files at once. For example, if we wanted to search for the word "hello" in hello.txt and hello2.txt, we could run:
    grep "hello" hello.txt hello2.txt

    Recursive Search
    You can also search an entire directory, including all subdirectories:
    grep -r "hello" .

- Find

    Command is a powerful tool for finding files and directories by name

## Common commands

- pwd

    Print working directory
- cd

    Changes directory

- cd ..

    Goes back to the parent directory

- ls 

    List the contents of the directory

- cat

    View the contents of a file

- head

    Head command prints the first n(lines of a file) where n is a number you specify
    head -n 10 file1.txt

- tail
    Tail command prints the last n(lines of a file) where n is a number you specify
    tail -n 10 file1.txt

- more

    Displays file contents one screen at a time.

- less 

    Display the contents of a file in a terminal

- touch 

    Command updates the access and modification timestamps of a file
    Create multiple files at once by listing them

- mkdir

    Creates a new directory inside the current directory

- move

    Renaming a file:
    mv some_file.txt some_other_name.txt

    Moving a file from the current directory to another nested directory:
    mv some_file.txt some_directory/some_file.txt

    Moving a file from the current directory, to the parent directory:
    mv some_file.txt ../some_file.txt

    If you don't want to rename the file and you're just moving it to a different directory, you can omit the filename:
    mv some_file.txt some_directory/

- rm 

    The remove command deletes a file or empty directory:
    rm some_file.txt

    You can optionally add a -r flag to tell the rm command to delete a directory and all of its contents recursively. "Recursively" is just a fancy way of saying "do it again on all of the subdirectories and their contents".
    rm -r some_directory

- cp

    The copy command does what you would (hopefully) expect: it copies a file from one location to another.
    cp source_file.txt destination/

    You can also copy a directory and all of its contents recursively by adding the -R flag:
    cp -R my_dir new_dir

- cd ~

    An alias for your home directory

- grep 

    Allows you to search for text in files

- find

    The find command is a powerful tool for finding files and directories by name, not by their contents.

    Find a File by Name
    Let's say you're looking for a file named hello.txt somewhere in your home directory. You can use the find command to search for exactly that title:

    find some_directory -name hello.txt

    Pattern Search
    The find command can also search for files that match a pattern. For example, if you wanted to find all files that end in .txt, you could run:

    find some_directory -name "*.txt"

    The * character is a wildcard that matches anything. If you're trying to find filenames that contain a specific word, you can use the * character to match the rest of the filename:

    Find all filenames that contain the word "chad"
    find some_directory -name "*chad*"

## Notes

- Directories (Folders on windows) containers that hold files or directories
- Files are a dump of raw binary data (0s & 1s)
- Relative filepaths which are paths that take your current directory into account
- Absolute path is a path that starts at the root of the filesystem
- A user's home directory is the directory where their personal files are stored 