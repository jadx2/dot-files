#!/bin/bash

# Session Name
SESSION="Default"
SESSIONEXISTS=$(tmux list-sessions | grep $SESSION)

if ["$SESSIONEXISTS" = ""]
then
  # Start new session with session name and name it "Vim"
  tmux new-session -d -s $SESSION -n Vim
  
  # Select pane 1 and run vim with size of 90%
  tmux selectp -t 1 
  tmux send-keys "vim ." C-m

  # Add vertical pane to vim window
  tmux splitw -v 
  tmux resize-pane -D 20
  tmux send-keys "clear" C-m

  # Split pane 2 in 2
  tmux selectp -t 2
  tmux splitw -h
  tmux resize-pane -x 50
  tmux send-keys "clear" C-m

  # Split pane 3 in 2
  tmux selectp -t 3
  tmux splitw -h
  tmux send-keys "clear" C-m

  # Go back to pane 1
  tmux selectp -t 1

  # Create a new window for utils
  tmux new-window -t $SESSION:2 -n Utils

  # Split window Utils in 2
  tmux splitw -h -p 25
  tmux clock-mode

  # Split pane htop
  tmux selectp -t 2
  tmux splitw -v
  tmux send-keys "htop" C-m

  # Create a new window for IRC
  tmux new-window -t $SESSION:3 -n IRC

  # Go back to window Vim
  tmux select-window -t $SESSION:1
fi

# Attach session on Vim window
tmux attach-session  -t $SESSION


