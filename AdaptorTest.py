from Adaptor import Adaptor
from room import Room
from InOutAdaptor import InOutAdaptor

__author__ = 'augusto'

import unittest

class InOutAdaptorMock(InOutAdaptor):
    def __init__(self,adaptor_id):
        super(InOutAdaptorMock,self).__init__(adaptor_id)

    def simulateEntrance(self):
        self.new_value_notification(1,90) #out
        self.new_value_notification(0,80) #in

class AdaptorTest(unittest.TestCase):
    def test_start_reading(self):
        adaptor = Adaptor(1)
        self.assertTrue(adaptor.start_reading())

    def test_add_listener(self):
        adaptor = Adaptor(1)
        room = Room()
        adaptor.add_listener(room)
        self.assertEqual(len(adaptor.get_listeners()),1)

    def test_person_entering(self):
        adaptor = InOutAdaptorMock(1)
        room = Room()
        adaptor.add_listener(room)
        number = room.get_people()
        adaptor.simulateEntrance()
        self.assertEqual(room.get_people(),number+1)

if __name__ == '__main__':
    unittest.main()
