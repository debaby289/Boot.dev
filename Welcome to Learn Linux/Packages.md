# Chapter 6: Packages

## Key concepts

- Advanced Package Tool (APT) is the primary package manager for Ubuntu
    apt --version


## Common commands

| Command                | Description                                          | Example                   |
| ---------------------- | ---------------------------------------------------- | ------------------------- |
| `apt update`           | Updates the list of available packages               | `sudo apt update`         |
| `apt upgrade`          | Upgrades installed packages to their latest versions | `sudo apt upgrade`        |
| `apt install`          | Installs a new package                               | `sudo apt install neovim` |
| `apt remove`           | Removes an installed package                         | `sudo apt remove neovim`  |
| `apt search`           | Searches for a package by name or keyword            | `apt search neovim`       |
| `apt show`             | Displays detailed information about a package        | `apt show neovim`         |
| `apt list --installed` | Lists all installed packages                         | `apt list --installed`    |

## Notes
- WSL/Ubuntu Instructions
    First, make sure that apt itself is up to date and will install the latest version of Neovim. Run the following command:
    sudo apt update
    This command only upgrades apt, it doesn't upgrade anything else.

    Next, install Neovim:
    sudo apt install neovim

    Check Installation
    Let's make sure we installed it properly. Check your version:
    nvim --version