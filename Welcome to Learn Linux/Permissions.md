# Chapter 3: Permissions

## Key concepts
- sudo chown -R root contacts

    Here's an explanation of the command:
    sudo - Run as the root user
    chown - Command to change the owner
    -R - "Recursive", meaning also apply the changes to everything inside the directory
    root - The name of the new owner
    contacts - The directory to change the owner of


## Common commands

- sudo 

    Run a command as a "superuser"

- chmod

    Update permissions
    chmod -R u=rwx,g=---,o=--- .



## Notes
- Permission access

    drwxrwxrwx

    Let's break down each character. The first one just tells you whether you're looking at a file or a directory:
    -: Regular file (e.g. -rwxrwxrwx)
    d: Directory (e.g. drwxrwxrwx)
    The next 9 characters are broken up into 3 sets of rwx and represent the permissions themselves for the "owner", "group", and "others", in order. Each group of 3 represents the permissions for reading, writing, and executing, in order. So, for example:

    rwx: All permissions
    rw-: Read and write, but not execute
    r-x: Read and execute, but not write

    The first 3 characters are "owner" permissions
    The next 3 characters are "group" permissions
    The last 3 characters are "others" permissions

    -rwxrwxrwx: A file where everyone can do everything
    -rwxr-xr-x: A file where everyone can read and execute, but only the owner can write
    drwxr-xr-x: A directory where everyone can read (ls the contents) and execute (cd into it), but only the owner can write (modify the contents)
    drwx------: A directory where only the owner can read, write and execute

- root

    superuser that has access to everything
