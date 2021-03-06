# The following lines were added by compinstall

zmodload -i zsh/complist
zstyle ':completion:*' completer _expand _complete _ignored _approximate
zstyle ':completion:*' max-errors 2
zstyle ':completion:*' menu select=2
zstyle :compinstall filename '/home/thomas/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall
# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
setopt appendhistory autocd
bindkey "OA" history-search-backward
bindkey "OB" history-search-forward
bindkey -v
# End of lines configured by zsh-newuser-install

## aliases ####
alias mv='nocorrect mv -i'
alias cp='nocorrect cp -i'
alias rm='nocorrect rm -i'
alias mkdir='nocorrect mkdir'
alias man='nocorrect man'
alias ll='ls --color=auto -lA'
alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'
alias cd..='cd ..'
alias cd/='cd /'
alias z='vim ~/.zshrc;src'
alias :q='exit'
alias please='sudo $(fc -ln -1)'
alias lstty='ls /dev/tty*'

#Enable this for a nice interactive way to get a decent prompt.
autoload -U promptinit
promptinit

autoload -U colors
colors

# prompt adam2
if [ -f ~/.zshprompt ]; then
    source ~/.zshprompt
fi

if [ -f ~/.texpaths ]; then
    source ~/.texpaths
fi

## invoke this every time when u change .zshrc to
## recompile it.
src ()
{
	autoload -U zrecompile
	[ -f ~/.zshrc ] && zrecompile -p ~/.zshrc
	[ -f ~/.zcompdump ] && zrecompile -p ~/.zcompdump
	[ -f ~/.zshrc.zwc.old ] && rm -f ~/.zshrc.zwc.old
	[ -f ~/.zcompdump.zwc.old ] && rm -f ~/.zcompdump.zwc.old
	source ~/.zshrc
}

export EDITOR=vim
function gi() { curl -L -s https://www.gitignore.io/api/$@ ;}
function mkchd() { mkdir $@; cd $@;}
export GOPATH=$HOME/workspace/go
