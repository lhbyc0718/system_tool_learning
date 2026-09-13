import subprocess
import sys


def test_normal_name():
    result = subprocess.run(
        [sys.executable, "-m", "greetlab.cli", "--name", "Alice"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0
    assert "Hello, Alice!" in result.stdout


def test_blank_name():
    result = subprocess.run(
        [sys.executable, "-m", "greetlab.cli", "--name", "   "],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 2
    assert "Hello" not in result.stdout
