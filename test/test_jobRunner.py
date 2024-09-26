import pytest  # type: ignore

from jobRunner.jobRunner import JobRunner, fib


@pytest.fixture
def job():
    args = {"job_num": "9999"}
    return JobRunner(args)


def test_fib() -> None:
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    assert fib(10) == 55


def test_job_num(job) -> None:
    assert job.get_job_num() == "9999"
