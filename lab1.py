
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list is None:        #If list is None, ValueError is raised
      raise ValueError
   if len(int_list) == 0:     #If list is empty, None is returned
      return None
   else:
      mx = int_list[0]        #Uses first number in list as first max number (mx)
      for num in int_list:
         if num > mx:
            mx = num          #If current num is greater than max, current becomes new max
      return mx               #Max num is returned
   pass

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list is None:       #If list is None, ValueError is raised 
      raise ValueError
   if len(int_list) == 0:     #If list is empty, return empty list
      return []
   else:
      out_list = [int_list.pop()] + reverse_rec(int_list)   #Takes last item of list and adds the rest of the list reversed
      return out_list
   pass

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if not int_list:           #If list is None or empty, ValueError is raised
      raise ValueError
   elif low <= high:          #Runs function until the 'low' index is greater than the 'high' index
      mid = low + (high - low) // 2    #Finds middle index in order to split list in half for binary search
      if int_list[mid] == target:
         return mid                    #Returns index if target is found
      elif int_list[mid] > target:     #Searches first half of list if middle num value is greater than the target value
         return bin_search(target, low, mid - 1, int_list)
      else:                            #Searches second half of list if middle num value is less than the target value
         return bin_search(target, mid + 1, high, int_list)
   else:
      return None             #Returns None if target value is not in list
   pass
