import time
import os
import shutil

from utils import cprint, is_directory_empty

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def manage_queue(LOG, lockers, stop_event, liste_id):
    
    if LOG :
        cprint("[LOG]", "green", "")
        print("[manage_queue][start]")

    while not stop_event.is_set():
        while is_directory_empty(os.path.join(BASE_DIR, "grader_queue", "arrival")):
            with lockers["liste_id_json"]:
                print(liste_id[-1])
                shutil.move()

        time.sleep(1)

    if LOG :
        cprint("[LOG]", "green", "")
        print("[manage_queue][end]")
