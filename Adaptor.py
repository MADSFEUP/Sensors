__author__ = 'augusto'

class Adaptor(object):

    def __init__(self,adaptor_id):
        self.listeners = []
        self.adaptor_id = adaptor_id

    def start_reading(self):
        return True

    def add_listener(self, room):
        self.listeners.append(room)

    def get_listeners(self):
        return self.listeners

