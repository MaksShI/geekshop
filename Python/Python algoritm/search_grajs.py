from collections import deque


def person_is_sellar(name):
    return 'gg' in name


def search(graph):
    search_queue = deque()
    search_queue += graph['you']
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_sellar(person):
                print(f'{person} + is mango seller!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['anuj'] = []
graph['peggy'] = []
graph['jhonny'] = []
graph['thom'] = []
graph['claire'] = ['thom', 'jhonny']

print(search(graph))
