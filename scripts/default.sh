#!/bin/bash

# Session Name
SESSION="DEV"
SESSIONEXISTS=$(tmux list-sessions | grep $SESSION)

if ["$SESSIONEXISTS" = ""]
then
  # Start new session with session name and name it "Vim"
  tmux new-session -d -s $SESSION -n Nvim
  
  # Select pane 1 and run vim with size of 90%
  tmux selectp -t 1 
  tmux send-keys "nvim ." C-m

  # Add vertical pane to vim window
  tmux splitw -v 
  tmux resize-pane -D 20
  tmux send-keys "clear" C-m

  # Split pane 2 in 2
  tmux selectp -t 2
  tmux splitw -h
  tmux send-keys "clear" C-m

  # Go back to pane 1
  tmux selectp -t 1

  # Create a new window for extras
  tmux new-window -t $SESSION:2 -n Extras

  # Go back to vim window
  tmux select-window -t $SESSION:1
fi

# Attach session on Vim window
tmux attach-session  -t $SESSION


