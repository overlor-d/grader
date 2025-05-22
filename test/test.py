import queue

q = queue.Queue()

q.put("nouvelle soumission")

item = q.get_nowait()

q.task_done()

print(item)
