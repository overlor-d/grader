import time
import os

from utils import cprint

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def manage_queue(LOG, stop_event, liste_id):
    
    while not stop_event.is_set():
        pass


    if LOG :
        cprint("[LOG]", "green", "")
        print("[manage_queue][end]")
