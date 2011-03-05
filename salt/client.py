'''
The client module is used to create a client connection to the publisher
'''
# The components here are simple, and they need to be and stay simple, we
# want a client to have 3 external concerns, and maybe a forth configurable
# option.
# The concers are
# 1. Who executes the command?
# 2. what is the function being run?
# 3. What arguments need to be passed to the function?
# 4. How long do we wait for all of the replies?
#
# Next there are a number of tasks, first we need some kind of authentication
# This Client initially will be the master root client, which will run as the 
# root user on the master server.
# BUT we also want a client to be able to work over the network, so that
# controllers can exist within disperate applicaitons.
# The problem is that this is a security nightmare, so I am going to start
# small, and only start with the ability to execute salt commands locally.
# This means that the primary client to build is, the LocalClient

class LocalClient(object):
    '''
    Connect to the salt master via the local server and via root
    '''
    def __init__(self):
        pass

