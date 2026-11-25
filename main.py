import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import pandas as pd

from benchmarker import Benchmarker, Stopwatch, Time


def time_simulation(benchmarker, algorithm: int, integer: int) -> dict[str, int]:
    timer = Stopwatch()
    benchmarker.run_simulation(algorithm, integer)
    time: Time = timer.stop()

    return {
        "integer": integer,
        "time (ms)": time.millis(),
    }


def main():
    parser = argparse.ArgumentParser(description="Benchmarker for the Informatiklabor")

    parser.add_argument("email", help="The E-Mail address to use")
    parser.add_argument(
        "script",
        help="The relative or absolute path to the jar script to profile",
        type=Path,
    )
    parser.add_argument(
        "-o", "--out_dir", help="The output directory for the .csv files", type=Path
    )
    parser.add_argument(
        "-j",
        "--jobs",
        "-w",
        "--workers",
        help="Number of threads to use",
        type=int,
        default=1,
    )

    args = parser.parse_args()

    benchmarker = Benchmarker(args.email, args.script)

    out_dir: Path = args.out_dir or Path(".")
    out_dir.mkdir(parents=True, exist_ok=True)

    with ThreadPoolExecutor(max_workers=args.jobs) as executor:
        for algorithm in (1, 2):
            for run in range(3):
                futures = [
                    executor.submit(time_simulation, benchmarker, algorithm, integer)
                    for integer in range(100)
                ]

                times: list[dict[str, int]] = [
                    future.result() for future in as_completed(futures)
                ]

                file_name = f"algorithmus{algorithm}-{run + 1}.csv"
                pd.DataFrame(data=times).to_csv(
                    out_dir / file_name,
                    index=False,
                )


if __name__ == "__main__":
    main()
