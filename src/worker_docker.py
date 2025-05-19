import time

from utils import cprint


def worker(log, lockers, stop_event, liste_id):

    while not stop_event.is_set():
        time.sleep(1)

    if log :
        cprint("[LOG]", "green", "")

        print("[worker][end]")
