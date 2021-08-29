from time import time
import requests
import json
import threading
import time

def send_request(id: int):
    response=requests.get(f'http://127.0.0.1:8000/blog/{id}')
    print(response.status_code)
start=time.time()
task_list=[]
for i in range(100):
    #get_time("Europe", zone)
    task = threading.Thread(target=send_request,args=(i,))
    task.start()
    task_list.append(task)
print('waiting')
[t.join() for t in task_list]
print('end')
print("Total time taken:", time.time()-start)