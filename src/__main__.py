from .modes.hdiff import Hdiff
from .modes.full import Full
from .modes.client_game_res import ClientGameRes
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version", help="Specify the branch version.")
    args = parser.parse_args()

    version = args.version
    cgr = ClientGameRes(version)

    cgr.download_indexes()
    cgr.download_blks()
    pass