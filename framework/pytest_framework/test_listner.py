import pytest


def pytest_runtest_logreport(report):
    if report.when == 'call':
        with open("test_log.txt", "a") as log_file:
            if report.failed:
                log_file.write(f"Test failed: {report.nodeid}\n")
            elif report.passed:
                log_file.write(f"Test passed: {report.nodeid}\n")
            elif report.skipped:
                log_file.write(f"Test skipped: {report.nodeid}\n")


def test_pass():
    assert 1 == 1


def test_fail():
    assert 1 == 2


def test_skip():
    pytest.skip("Skipping this test")

