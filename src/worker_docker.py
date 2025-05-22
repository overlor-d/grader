import time

from utils import cprint
import queue

def worker(LOG, lockers, stop_event, liste_submission):

    if LOG :
        cprint("[LOG]", "green", "")
        print("[worker][start]")


    while not stop_event.is_set():

        while not liste_submission.empty():
            try:
                objet = liste_submission.get_nowait()
                print(objet)
                liste_submission.task_done()
            except queue.Empty:
                pass

        time.sleep(1)

    if LOG :
        cprint("[LOG]", "green", "")

        print("[worker][end]")
