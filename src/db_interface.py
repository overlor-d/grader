import mysql.connector
from dotenv import load_dotenv
import os

DEBUG = False

load_dotenv()


class Database :
    def __init__(self):
        
        self.host="localhost",
        self.port=int(os.getenv("PORT")),
        self.user=os.getenv("USER"),
        self.password=os.getenv("PASSWORD"),
        self.database=os.getenv("NAME_BDD")

    def get_connection(self):
        try:
            conn = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )

            if (DEBUG):
                print("[DEBUG] Connexion MySQL réussie")

            return conn
        
        except mysql.connector.Error as err:

            if (DEBUG):
                print(f"[DEBUG] Erreur de connexion à la base MySQL : {err}")

            return None

    