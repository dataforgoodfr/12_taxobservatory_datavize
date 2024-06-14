# Taxplorer website for CbCR data visualization

The repository contains the source code for the
[https://www.taxplorer.eu](https://www.taxplorer.eu) Taxplorer website for
Country-By-Country Report data visualization. 

It has been developed during the 12th season of [dataforgood](https://dataforgood.fr/).

The website is deployed on
[https://www.taxplorer.eu](https://www.taxplorer.eu/). The `main` branch is the
one deployed on the production website .

The `dev` branch is deployed on the developpement website [https://dev.taxplorer.eu](https://dev.taxplorer.eu)

# Contributing

If you want to contribute a new feature, please fork the `ðev` branch and
propose a pull request. Once accepted, it will integrate the `dev` branch and
eventually be deployed on the production website once a release is created by
syncing the `main` branch with the `dev` branch.

# Local development environment

## Environment installation

For development on your machine, if you have a linux on which you have `sudo`
access, you can simply : 

```
git clone https://github.com/dataforgoodfr/12_taxobservatory_dataviz
.deploy/deploy.sh
```

This will :

- create the virtual environment in the repository
- install poetry and the project requirements
- install nginx and the definition of the website
- install a systemd service file

You will then be able to connect to the website
[http://localhost:5000](http://localhost:5000). 

If you need to restart the taipy server, you can : 

```
sudo service taxplorer.uwsgi restart
```
## Pre-commit

To run the pre-commit, follow the instructions on how to [install pre-commit](https://pre-commit.com/) and then run them with :

    pre-commit run --all-files

The pre-commit must be run before proposing a pull request, otherwise the CI/CD
will complain about your proposed feature.

