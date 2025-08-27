# Software Design Patterns
# Design patterns ae proven, reusable solutions to common problems in software design 
# providing templates or guidlines for structuring code to solve recurring challanges
# in a consistent and efficient way

# 1. Resusable Solutions
# 2. Standardized Terminology
# 3. Scalablity
# 4. Maintainability
# 5. Performance 
# 6. Documentation
# 7. Best Practices
from abc import ABC, abstractmethod
from enum import Enum

class State(ABC):
    @abstractmethod
    def publish():
        pass

class UserRoles(Enum):
    READER =1
    EDITOR =2
    ADMIN = 3

class DraftState(State):
    def __init__(self, document):
        super().__init__()
        self._document = document

    def publish(self):
        self._document.state = ModerationState(self._document)

class ModerationState(State):
    def __init__(self, document):
        super().__init__()
        self._document = document

    def publish(self):
        if self._document.current_user_role == UserRoles.ADMIN:
            self._document.state= PublishState(self._document)

class PublishState(State):
    def __init__(self, document):
        super().__init__()
        self._document = document

    def publish(self):
        pass

class Document:
    def __init__(self, current_user_role: UserRoles):
        self.state = DraftState(self)
        self.current_user_role = current_user_role

    def publish(self):
        self.state.publish()

doc =Document(UserRoles.EDITOR)
print(doc.state.__class__.__name__)
doc.publish()
print(doc.state.__class__.__name__)
doc.current_user_role = UserRoles.ADMIN
doc.publish()
print(doc.state.__class__.__name__)


# from enum import Enum
# class DocumentStates(Enum):
#     DRAFT = 1
#     MODERATION =2 
#     PUBLISHED =3

# class UserRoles(Enum):
#     READER =1
#     EDITOR =2
#     ADMIN = 3

# class Document:
#     def __init__(self, state:DocumentStates, current_user_role: UserRoles):
#         self.state = state
#         self.current_user_role = current_user_role
    
#     def publish(self):
#         if self.state == DocumentStates.DRAFT:
#             self.state = DocumentStates.MODERATION
#         elif self.state == DocumentStates.MODERATION and self.current_user_role == UserRoles.ADMIN:
#             self.state = DocumentStates.PUBLISHED
#         elif self.state == DocumentStates.PUBLISHED:
#             pass
    
# doc = Document(DocumentStates.DRAFT, UserRoles.ADMIN)
# print(f"Initial state: {doc.state.name}")
# doc.publish()
# print(f"Initial state: {doc.state.name}")

