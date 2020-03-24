# class Door:
#     def __init__(self, number, status, color):
#         self.number = number
#         self.status = status
#         self.color = color
#     def open(self):
#         self.status = 'opened'
#     def close(self):
#         self.status = 'closed'

### Door1 ######
# door1 = Door(1, 'closed')
# print(type(door1))
#
# door1.number = 1
# print(door1.status)
#
# door1.open()
# print(door1.status)


#### Door 2 - color #####
# door2 = Door(1, 'opened', 'white')
# print(door2)
#
# print(door2.color)

### Closed Door ###
# class ClosedDoor:
#     def __init__(self, number, status='closed'):
#         self.number = number
#         self.status = status
#     def open(self):
#         self.status = 'opened'
#     def close(self):
#         self.status = 'closed'
#
# #### Door 3 - color #####
# door3 = ClosedDoor(2,)
# print(door3)
#
# print(door3.status)

### Toggle Door ###
# class ToggleDoor:
#     def __init__(self, number, status):
#         self.number = number
#         self.status = status
#
#     def open(self):
#         self.status = 'opened'
#     def close(self):
#         self.status = 'closed'
#     def change(self):
#         d = {'opened': 'closed', 'closed': 'opened'}
#         self.status=d[self.status]
#         # if self.status == 'opened':



#### Door 4 - toggle #####
# door4 = ToggleDoor(1,'opened')
# print(door4)
# door4.change()
# print(door4.status)

#### Modify Door ###
# class Door:
#     color = 'brown'
#     status = 'undefined'
#     def __init__(self, number, status):
#         self.number = number
#         self.status = status
#     def open(self):
#         self.status = 'open'
#     def close(self):
#         self.status = 'closed'
#
# door1 = Door(1, 'closed')
# print(door1.__class__.__dict__['status'])
#
# print(door1.__dict__['status'])


#### Modify Door 2 ###
# class Door:
#     color = 'brown'
#     status = 'closed'
#     def __init__(self, number):
#         self.number = number
#     def open(self):
#         self.status = 'open'
#     def close(self):
#         self.status = 'closed'
#
# door1 = Door(1)
# print(door1.__class__.__dict__['status'])
#
# print(door1.__dict__['status'])


#### Modify Door 3 ###
# class Door:
#     color = 'brown'
#     status = 'closed'
#     def __init__(self, number):
#         self.number = number
#     def toggle(self):
#         d = {'open': 'closed', 'closed': 'open'}
#         self.status = d[self.status]
#
# door1 = Door(1)
# print(door1.status)
# door1.toggle()
# print(door1.status)

#### Modify Door 1 ###
# class Door:
#     color = 'brown'
#     def __init__(self, number, status):
#         self.number = number
#         self.status = status
#     @classmethod
#     def paint(cls, color):
#         cls.color = color
#     def open(self):
#         self.status = 'open'
#     def close(self):
#         self.status = 'closed'
#
# door1 = Door(1, 'closed')
# door1.paint('blue')
# print(door1.color)

#### Modify Door 2 ###
class Door:
    color = 'brown'
    def __init__(self, number, status):
        self.number = number
        self.status = status
    @classmethod
    def paint(cls, color):
        cls.color = color
    def paint(self, color):
        self.color = color
    def open(self):
        self.status = 'open'
    def close(self):
        self.status = 'closed'

door1 = Door(2, 'open')
door1.paint('red')
print(door1.color)
print(door1.__dict__['color'])
print(Door.color)