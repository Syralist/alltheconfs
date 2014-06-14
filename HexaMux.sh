#!/bin/bash
SESSION='hexapod'
TMUX='tmux -2'
# if the session is already running, just attach to it.
$TMUX has-session -t $SESSION
if [ $? -eq 0 ]; then
    echo "Session $SESSION already exists. Attaching."
    sleep 1
    $TMUX attach -t $SESSION
    exit 0;
fi

cd ~/hexapod
$TMUX new-session -d -s $SESSION

$TMUX split-window -h
$TMUX select-pane -t 0
$TMUX send-keys "cd hexapy" C-m
$TMUX select-pane -t 1
$TMUX send-keys "git pull" C-m
$TMUX split-window -v
$TMUX select-pane -t 0

$TMUX attach-session -t $SESSION
