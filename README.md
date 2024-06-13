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

TBD

## Pre-commit

To run the pre-commit, follow the instructions on how to [install pre-commit](https://pre-commit.com/) and then run them with :

    pre-commit run --all-files

The pre-commit must be run before proposing a pull request, otherwise the CI/CD
will complain about your proposed feature.

## Deployment

We deploy two websites. One for production and one for development. In both
cases, the process is the same, the only difference being the branch being used
to run the server.

Deploying a website involves : 

- cloning the repository and setting up the virtual environment,
- configuring nginx with a base setup listening on port 80 and then adding https
  support with a SSL certificate
- wrapping the start/stop of the taipy server with a systemd service

### Cloning and virtual environment

First clone the repository :

```
cd /opt/d4g
git clone https://github.com/dataforgoodfr/12_taxobservatory_dataviz.git
cd 12_taxobservatory_dataviz
```

If you want to deploy the development website, you must checkout the `dev`
branch. If you want to deploy the production website, you must checkout the
`main` branch. 

```
git checkout dev   # For development website
git checkout main  # For production website
```

You can then create a local virtual environment, install poetry as well as the
project dependencies :
```
. ./d4g-utils/install_poetry.sh
```

We need some extra packages for the deployment :

```
source .venv/bin/activate
pip install uwsgi gevent
```

### Nginx setup

TBD

### Systemd service file

TBD

