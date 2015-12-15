from Adaptor import Adaptor
import time
import threading
from DistanceSensor import DistanceSensor
import time
__author__ = 'augusto'


class InOutAdaptor(Adaptor):

    def __init__(self, adaptor_id, max_distance, max_delta, sensor_in, sensor_out):
        super(InOutAdaptor, self).__init__(adaptor_id)
        self.sensor_in_timestamp = 0
        self.sensor_out_timestamp = 0
        self.maximum_distance = max_distance
        self.maximum_delta = max_delta
        self.sensor_out = sensor_out
        self.sensor_in = sensor_in
        self.stopped = True

    def start_reading(self):
        self.stopped = False
        sub_thread = threading.Thread(target=self.__keep_reading_values)
        sub_thread.start()

    def stop_reading(self):
        self.stopped = True

    def __keep_reading_values(self):
        while not self.stopped:
            d_in = self.sensor_in.read_distance()
            self.__new_value_notification(self.sensor_in,d_in)
            d_out = self.sensor_out.read_distance()
            self.__new_value_notification(self.sensor_out,d_out)
            time.sleep(0.1)

    def __new_value_notification(self, sensor, value):

        ts = time.time()

        if value <= self.maximum_distance:
            if sensor == self.sensor_in:
                self.sensor_in_timestamp = ts
            elif sensor == self.sensor_out:
                self.sensor_out_timestamp = ts

        timedif = self.sensor_out_timestamp - self.sensor_in_timestamp

        if 0 < timedif < self.maximum_delta:  # out
            self.sensor_out_timestamp = 0
            self.sensor_in_timestamp = 0
            for listener in self.get_listeners():
                listener.remove_person(ts, self.adaptor_id)
        elif 0 > timedif > -self.maximum_delta:  # in
            self.sensor_out_timestamp = 0
            self.sensor_in_timestamp = 0
            for listener in self.get_listeners():
                listener.add_person(ts, self.adaptor_id)
