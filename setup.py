from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    # packages=find_packages()+find_packages(where="submodules"),
    packages=find_packages(where="submodules"),
    package_dir={"KDTree4RRT":"./submodules/KDTree4RRT"},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)