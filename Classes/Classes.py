# class DataBase:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
#
#     def __init__(self, user, password, port):
#         self.user = user
#         self.password = password
#         self.port = port
#
#     def __del__(self):
#         DataBase.__instance = None
#
#     def connect(self):
#         print(f"Соединение с базой данных: {self.user} {self.password} {self.port}")
#
#     def close(self):
#         print("Закрываю соединение с базой данных")
#
#     def read(self):
#         print("Данные из базы данных")
#
#     def write(self, data):
#         print(f"Запись в базу данных: {data}")
#
#
# db = DataBase("root", '1234', 90)
# print(DataBase.__dict__)
# print(db.__dict__)
# print(db.user)