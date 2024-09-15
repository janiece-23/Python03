from pyre import Pyre    #Moduels to use Python Functions and bulitin tools.
from pyre import zhelper
import zmq
import uuid
import json 

 def get_peer_node(username):  
# Function name is: get_peer_node
# username: Used with the variable n to use imported Pyre services and built-in tools.
# Parameters:
#           n = Pyre(username)The get_peer_node in this code is included in the operation.
# The return function is used to have users confirm their Username.

 def join_group(node,group):
 # Function name: join_group, is used to call the function.
# Parameters: 
#             node : Is the peer to peer node that the chat is connect to in the header function.
#             group: Is the peer chat group that the users want to join.
# There is not a return function.

def chat_task(ctx, pipe, n, group):
# Function name: chat_task 
# Parameters: 
#           ctx: This is a ZeroMQ Connection Context.
#           pipe: Is a pipe for communications that are pipe polled by ZeroMQ for messaging.
#           n: The peer to peer node that is being used by my chat application is connected to.
#           group: The peer group chat that the user will be connected to.
# There is no return statement that is included in this code block.

def get_channel(node,group):
# Function name: get_channel
# Parameters: 
#           node:Is apart of the n operation, this is where my chat app is connected to.
#           group: Is the peer user messaging channel. 
# Return: It is used to return the zmq.Context(), ctx, chat_task, n=node, group=groups parameters.