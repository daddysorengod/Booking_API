from h11 import Data


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
    
    def image_convert(image) -> dict:
        return {
            "url": image['url'],
            "name": image['name'],
        }
        
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