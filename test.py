from time import time
import requests
import json
import threading
import time

def send_request(i: int):
    if True:
        response=requests.post('http://127.0.0.1:8000/blog',json={'title': f'Kibria{i+2000+2}','body': 'Hello kibria'})
        print("post",response.status_code)
    else:
        response=requests.get(f'http://127.0.0.1:8000/blog/{i}')
        print("get",response.status_code)

start=time.time()
task_list=[]
for i in range(402):
    #get_time("Europe", zone)
    task = threading.Thread(target=send_request, args=(i,))
    task.start()
    task_list.append(task)
print('waiting')
[t.join() for t in task_list]
print('end')
print("Total time taken:", time.time()-start)