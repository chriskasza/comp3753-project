# comp3753-project
Final project for COMP 3753. A sentiment analysis tool to predict USA midterm election results using Twitter and Elasticsearch

## Setting up a dev environment
[Nice blog about managing Python environments](https://jacobian.org/writing/python-environment-2018/)

### Install pyenv
`Pyenv` is a tool that allows you to maintain several different Python versions at once. 

To install, use the easy installer script from https://github.com/pyenv/pyenv-installer.
```
$ curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
```
Edit your shell rc file (e.g. `~/.bashrc`, `~/.zshrc`) and add the following lines:
```
export PATH="/home/kasza/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```
Open a new shell to begin using `pyenv`.

### Install Python 3.7
Install build dependencies (only needs to be done once).
```
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev
```
Install Python
```
pyenv install 3.7.0
```

### Clone the repository (if you haven't already)
```
git clone git@github.com:chriskasza/comp3753-project.git
```

### Set the Python version for the project
```
cd comp3753-project
pyenv local 3.7.0
```

### Install the packages in the Pipfile
```
pipenv install
```
