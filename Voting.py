#Task1
def name_matches(vote : str, name : str) -> bool:
    """This function checks if the vote matches the name of an individual regardless of the case"""
    if (str.lower(vote)) in (str.lower(name)):
     return True
    else:
       return False


#Task2
#helper function
def change_case(name_list : list) -> list:
   """This helper function changes the capitalization of a list to lower case regardless of its form for comparison"""
   newlist = []
  
   for itm in name_list:
      temp = str.lower(itm) 
      newlist.append(temp)
   return newlist

def any_votes_for(vote : str, name_list: list[str]) -> bool:
    """ This function checks if the name of a person inputed as a vote is within a list of voter names. It returns true if the input name is within the list and false if not."""
    if (str.lower(vote)) in (change_case(name_list)):
      return True
    else:
      return False
    

#Task3
def count_votes_for(name : str, name_list: list[str]) -> int:
   """This function counts the amount of votes that a person in name has in the name_list. Using a for loop, it searches each element and if it matches the name input, adds 1"""
   count = 0
   x = (str.lower(name))
   for item in (change_case(name_list)):
       if ((item)==(x)):
         count =  count + 1
   return count

#Task4
def got_more_votes(name1 : str, name2 : str, name_list: list[str]) -> str:
   """This function compares the votes of name1 and name2 depending on how many times it is repeated and then returns certain whichever is greater and if there is a tie, it returns tie """
   x = count_votes_for(name1, name_list)
   y = count_votes_for(name2, name_list)
   if x > y:
         return name1
   elif y > x:
        return name2
   else:  
    return "Tie"

#Task5
def record_vote(name_list: list[str], vote : str) -> list:
    """This function adds a new name (a vote) to a list"""
    name_list.append(vote)


#Task6
#Task6
def clean_votes(name_list : list[str]) -> list[str]:
   """This function returns the element within a list that has a space"""
   for itm in name_list:
      if  " " in itm:
        return list(filter(lambda w: " " in w, name_list))
   else:
        return []
def clean_votess(name_list : list[str]) -> list[str]:
   """This function returns the element within a list that has a space"""
   for itm in name_list:
      if  " " in itm:
        name_list = list(filter(lambda w: " " in w, name_list))
      else:
        return []
   return name_list


#Task8
# helperfunction   
def key_fun(elem: str) -> int:
    """This helper function splits a string by spaces and takes the length of that string """
    return len(elem.split(" "))

def sort_phrase_len(list_string : list[str]) -> list[str]:
   """This function sorts the split strings within a list based on the smallest to largest"""
   return sorted(list_string, key=key_fun) 


#Task9
#helper function
def countlist(listofnames : list) -> int:
   """This helper function counts the length of the elements in a given list """
   return len(listofnames)


#Task6
def clean_votes(name_list : list[str]) -> list[str]:
   """This function returns the element within a list that has a space"""
   for itm in name_list:
      if  " " in itm:
        return list(filter(lambda w: " " in w, name_list))
   else:
        return []


def check_percent(name : str, votes_list: list[str], expected_percentage : float, error : float) -> str:
 """ This function calculates the percetage of a given name and then compares the percentage with the error number and the expected percentage to determine whether the derived percentage is "higher" if greater than the addition of expected and error, "lower" if lesser than the subtarction od expected and error or "in range" if within the lower and upper boundaries """
 percent = count_votes_for(name, votes_list)/ countlist(votes_list)
 upperbound = error + expected_percentage
 lowerbound = expected_percentage - error
 if percent < lowerbound:
     return("lower")
 elif percent > upperbound:
       return ("higher")
 else:
      return("in-range") 


assert "name_matches" in dir()
assert "any_votes_for" in dir()
assert "count_votes_for" in dir()
assert "got_more_votes" in dir()
assert "record_vote" in dir()
assert "clean_votes" in dir()
assert "sort_phrase_len" in dir()
assert "check_percent" in dir()
print("All required methods exist!")
