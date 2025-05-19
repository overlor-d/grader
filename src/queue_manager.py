import time

from utils import cprint

def manage_queue(log, stop_event, liste_id):
    
    long = len(liste_id)

    while not stop_event.is_set():
        if long != len(liste_id) :
            if log : 
                cprint("[LOG]", "green", "")
                print(f"[manage_queue] -> la liste a changé nouvel element : {liste_id[-1]}")
            long = len(liste_id)
        time.sleep(1)


    if log :
        cprint("[LOG]", "green", "")

        print("[manage_queue][end]")
