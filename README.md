# Getting Started
Once this repo is cloned, create a conda environment with all of the required packages using:
```
conda create --name <name_of_environment> --file spec-file.txt
```
Activate the environment by writing:
```
conda activate <name_of_environment>
```

To update the list of packages if needed, use:
```
conda list --explicit > spec-file.txt
```

# Developing and Running the server locally
To start up the dev server locally (with live reload), run:
```
FLASK_APP=flaskr FLASK_ENV=development flask run
```
