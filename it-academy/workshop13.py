######## Inheritance ###########
class Door:
    color = 'white'
    def __init__(self, number, status):
        self.number = number
        self.status = status
    def open(self):
        self.status = 'opened'
    def close(self):
        self.status = 'closed'

# class SecurityDoor(Door):
#     pass
#
# sdoor = SecurityDoor(1, 'closed')
# print(SecurityDoor.color is Door.color)
#
# print(sdoor.color is Door.color)
#
# print(sdoor.__dict__)

######## Override ########
# class SecurityDoor(Door):
#     color = 'grey'
#     locked = True
#
#     def open(self):
#         if not self.locked:
#             self.status = 'open'
#
# # print(SecurityDoor.__dict__)
#
# sdoor = SecurityDoor(1, 'closed')
# sdoor.open()
# print(sdoor.status)
# sdoor.locked = False
# print(sdoor.status)

######## Another task ########
# class SecurityDoor(Door):
#     color = 'grey'
#     locked = True
#
#     def open(self):
#         if not self.locked:
#             self.status = 'open'
#
#     def close_and_lock(self):
#         self.status = 'closed'
#         self.locked = True
#
#
# sdoor = SecurityDoor(1, 'open')
# sdoor.close_and_lock()
# print(sdoor.status)
# print(sdoor.locked)


######## Another task 2 ########
# class SecurityDoor(Door):
#     color = 'grey'
#     locked = False
#
#     def open(self):
#         if not self.locked:
#             self.status = 'open'
#
#     def close(self, locked=False):
#         self.status = 'closed'
#         self.locked = locked
#
# sdoor = SecurityDoor(1, 'open')
# sdoor.close(True)
# print(sdoor.status)
# print(sdoor.locked)

######## Another task 3 ########
class SecurityDoor(Door):
    color = 'grey'
    locked = False

    def __init__(self, number, status, locked=False):
        self.number = number
        self.status = status
        self.locked = locked

    def open(self):
        if not self.locked:
            self.status = 'open'

    def close(self, locked=False):
        self.status = 'closed'
        self.locked = locked

sdoor = SecurityDoor(1, 'open')
# sdoor.close(True)
# print(sdoor.status)
print(sdoor.locked)