import time

from utils import cprint


def worker(LOG, lockers, stop_event, liste_submission):

    if LOG :
        cprint("[LOG]", "green", "")
        print("[worker][start]")

    i = len(liste_submission)

    while not stop_event.is_set():
        if len(liste_submission) != i:
            print("nouvel element à traiter")
            i = len(liste_submission)
            print(liste_submission[-1])

        time.sleep(1)

    if LOG :
        cprint("[LOG]", "green", "")

        print("[worker][end]")
