from itertools import islice  #islice as scissors that cut 
stream_users=__import__('0-stream_users')
for users in islice(stream_users()6,):
   print(users)