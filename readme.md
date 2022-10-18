# FNCSF.PDE.EXPORTER
> A data exporter for serverless organisations.

# How to use the Exporter

## Overview

* The *exporter* is **command-line-tool** can be used to sync the PDE datasets with the FNCSF platform. 
* The exporter will perform some data quality checks on the data to be exorted and will report any issues found.

# How to contribute to the Exporter code base

1. Git clone the repository
2. Init a *git flow* feature/bugfix branch
```bash
git flow init <feature|bugfix> <feature_name>
```
3. Start the *poetry shell*
```
poetry shell
poetry install
```
4. Make your changes
5. Submit a pull request