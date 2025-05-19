import threading
import signal
import time

import listener_api as api
import worker_docker as wd
import queue_manager as qm
from utils import cprint

stop_event = threading.Event()
lockers = {
    "liste_id_json" : threading.Lock(),
}

LOG = True

def signal_handler(sig, frame):
    if LOG:
        cprint("[LOG]", "yellow", end="")
        print("-> Arret demande ...")
    stop_event.set()

def main():

    if LOG:
        cprint("[LOG]", "green", end="")
        print("-> Demarrage ...")

    liste_id_json = []

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    # mettre le thread de flask en dehors pour eviter la boucle infini en cas de join
    flask_thread = threading.Thread(target=api.run_listener_api)

    threads = [
        threading.Thread(target=qm.manage_queue, args=(LOG, lockers, stop_event, liste_id_json,)),
        threading.Thread(target=wd.worker, args=(LOG, lockers, stop_event, liste_id_json,))
    ]

    for t in threads:
        t.start()
    flask_thread.start()

    if LOG:
        cprint("[LOG]", "green", end="")
        print("-> Application demarree avec succes")


    for t in threads:
        t.join()

    if LOG:
        cprint("[LOG]", "yellow", end="")
        print("-> Arrêt du serveur Flask...")
    api.server_instance.stop()
    flask_thread.join()

    if LOG:
        cprint("[LOG]", "green", end="")
        print("-> END")

if __name__ == "__main__":
    main()
