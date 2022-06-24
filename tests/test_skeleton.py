import pytest

from csc_docker_pool.skeleton import main

__author__ = "maso"
__copyright__ = "maso"
__license__ = "MIT"


def test_main(capsys):
    """CLI Tests"""
    # capsys is a pytest fixture that allows asserts against stdout/stderr
    # https://docs.pytest.org/en/stable/capture.html
    main(["relay", "--help"])
    captured = capsys.readouterr()
    assert "relay" in captured.out
