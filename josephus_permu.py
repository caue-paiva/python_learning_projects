
NUM_BANDITS:int  = 41

def last_one_alive(num_bandits: int, k: int)->int:
   bandit_list: list = [x for x in range(1,num_bandits+1)]
   bandit_set: set = set()
   start_index:int = 0
  # print("k: ", k)
   cur_size: int
   while (cur_size := len(bandit_list)) > 1:
    killed = (start_index+k-1) % cur_size
    del bandit_list[killed]
    start_index = killed % len(bandit_list)
   
   
   print(bandit_list)
 
  




print(last_one_alive(41,3))
      