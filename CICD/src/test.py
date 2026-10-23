import subprocess


def run_do(*args):
    return subprocess.run(
        ["./build/DO", *args],
        capture_output=True,
        text=True
    )


def test_linux():
    result = run_do("1")
    assert result.stdout == "Learning to Linux\n"
    assert result.returncode == 0


def test_network():
    result = run_do("2")
    assert result.stdout == "Learning to work with Network\n"
    assert result.returncode == 0


def test_monitoring():
    result = run_do("3")
    assert result.stdout == "Learning to Monitoring\n"
    assert result.returncode == 0


def test_extra_monitoring():
    result = run_do("4")
    assert result.stdout == "Learning to extra Monitoring\n"
    assert result.returncode == 0


def test_docker():
    result = run_do("5")
    assert result.stdout == "Learning to Docker\n"
    assert result.returncode == 0


def test_cicd():
    result = run_do("6")
    assert result.stdout == "Learning to CI/CD\n"
    assert result.returncode == 0


def test_bad_number():
    result = run_do("7")
    assert result.stdout == "Bad number!\n"
    assert result.returncode != 0


def test_no_arguments():
    result = run_do()
    assert result.stdout == "Bad number of arguments!\n"
    assert result.returncode != 0