import subprocess
from pathlib import Path
from time import time
from warnings import warn

a, b = (time(), time())
if a == int(a) and b == int(b):
    warn(
        "Timings might be inaccurate due to missing decimals.", category=RuntimeWarning
    )


class Benchmarker:
    def __init__(self, email: str, script: Path):
        self.EMAIL: str = email
        self.SCRIPT: Path = script

    def run_simulation(self, algorithm: int, integer: int):
        command: list[str] = [
            "java",
            "-jar",
            str(self.SCRIPT),
            self.EMAIL,
            str(algorithm),
            str(integer),
        ]

        res: subprocess.CompletedProcess[str] = subprocess.run(
            command, check=False, capture_output=True, text=True
        )

        return res


class Time(float):
    def __new__(cls, seconds: float | None = None):
        if seconds is None:
            seconds: float = time()
        return super().__new__(cls, seconds)

    def seconds(self) -> int:
        return round(self)

    def millis(self) -> int:
        return round(self * 1000)

    def __sub__(self, other):
        return Time(super().__sub__(other))


class Stopwatch:
    def __init__(self):
        self.start()

    def start(self) -> Time:
        self.start_time: Time = Time()
        return self.start_time

    def stop(self) -> Time:
        self.stop_time: Time = Time()
        self.elapsed_time: Time = self.stop_time - self.start_time
        return self.elapsed_time
