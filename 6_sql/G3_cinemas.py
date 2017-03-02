import argparse


def set_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--movie",
                        action="store", dest="movie", type=int,
                        help="Movie ID")
    return parser.parse_args()


def solution(options):
    raise NotImplementedError("To be implemented.")


if __name__ == "__main__":
    solution(set_options())
