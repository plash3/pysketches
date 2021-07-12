import concurrent.futures
import sys
import http.client
import json
import queue as qu
import threading

def traverse_graph(queue, visited_set, lock, event, thread_id) -> float:
    rewards = 0
    while not event.is_set():
        try:
            node = queue.get(timeout=1)
            t = adj(node)
            rewards += t[0]
            print(node, rewards, thread_id)
            with lock:
                for v in t[1]:
                    if v not in visited_set:
                        visited_set.add(v)
                        queue.put(v)
            queue.task_done()
        except qu.Empty:
            pass
    return rewards

def adj(node):
    conn = http.client.HTTPConnection(host)
    conn.request('GET', url_base + node)
    response = conn.getresponse()
    json_data = json.loads(response.read().decode())
    conn.close()
    reward = json_data['reward']
    adjacency_list = []
    for url in json_data.get('children', []):
        ind = url.rfind('/') + 1
        adjacency_list.append(url[ind:])
    return (reward, adjacency_list)

host = 'algo.work'
url = '/interview/a'
ind = url.rfind('/') + 1
url_base = url[:ind]
node = url[ind:]

def test_traverse_graph():
    event = threading.Event()
    lock = threading.Lock()
    visited_set = set()
    visited_set.add(node)
    queue = qu.Queue()
    queue.put(node)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        future_set = {executor.submit(traverse_graph, queue, visited_set, lock, event, i) for i in range(2)}
        queue.join()
        event.set()
        result = 0
        for future in concurrent.futures.as_completed(future_set):
            result += future.result()
    print(result)

def main():
    test_traverse_graph()

if __name__ == '__main__':
    sys.exit(main())
