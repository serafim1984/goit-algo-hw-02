import queue



def rec_request(req_queue):
    global i
    
    i += 1
    req_queue.put(i)
    request_text = input('Please write you request: ')
    req_dict[i] = request_text
    return

def resolve_request(req_queue):
    request = req_dict.pop(req_queue.get())
    print(f'You need to resolve: {request}')
    input('Is it OK?')
    return
    

i = 0 
req_queue = queue.Queue()
req_dict = {}

while True:

    action_type = input('What is activity (leave - leave a request, close - close a request, quit - to quit): ')

    if action_type == "leave":

        rec_request(req_queue)

    elif action_type == 'close':

        if req_queue.empty() != True:
        
            resolve_request(req_queue)

        else:

            print('Queue is empty - no requests to resolve')

    elif action_type == 'quit':
        
        print('Goodbye!')
        break

    else:
        print('Wrong iput try once more')

    print(req_dict)
        



    
