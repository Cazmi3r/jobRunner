def fib(n: int) -> int:
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


class JobRunner:
    def __init__(self, args) -> None:
        self.job_num = args["job_num"]

    def get_job_num(self) -> str:
        return self.job_num
