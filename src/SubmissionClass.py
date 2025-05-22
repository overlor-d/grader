import json

class SubmissionJob:
    def __init__(self, file_path, timestamp):

        with open(file_path, 'r') as fd :
            data = json.load(fd)
        
        self.langage = data["langage"]
        self.test_id = data["test_id"]
        self.user_id = data["user_id"]
        
        self.code_path = data["code_path"]
        self.test_path = data["test_path"]

        self.timestamp = timestamp

    def __str__(self) :
        return f"[langage -> {self.langage}][test id -> {self.test_id}][user id -> {self.user_id}][code path : {self.code_path}, test path : {self.test_path}]"