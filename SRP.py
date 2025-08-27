#******************************************Good Example*************************************************************
#*******Without any compossition or Inhertance*********
class Emailsender: # send an email
    def send(self, recipient, message):
        print(f"sending an email to {recipient}: {message}")

class User: # 1. Maintain the Username and details
    def __init__(self, username, email):
        self.username = username
        self.email = email

class Userservice (): # 2. Provide the service
    def register(self, user):
        self.user=user
        print(f"Registering username {self.user.username}")
        self._emailsender=Emailsender()
        self._emailsender.send(self.user.email, "Hello")

user = User("sanap","@email.com")
service = Userservice() #remains same
service.register(user)

user2 = User("jqwe","@hmail.com")
service.register(user2)
# Multiple instances in one service # Each Method needs to pass less arguments

#******* With composition or Inhertance*********Tight coupling and less flexibility, cerate new user everytime 
# class Emailsender: # send an email
#     def send(self, recipient, message):
#         print(f"sending an email to {recipient}: {message}")

# class User: # 1. Maintain the Username and details
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email

# class Userservice (Emailsender): # 2. Provide the service
#     def __init__(self, user:User, message):
#         super().__init__()
#         self.user =user
#         self.message = message

#     def register(self):
#         print(f"Registering username {self.user.username}")
#         self.send(self.user.email, self.message)

# user = User("sanap","@email.com")
# Regi =Userservice(user, "Hello")
# Regi.register()
#Cleaner Method Signatures

#************************************************BAD EXample***********************************************************************************
# class Emailsender: # Send an email
#     def send(self, recipient, message):
#         print(f"sending an email to {recipient}: {message}")

# class User: # 1. Responsibility: maintain the username and 2. provide the registration service
#     def __init__(self, username, email, message):
#         self.username = username
#         self.email = email
#         self._emailsender =Emailsender()
#         self.recipient=recipient
#         self.message=message

#     def register(self):
#         print(f"Registering username {self.username}")
#         self._emailsender.send(self.email, self.message)

# usr = User("sanap","@email.com","Hello!")
# usr.register()