#!/bin/sh
#
session="Dev-Front"

# set up tmux
tmux start-server

# create a new tmux session, starting vim from a saved session in the new window
tmux new-session -d -s $session -n vim

# First window is for vim
tmux selectp -t 1 
tmux send-keys "vim ." C-m 

# create a new window called terminal
tmux new-window -t $session:2 -n terminal

# Split pane 1 horizontal by 50%, start htop
tmux splitw -h -p 50
tmux send-keys "htop" C-m 

# Select pane 2 
tmux selectp -t 2

# Split pane 2 vertiacally by 50%, start live-server
tmux splitw -v -p 50
tmux send-keys "live-server ." C-m 

# return to main vim window
tmux select-window -t $session:1

# Finished setup, attach to the tmux session!
tmux attach-session -t $session
