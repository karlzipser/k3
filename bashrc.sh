
alias ls='ls -alh'
alias fixScreen='DISPLAY=:0 xrandr --output HDMI-0 --mode 1024x768'
alias gacp="git add .;git commit -m 'gacp';git push origin master"
alias gacpk3='cd ~/k3; git pull; gacp; cd'
alias pgpk3='cd ~/k3; git pull; cd'
alias U3='ssh -p 1022 -XY karlzipser@169.229.219.141'
alias U='ssh -p 1022 -XY karlzipser@169.229.219.140'
alias ipy="ipython --no-banner"
alias sb='cd;source ~/.bashrc'

export PYTHONPATH=~:$PYTHONPATH
export PYTHONPATH=~/k3:$PYTHONPATH
export PATH=~/k3:$PATH
export PATH=~/k3/scripts:$PATH

git config --global credential.helper "cache --timeout=86400"

if [ "$(whoami)" != "nvidia" ]
  then
    export HISTSIZE=2000
    export HISTFILESIZE=10000
fi

PS1="\[\033[01;35m\]\w\[\033[00m\] $ "

if [ $HOSTNAME == "bdd2" ]
  then
    #PS1="\[\033[01;33m\]$HOSTNAME\w\[\033[00m\] $ "
    PS1="\[\033[01;34m\]*** $HOSTNAME *** \w\[\033[00m\] $ "
fi

if [ $HOSTNAME == "bdd3" ]
  then
    PS1="\[\033[01;32m\]*** $HOSTNAME *** \w\[\033[00m\] $ "
fi

if [ $HOSTNAME == "bdd4" ]
  then
    PS1="\[\033[01;34m\]*** $HOSTNAME *** \w\[\033[00m\] $ "
fi




#EOF
