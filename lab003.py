# Part 1: Core Functions-Data Handling and User Input
#Create new Function to get your u
from http.cookiejar import uppercase_escaped_char
from tokenize import group


def get_username():
    print(input(f"Input Username:"))
    return
get_username()


#Create a Function to Select a Chat Group to Join
def get_group():
    print(input(f"Input the Name of Group Chat:"))
get_group()
#Create a Function to Send a Message
def get_message():              #Message sending input variable
    print(input("Send Messages:"))
get_message()

#Part 2: Understanding Peer-to-Peer Communication Functions
##Initializing the Chat##
def initialize_chat():
    get_username()
    get_group()
from pyre import Pyre


def get_peer_node(username):
    n = Pyre(username)
    #n.set_header("CHAT_HEADER1" , "example header1")
    #n.set_header("CHAT_HEADER2" , "example header2")
    n.start()
    return n
get_peer_node(get_username())

def join_group(node, group):
    node.join(group)
    print(f"Joined group: {group}")

def get_channel(node, group):
    ctx = zmq.Context()
    return zhepler.zthread_fork(ctx, chat_task, n=node, group=group)


##Sending and Receiving Messages##
def start_chat():
    channel = initialize_chat()

    while True:
        try:
            msg = get_message()
            channel.send(msg.encode('utf_8'))
        except (KeyboardInterrput, SystemExit):
            break
    channel.send("$$STOP".encode('utf_8'))
    print("FINISHED")
start_chat(input(get_message()))

def chat_task(ctx, pipe, n, group):
    poller = zmq.Poller()
    poller.register(pipe, zmq.POLLIN)
    # print(n.socket())
    poller.register(n.socket(), zmq.POLLIN)
    # print(n.socket())
    while(True):
        items = dict(poller.poll())
        print(n.socket(), items)
        if pipe in items and items[pipe] == zmq.POLLIN:
            message = pipe.recv()
                #message to quit
            if message.decode('utf-8') == "$$STOP":
                break
            print(f"YOU: {message.decode('utf-8')}")
            n.shouts(group, message.decode('utf-8'))
        else:
            cmds = n.recv()
            msg_type = cmds.pop(0).decode('utf-8')
            peer_id = uuid.UUID(bytes=cmds.pop(0))
            peer_username = cmds.pop(0).decode('utf-8')
            match msg_type:
                case "SHOUT":
                    intended_group = cmds.pop(0).decode('utf-8')
                    if intended_group == group:
                        # print(f"{peer_username}({peer_id}): {cmds}")
                        print(f"{peer_username}: {cmds.pop(0).decode('utf-8')}")
                case "ENTER":
                    headers = json.loads(cmds.pop(0).decode('utf-8'))
                    # print(f"NODE_MSG HEADERS: {headers}")
                    # for key in headers:
                    #    print("key = {0}, value = {1}".format(key, headers[key]))
                    # print( f"{peer_username}({peer_id}): is now connected." )
                    print( f"{peer_username}: is now connected." )
                case "JOIN":
                    #print( f"{peer_username}({peer_id}): joined {cmds.pop(0).decode('utf-8')}." )
                    print( f"{peer_username}: joined {cmds.pop( 0 ).decode( 'utf-8' )}." )
            # print(f"NODE_MSG CONT: {cmds}")
    n.stop()
chat_task(ctx, pipe, n, group)










