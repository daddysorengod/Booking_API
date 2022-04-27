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
        list = []
        for item in room['image']:
            list.append(item)
            
        return {
            "id": str(room['_id']),
            "roomCode": room['roomCode'],
            "roomClass": room['roomClass'],
            "state": room['state'],
            "price": room['price'],
            "numberOfPeople": room['numberOfPeople'],
            "hotelId":room['hotelId'],
            "image":list
        }
    
    # def image_convert(image) -> dict:
    #     return {
    #         "url": image['url'],
    #         "name": image['name'],
    #     }
        
    def post_convert(post) -> dict:
        list = []
        for item in post['image']:
            list.append(item)
            
        return {
            "id": str(post['_id']),
            "content": post['content'],
            "createAt": post['createAt'],
            "likeCount": post['likeCount'],
            "idComment": post['idComment'],
            "image": list                
        }
        
    def comment_convert(comment)-> dict:
        return {
            "id": str(comment['_id']),
            "idAccount": comment['idAccount'],
            "content": comment['content'],
            "likeCount" : comment['likeCount']
            
        }
        
    def hotel_convert(hotel) -> dict:
        list = []
        for item in hotel['image']:
            list.append(item)
        return {
            "id": str(hotel['_id']),
            "nameHotel": hotel['nameHotel'],
            "star": hotel['star'],
            "location": hotel['location'],
            "description": hotel['description'],
            "image":list
        }
    
    def detail_convert(detail) -> dict:
        list = []
        for item in detail['room']:
            list.append(item)
        return {
            "id": str(detail['_id']),
            "account": detail['account'],
            "room": list,
            "checkIn": detail['checkIn'],
            "staying": detail['staying'],
            "state": detail['state'],
            "totalPrice":detail['totalPrice']
        }
    
    def history_convert(history) -> dict:
        return {
            "id": str(history['_id']),
            "room": history['room'],
            "checkIn": history['checkIn'],
            "checkOut": history['checkOut']
        }