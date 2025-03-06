# service that handles user related operations

# function check if user is blacklisted return boolean

# if you not in whitelist you are blacklisted (temporary solution)
def is_black_listed_user(userid: str) -> bool:
    return not is_whitelisted_user(userid)


# Define a constant whitelist of user IDs
_WHITELISTED_USER_IDS = {473372343, 456, 789}


# Function to check if user_id exists in the whitelist
# for now there is static whitelist of user ids
def is_whitelisted_user(userid: str) -> bool:
    check_result = userid in _WHITELISTED_USER_IDS
    print(f'isWhitelistedUser: {check_result}')
    return check_result
