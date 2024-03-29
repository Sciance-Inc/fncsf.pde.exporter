# FNCSF.PDE.EXPORTER

> A data exporter for serverless organisations.

# How to use the Exporter

## Overview

- The _exporter_ is **command-line-tool** can be used to sync the PDE datasets with the FNCSF platform.
- The exporter will perform some data quality checks on the data to be exorted and will report any issues found.

## How to format your dataframes

- All of your dataframes schould be :
  1. In a **.CSV** file format.
  2. **comma-separated**.
  3. **UTF-8** encoded.

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

# How to run the docker

## As a docker run

```bash
docker run  -e TST_AWS_ACCESS_KEY_ID=<the AWS secret key id> -e TST_AWS_SECRET_ACCESS_KEY=<the AWS secret access key> -v <absolute path to the csvs folder>:/upload ghcr.io/sciance-inc/fncsf.pde.exporter
```

## As a docker-compose file

```bash
version: '3.9'

services:
  exporter:
    image: ghcr.io/sciance-inc/fncsf.pde.exporter
    environment:
      - TST_AWS_ACCESS_KEY_ID=<the AWS secret key id>
      - TST_AWS_SECRET_ACCESS_KEY=<the AWS secret access key>
    volumes:
      - <absolute path to the csvs folder>:/upload
```

In a docker-compose, the absolute path to the csvs folder can be replaced with a relative one, starting with `./`.
