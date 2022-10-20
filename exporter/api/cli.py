#! /usr/bin/python3
#
# cli.py
#
# Project name: fncsf.pde.exporter.
# Author: Hugo Juhel
#
# description:
"""
Centralize errors for the statisfactory package
"""

#############################################################################
#                                 Packages                                  #
#############################################################################

from pathlib import Path

import click

# Project related packages
from exporter.api.credentials import store_credentials
from exporter.interactor.uploader import upload

#############################################################################
#                                Constants                                  #
#############################################################################


@click.group
def cli():
    pass


@cli.command()
@click.option("--access_key", type=click.STRING, prompt="The ACCESS key")
@click.option("--secret_key", type=click.STRING, prompt="The SECRET key")
def configure(access_key: str, secret_key: str):
    """
    Configure the data exporter.
    If existing, the credentials will be overidded

    Args:
        access_key (str): The access key you have been provided with.
        secret_key (str): The secret key associated to your access key.
    """

    store_credentials(access_key=access_key, secret_key=secret_key)


@cli.command()
@click.argument("path", type=click.Path(exists=True))
def export(path: Path):
    """
    Sync the datasets with the FNCSF's platform

    Args:
        path (Path): The path the .csvs are located
    """

    path = Path(path)
    upload(path)
