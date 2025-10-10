# Chapter 5: Input/Output

## Key concepts
- Flags are options that you can pass to a command to change its behavior.
    For example, the ls command can take a -l flag to show a "long" listing of files:
    ls -l

    Or the -a flag to show "all" files, including hidden files:
    ls -a

    You can also combine flags:
    ls -al

- Help 
    Examples
    curl --help
    curl -h
    curl -help
    curl --help all
    curl -h all


## Common commands
- man 

    Command will only work for programs that it has a manual for
    Type '/-r' to start searching
    Press 'n' to jump to the next result
    Press 'N' to go back if you went too far

- echo "Hello world"
   Hello world

- top

    q → quit
    k → kill a process
    r → renice (change priority)

## Notes

- Positional Arguments
    In a shell, commands (programs) can also take arguments. For example, the cd command takes a single argument (the directory to change to):

    cd /home/wagslane

    Other commands might take multiple arguments. For example, the mv command takes two arguments: the file to move, and the destination to move it to:

    mv file.txt dest/file.txt

- "Standard Output", usually called "standard out" or "stdout", is the default place where programs print their output

- "Standard Error", usually called "stderr", is a data stream just like standard output, but is intended to be used for error messages.

- top command is a powerful tool that allows you to see which programs are using the most resources on your computer