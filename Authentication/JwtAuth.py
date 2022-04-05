from datetime import datetime, timedelta
from lib2to3.pgen2 import token
from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from passlib.context import CryptContext
import jwt

class AuthHandler:
    security = HTTPBearer()
    secret = "SECRET"
    pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")
    
    def get_password_hash(self, password:str) -> str:
        return self.pwd_context.hash(password)
    
    def verify_password(self, plain_password, hased_password):
        return self.pwd_context.verify(plain_password,hased_password)
    
    def encode_token(self, id):
        payload = {
            'exp': datetime.utcnow() + timedelta(days=0, minutes=5),
            'iat': datetime.utcnow(),
            'sub': id
        }
        encoded = jwt.encode(payload,self.secret,algorithm='HS256')
        return encoded
    
    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret, algorithms=['HS256'])
            return payload['sub']
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail='signature has expired')
        except jwt.InvalidSignatureError:
            raise HTTPException(status_code=401, detail='invalid token')
        
        
    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(auth.credentials)