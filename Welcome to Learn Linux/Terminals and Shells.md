# Chapter 1: Terminals and Shells

## Key concepts

- Create a variable

        name = "Lane"
        echo $name

- Interpolate a variable in a string

        $ echo $name
        # prints: Lane

## Common commands

- history

    Print out the history of commands you've typed in your shell.

- clear (Ctrl+L)

    Clears the terminal.

## Notes

- CLI = Command Line Interface
- GUI = Graphical User Interface

    Note: GUI can be easier for beginners, but a CLI is often more powerful, automatable, and scriptable.

- Install WSL 2 (Windows Subsystem for Linux) on Windows to run a native Linux userland.

- Terminal emulator

    A terminal emulator is a program that emulates a physical terminal. It displays a command-line interface and passes your input to a shell. Examples: Ghostty, Alacritty, Windows Terminal.

- Shells

    Shells interpret the commands you type and execute them. Many shells provide additional features like scripting, tab completion, and customization.

- REPL

    Shells are often referred to as "REPL"s. REPL stands for:

    - Read
    - Eval (evaluate)
    - Print
    - Loop

- Terminal vs distribution

    Ubuntu is not a terminal emulator; it is a Linux distribution (an operating system).