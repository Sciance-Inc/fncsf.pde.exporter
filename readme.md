# FNCSF.PDE.EXPORTER

# User's guide
> A data exporter for serverless organisations.

# How to use the Exporter

## Overview

- The _exporter_ is **command-line-tool** can be used to sync the PDE datasets with the FNCSF platform.
- The easiest way to use the _exporter_ is to run it in a **docker container**. Make sure you have `docker` installed on your machine.
- The exporter will perform some data quality checks on the data to be exorted and will report any issues found.

## How to format your dataframes

- All of your dataframes schould be :
  1. In a **.CSV** file format.
  2. **comma-separated**.
  3. **UTF-8** encoded.

# How to run the docker

## As a docker run
* The <variable_name> define a variable, just replace <variable_name> with the value you want to use. Do not include the angle brackets.

```bash
docker run -e PDE_AWS_ACCESS_KEY_ID=<the AWS secret key id> -e PDE_AWS_SECRET_ACCESS_KEY=<the AWS secret access key> -v <absolute path to the csvs folder>:/upload ghcr.io/sciance-inc/fncsf.pde.exporter:master
```

If your csv files are in a folder named 'exemple', you can directly run the docker with the following command :
(note that `cd` is used to change the working directory to the folder where the CSV files are located)

```bash
cd /path/to/your/csv/folder
docker run -e PDE_AWS_ACCESS_KEY_ID=<the AWS secret key id> -e PDE_AWS_SECRET_ACCESS_KEY=<the AWS secret access key> -v .:/upload ghcr.io/sciance-inc/fncsf.pde.exporter:master
```

## As a docker-compose file

```bash
version: '3.9'

services:
  exporter:
    image: ghcr.io/sciance-inc/fncsf.pde.exporter:master
    environment:
      - PDE_AWS_ACCESS_KEY_ID=<the AWS secret key id>
      - PDE_AWS_SECRET_ACCESS_KEY=<the AWS secret access key>
    volumes:
      - <absolute path to the csvs folder>:/upload
```

In a docker-compose, the absolute path to the csvs folder can be replaced with a relative one, starting with `./`.

# Troobleshooting 

## Launching the tool
* permission issue roblem
  * If you get a permission issue when running the docker, try to run the docker with `sudo` or change the permissions of the folder where the CSV files are stored : 
    * `sudo docker run .....`

## File validation
* E023 : One of the file is missing a column. The name of the missing column is in the (middle) of the error message.
  
## Developper guide


# How to contribute to the Exporter code base

1. Git clone the repository
2. Init a _git flow_ feature/bugfix branch

```bash
git flow init <feature|bugfix> <feature_name>
```

3. Start the _poetry shell_

```
poetry shell
poetry install
```

4. Make your changes
5. Submit a pull request

# How to build the docker

> We recommend PULLING the docker instead of building it.

```bash
docker build -t fncsf_pde_exporter -f docker/Dockerfile .
```

# How to pull the docker

```bash
docker pull ghcr.io/sciance-inc/fncsf.pde.exporter:master
```


