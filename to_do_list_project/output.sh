#!/bin/bash
echo "alias make_todo='python3 $HOME/to_do_list_project/get_to_do.py'" >> ~/.bashrc
echo "alias ctd='cat $HOME/.todo.txt'" >> ~/.bashrc

source ~/.bashrc

