#!/bin/sh
#
session="Dev-Back"

# set up tmux
tmux start-server

# create a new tmux session, starting vim from a saved session in the new window
tmux new-session -d -s $session -n vim

# First window is for vim
tmux selectp -t 1 
tmux send-keys "vim ." C-m 

#Split pane 1 70%
tmux splitw -h -p 15

#Select pane 2
tmux selectp -t 2

#Split pane 2 vertically 50%
tmux splitw -v -p 50

# create a new window called Extra
tmux new-window -t $session:2 -n Extra

# return to main vim window
tmux select-window -t $session:1

# Finished setup, attach to the tmux session!
tmux attach-session -t $session
