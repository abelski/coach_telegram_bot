#service that handles user related operations

#function check if user if blaclister return boolean

#TODO: implement real logic
def isBlackListedUser(userid):
    usercheckresult = userid == 1
    print(f'isBlackListedUser: {usercheckresult}')
    return usercheckresult