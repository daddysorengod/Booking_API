def account_helper(account) -> dict:
    return {
        "id": str(account['_id']),
        "username" : account['username'],
        "password" : account['password'],
        "name": account['name'],
        "email": account['email'],
        "avatar": account['avatar'],
        "national" : account['national'],
        "createAt" : account['createAt'],
        "role": account['role']
    }

    
    