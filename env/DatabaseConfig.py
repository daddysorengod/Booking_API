import motor.motor_asyncio

myClient = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://daddysorengod:vht01042000@cluster0.ejgjx.mongodb.net/Booking?retryWrites=true&w=majority")
db = myClient['Booking']

