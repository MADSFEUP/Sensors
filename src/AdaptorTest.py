from Adaptor import Adaptor
from room import Room
from InOutAdaptor import InOutAdaptor
from DistanceSensor import DistanceSensor
import unittest
import time

__author__ = 'augusto'

class DistanceSensorMock(DistanceSensor):
    def __init__(self,sensor_id):
        super(DistanceSensorMock, self).__init__(sensor_id)
        self.distance = 0
        self.sensor_id = sensor_id

    def read_distance(self):
        return self.distance

class AdaptorTest(unittest.TestCase):
    def test_start_reading(self):
        adaptor = Adaptor(1)
        adaptor.start_reading()

    def test_add_listener(self):
        adaptor = Adaptor(1)
        room = Room()
        adaptor.add_listener(room)
        self.assertEqual(len(adaptor.get_listeners()),1)

    def test_person_entering(self):
        in_mock = DistanceSensorMock(1)
        out_mock = DistanceSensorMock(2)
        adaptor = InOutAdaptor(1,200,1000,in_mock,out_mock)
        in_mock.distance = 300
        out_mock.distance = 300
        room = Room()
        adaptor.add_listener(room)
        number = room.get_people()

        in_mock.distance = 300
        out_mock.distance = 90

        adaptor.start_reading()
        time.sleep(0.5)
        in_mock.distance = 90
        out_mock.distance = 300
        time.sleep(0.5)

        self.assertEqual(room.get_people(), number+1)
        adaptor.stop_reading()

if __name__ == '__main__':
    unittest.main()
