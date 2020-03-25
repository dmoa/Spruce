#!/usr/bin/env bash

INSTALL_PATH=$(pwd)

git_clone() {
    git clone https://github.com/dmoa/spruce
    cd spruce
}

install_dependencies() {
    pip install -r requirements.txt
}

delete_script() {
    "echo" "installation complete, deleting installation script"
    cd ..
    rm install.sh
}

if [ "$(uname)" = "Darwin" ]; then
    # Do something under Mac OS X platform
    "echo" "detected MacOS"
    git_clone
    install_dependencies
    printf "%s\n" "alias spruce='python $INSTALL_PATH'/spruce/spruce/main.py" >> ~/.zshrc
    delete_script
    zsh
elif [ "$(expr substr $(uname -s) 1 5)" = "Linux" ]; then
    # Do something under GNU/Linux platform
    "echo" "detected Linux"
    git_clone
    install_dependencies
    printf "%s\n" "alias spruce='python $INSTALL_PATH'/spruce/spruce/main.py" >> ~/.bashrc
    delete_script
    bash
elif [ "$(expr substr $(uname -s) 1 9)" = "CYGWIN_NT" ]; then
    # Do something under Windows NT platform
    "echo" "detected Windows (Cygwin)"
    git_clone
    install_dependencies
    printf "%s\n" "alias spruce='python $INSTALL_PATH'/spruce/spruce/main.py" >> ~/.bashrc
    delete_script
    bash
else
    "echo" "ERROR: could not detect platform"
    exit 0
fi

exit 0
