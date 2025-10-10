# Chapter 4: Programs

## Key concepts

- Compiled programs

    A compiled program is a program that has been converted from human-readable source code into machine code (binary)
    Examples:
    - C, C++, Go  
    - Compilation done via `gcc`, `go build`, etc.  
    - Produces an executable file (e.g. `a.out`, `main`)

- Interpreted programs

    An interpreted program is a program that is executed by another program
    Examples:
    - Python, Bash, JavaScript  
    - Runs with `python script.py` or `bash script.sh`

- Shebang
    #! interpreter [optional-arg]
    #!/usr/bin/python3
    A special line at the top of a script that tells your shell which program to use to execute the file


## Common commands

- ls -a ~

    List all files (including hidden ones) in your home directory

- nano ~/.bashrc

    A simple, user-friendly text editor that runs right in your terminal. When you type nano ~/.bashrc, it opens the .bashrc file (which is a hidden configuration file for your Bash shell, located in your home directory ~) directly within the nano editor. This allows you to add or remove lines of code to customize your shell environment.

## Notes

- PATH

    echo $PATH
    /usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin

    Your shell will look for executables in the following directories:
    /usr/local/bin
    /usr/bin
    /bin
    /usr/sbin
    /sbin