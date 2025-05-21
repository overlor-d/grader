import time
import os
import shutil

from utils import cprint, is_directory_empty

from SubmissionClass import SubmissionJob

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def manage_queue(LOG, lockers, stop_event, liste_id):
    
    if LOG :
        cprint("[LOG]", "green", "")
        print("[manage_queue][start]")

    while not stop_event.is_set():
        while not is_directory_empty(os.path.join(BASE_DIR, "grader_queue", "arrival")):
            with lockers["liste_id_json"]:
                id_arrival = liste_id[0][0]
                liste_id[0].pop(0)

            if LOG :
                cprint("[LOG]", "green", "")
                print(f"[manage_queue][ARRIVEE][{id_arrival}]")
            shutil.move(
                os.path.join(BASE_DIR, "grader_queue", "arrival", f"{id_arrival}.json"), 
                os.path.join(BASE_DIR, "grader_queue", "pending", f"{id_arrival}.json")
            )

        time.sleep(5)

    if LOG :
        cprint("[LOG]", "green", "")
        print("[manage_queue][end]")
