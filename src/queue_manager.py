import time
import os
import shutil

from utils import cprint, is_directory_empty

from SubmissionClass import SubmissionJob

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def manage_queue(LOG, lockers, stop_event, queue_id, liste_submission):

    if LOG :
        cprint("[LOG]", "green", "")
        print("[manage_queue][start]")


    while not stop_event.is_set():
        while not is_directory_empty(os.path.join(BASE_DIR, "grader_queue", "arrival")):

            id_arrival = queue_id.get_nowait()

            if LOG :
                cprint("[LOG]", "green", "")
                print(f"[manage_queue][ARRIVEE][{id_arrival}]")

            file_path = os.path.join(BASE_DIR, "grader_queue", "arrival", f"{id_arrival}.json")

            liste_submission.put(SubmissionJob(file_path, id_arrival))

            shutil.move(
                file_path, 
                os.path.join(BASE_DIR, "grader_queue", "pending", f"{id_arrival}.json")
            )

            queue_id.task_done()

        time.sleep(5)

    if LOG :
        cprint("[LOG]", "green", "")
        print("[manage_queue][end]")
