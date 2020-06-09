import sys
import pytest
from click.testing import CliRunner

from segysak._cli import cli, NAME
from segysak import __version__ as version

from test_fixtures import temp_dir, temp_segy, TEMP_TEST_DATA_DIR


@pytest.mark.parametrize("help_arg", ["-h", "--help"])
def test_help(help_arg):
    sys.argv = ["", help_arg]
    with pytest.raises(SystemExit):
        cli()


def test_version():
    runner = CliRunner()
    result = runner.invoke(cli, ["--version"])
    assert result.exit_code == 0
    assert result.output == f"{NAME} {version}\n"


def test_no_input_file():
    sys.argv = [""]
    with pytest.raises(SystemExit):
        cli()


@pytest.mark.parametrize("cmd", ["scan", "ebcidc", "convert"])
def test_all_subcommands(temp_segy, cmd):
    runner = CliRunner()
    result = runner.invoke(cli, [cmd, str(temp_segy)])
    assert result.exit_code == 0
