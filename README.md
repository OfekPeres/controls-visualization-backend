# Getting Started
Clone this repo using the recursive strategy because it has submodules
```
git clone --recursive <url>
```
Once this repo is cloned, create a conda environment with all of the required packages using:
```
conda create --name <name_of_environment>
i.e.
conda create --name <controls-backend>

```
Activate the environment by writing:
```
conda activate <name_of_environment>
```

Install all of the python packages required by writing the following 2 lines
```
conda install pip
pip install -r requirements.txt
```

# Developing and Running the server locally
To start up the dev server locally (with live reload), run:
```
FLASK_APP=flaskr FLASK_ENV=development flask run
```

# Useful Commands
If you need to update a git submodule, run:
```
git submodule update --recursive --init --remote --merge
```