from Repository import FakeRepository


class UserRepository(FakeRepository.FakeRepository):

    def __init__(self):
        self.users = []

    def add(self, user):
        self.users.append(user)

    def remove(self, user):
        if self.users:
            for u in self.users:
                if u.login == user.login:
                    self.users.remove(u)

    def get_all(self):
        return self.users

    def get_by_id(self, id):
        if self.users:
            for u in self.users:
                if u.id == id:
                    return u
        return "Пользователь по данному id не найден"
