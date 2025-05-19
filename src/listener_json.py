import time
import os
import shutil
import json

from utils import cprint

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def listener(log, liste_id):

    time.sleep(5)

    debug_add_json(liste_id, 0)


    if log :
        cprint("[LOG]", "green", "")
        print("[listener][end]")

    return

def debug_add_json(liste_id, id):

    path_dossier_test = os.path.join(BASE_DIR,"testFiles")

    json_files = [
        f for f in os.listdir(path_dossier_test)
        if f.endswith(".json") and os.path.isfile(os.path.join(path_dossier_test, f))
    ]

    test_id = recup_test_id(os.path.join(BASE_DIR,"testFiles", json_files[id]))

    liste_id.append(test_id)
    shutil.copy(
        os.path.join(BASE_DIR,"testFiles", json_files[id]),
        os.path.join(BASE_DIR,"grader_queue", "pending", f"{test_id}_submission.json")
    )


def recup_test_id(path):
        
    with open(path, "r") as f:
        test_id = json.load(f)["test_id"]

    return test_id.zfill(3)


if __name__ == "__main__":
    #print(recup_test_id(os.path.join(BASE_DIR,"testFiles", "submission1.json")))
    pass