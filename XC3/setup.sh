echo "Checking Pre requirements"

py=$(python --version)
aws=$(aws --version)
terraform=$(terraform --version)

echo $py | grep -o '[0-9]'
echo $aws
echo $terraform

if [ "$py" = "Python 3.9.17" ]; then
  echo "python installed"
else
  echo "Python not found. Installing python"
  if pyenv --version; then
    echo "version manager found"
  else
     echo "Installing python version manager"
     git clone https://github.com/pyenv/pyenv.git ~/.pyenv
    # shellcheck disable=SC2016
    echo 'export PYENV_ROOT="$HOME/.pyenv"
    command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
    eval "$(pyenv init -)' >> ~/.bashrc
    source ~/.bashrc
  fi
  pyenv install 3.9.17
  pyenv global 3.9.17
  echo "Python version 3.9.17 installed successfully"
fi

#if [ "$terra" = ]