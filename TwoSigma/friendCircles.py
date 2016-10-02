# Complete the function below.

def  friendCircles(friends):
    
    #If we have an empty list or None return 0 as there are 0 friend circles
    if len(friends) == 0 or friends == None:
        return 0
    else:
        num_circles = 0
        ls = [ 0 ]
        are_friend = [0]
        while len(ls) != 0:
            y = ls[0]
            update_friends = friends[y] #element 0 then 1 then 2 then ... in friends
            ls = ls[1:]
            for indx, friend in enumerate(update_friends): #look through each letter in each row 
                if friend != 'N' and indx != y and indx not in are_friend:
                    ls.append(indx)
                    are_friend.append(indx)
            if not ls: #If we have an empty ls then we have a single match so we have another friend circle
                num_circles = num_circles + 1
                for indx in range(len(friends)):
                    if indx in are_friend: 
                        continue #Don't need duplicates so we continue 
                    else:
                        ls.append(indx)
                        are_friend.append(indx)
                        break
            else:
                continue 
            print ls, are_friend
        return num_circles