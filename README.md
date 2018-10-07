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
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```
Open a new shell to begin using `pyenv`.

### Install Python 3.7
Install build dependencies (only needs to be done once).
```
$ sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
  libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
  xz-utils tk-dev libffi-dev liblzma-dev
```
Install Python
```
$ pyenv install 3.7.0
```
This will not impact the version of Python that was installed by your Linux distribution. This additional version of Python will be installed in your home directory.

### Clone the repository (if you haven't already)
```
$ git clone git@github.com:chriskasza/comp3753-project.git
```

### Set the Python version for the project
```
$ cd comp3753-project
$ pyenv local 3.7.0
```

### Install pipenv
Pipenv handles package management and virtual environment management per project.

*Ensure the following command is run in the `comp3753-project` directory where we are using Python v3.7.*
```
$ pip install pipenv
```

### Install the packages from the Pipfile
```
$ pipenv install
```

## Set up prod env
### install elasticsearch
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-6.x.list
sudo apt-get update && sudo apt install -y openjdk-8-jdk elasticsearch
sudo /bin/systemctl daemon-reload
sudo /bin/systemctl enable elasticsearch.service
sudo /bin/systemctl start elasticsearch.service
