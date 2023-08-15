# Installation guide for XC3
This file contains step-by-step instructions for installation of XC3 project. \n

## Pre-Requirements
Following files should be pre-installed in your system

### Python V 3.9.*
Clone Python version manager in home directory
```bash
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```

Add version manager to bashrc/user profile/environment.

The example shows adding to bashrc:

Open bashrc
```bash
nano ~/.bashrc
```

Add following line to the end of file, save and exit.
```shell
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

To apply the changes, restart or 
```shell
source ~/.bashrc
```

## Terraform V1.4.6
Download and install terraform
```shell
wget https://releases.hashicorp.com/terraform/1.4.6/terraform_1.4.6_linux_amd64.zip
unzip terraform_1.4.6_linux_amd64.zip
sudo mv terraform /usr/local/bin/
```
Check version. It should be 1.4.6
```bash
terraform version
```

### AWS CLI V2.*
```shell
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64-2.11.3.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

## Cloning the Repo
```shell
git clone "your git URL"
```
