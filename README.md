# SRAMPS
A place to discuss findings and learning outcomes of XC3 project.
## Contributing members
Simon Dahal ()\
Raju Dahal (104055570@student.swin.edu.au, dahalraju55@gmail.com)\
Auninda Alam (103158504@student.swin.edu.au, simonsd054@gmail.com)\
Marzan Tahreen ()\
Prakriti Neupane ()\
Sujan ()

## Naming Convention
The project was named SRAMPS by taking the initials of each of the contributing members.

## Objective
This repo will not be a full-fledged project but a collection of smaller individual code snippets/projects to demonstrate findings and rearning outcomes.

## Setup
### Clone the repo
```shell
$ git clone https://github.com/TIP-2023S2/SRAMPS.git
```
### Create virtual working environment
```shell
$ python3 -m venv venv #Linux
$ python -m venv venv #Windows
```

### Activate Virtual Environment
```shell
$ source venv/bin/activate #Linux
$ cd venv/Scripts/activate.ps1 #Windows
```

#### Note: If you have issue activating venv on windows because of execution policy settings:
```shell
$ Set-ExecutionPolicy Unrestricted -Scope Process #Will resolve for the current session
$ Set-ExecutionPolicy Unrestricted -Force #To permanently set execution policy to unrestricted
```

### Usage
Create a different directory for each individual component. If updating findings on previous components, update in the previously created directory.