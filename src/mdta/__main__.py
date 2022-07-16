"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Molecular Dynamics Trajectory Analysis."""


if __name__ == "__main__":
    main(prog_name="mdta")  # pragma: no cover
