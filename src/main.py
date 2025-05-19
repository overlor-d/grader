import threading
import signal
import time

import listener_api as api
import worker_docker as wd
import queue_manager as qm
from utils import cprint

stop_event = threading.Event()
LOG = True

def signal_handler(sig, frame):
    if LOG:
        cprint("[LOG]", "green", "")
        print("-> Arrêt demandé")
    stop_event.set()

def main():
    liste_id_json = []

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    threads = [
        threading.Thread(target=api.run_listener_api),
        threading.Thread(target=wd.worker, args=(LOG, stop_event, liste_id_json,)),
        threading.Thread(target=qm.manage_queue, args=(LOG, stop_event, liste_id_json,))
    ]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
