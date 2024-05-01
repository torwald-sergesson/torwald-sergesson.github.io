---
title: ZSH config files
slug: zsh-configs 
categories:
- Dev
tags:
- shell
- linux
- zsh
- config
---

```
# Path to your oh-my-zsh installation.
export ZSH=$HOME/.oh-my-zsh

# Set name of the theme to load.
# Look in ~/.oh-my-zsh/themes/
# Optionally, if you set this to "random", it'll load a random theme each
# time that oh-my-zsh is loaded.
#ZSH_THEME="robbyrussell"
ZSH_THEME="candy"
#ZSH_THEME="crunch"

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# The optional three formats: "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load? (plugins can be found in ~/.oh-my-zsh/plugins/*)
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git)

source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# ssh
# export SSH_KEY_PATH="~/.ssh/dsa_id"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"
#
export LS_COLORS=''
export EDITOR='vim'
export TERMINAL='urxvt256c-ml'
export GOPATH='/home/user/distfiles/goos'
export GOROOT='/usr/local/go'
# pyenv
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PATH:$PYENV_ROOT/bin:$GOPATH/bin:/home/user/distfiles/src.bin/apache-maven-3.5.0/bin"
#eval "$(pyenv init -)"
#eval "$(pyenv virtualenv-init -)"
export IGNITE_HOME='/home/user/distfiles/src.bin/ignite/apache-mirror.rbc.ru/pub/apache/ignite/1.8.0/apache-ignite-fabric-1.8.0-bin'
export JAVA_HOME='/usr/lib/jvm/java-8-openjdk-amd64'
export CATALINA_HOME='/home/user/distfiles/src.bin/apache-tomcat-7.0.75'
export KAFKA_HOME=/home/user/distfiles/src.bin/kafka_2.11-0.10.1.0/
export PATH=$HOME/bin:/usr/sbin:/sbin:/usr/local/bin:$KAFKA_HOME/bin:$GOROOT/bin:$PATH

alias gdbpd='gdb python_debug'

# Proxy
export http_proxy=""
export https_proxy=$http_proxy

# aliases
alias cat='pygmentize -g'
alias mc='mc -b'
alias ddg='w3m https://duckduckgo.com'
alias inosmi='w3m http://inosmi.ru'
alias mirror='w3m http://mirror.yandex.ru'
alias minix='w3m http://www.minix3.org'
alias erldoc='w3m /usr/lib/erlang/doc/index.html'
alias github='w3m https://github.com'
alias apache='w3m http://apache-mirror.rbc.ru/pub/apache'
alias gcc='colorgcc'
alias cc='colorgcc'
#alias g++='colorg++'
alias gdb='gdb -q'
alias h='history'
alias z='zathura'
alias up='sudo apt-get update; sudo apt-get upgrade'
alias vi='vim'
alias emacs='emacs -nw'
alias pdf='mupdf'
alias gh='w3m https://github.com'
alias tpb='w3m https://piratebay.to'
alias mcm='make clean; make'
alias lor='w3m http://linux.org.ru'
```
