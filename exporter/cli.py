import click


@click.group()
@click.option(
    "-p",
    "--path",
    default=None,
    type=click.Path(exists=True),
    help="An optional path to the folder to run the commands from.",
)
@click.pass_context
def cli(ctx, path):

    ctx.ensure_object(dict)
    ctx.obj["path"] = path

    return ctx


@cli.command()
@click.pass_context
def compile(ctx):
    print("compile")
    print(ctx.obj["path"])
