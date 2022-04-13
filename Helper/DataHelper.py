class DataHelper:
    def account_convert(account) -> dict:
        return {
            "id": str(account['_id']),
            "username" : account['username'],
            "password" : account['password'],
            "name": account['name'],
            "email": account['email'],
            "avatar": account['avatar'],
            "national" : account['national'],
            "createAt" : account['createAt'],
            "token": account['token'],
            "role": account['role']
        }

    
    def room_convert(room) -> dict:
        return {
            "id": str(room['_id']),
            "roomCode": room['roomCode'],
            "roomClass": room['roomClass'],
            "state": room['state'],
            "price": room['price'],
            "numberOfPeople": room['numberOfPeople'],
            "checkIn": room['checkIn'],
            "checkOut":room['checkOut']
        }