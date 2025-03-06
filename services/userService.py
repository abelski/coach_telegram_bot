# service that handles user related operations

# function check if user is blacklisted return boolean

# TODO: implement real logic
def isBlackListedUser(userid: str) -> bool:
    check_result = userid == 1
    print(f'isBlackListedUser: {check_result}')
    return check_result

