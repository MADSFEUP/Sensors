from Adaptor import Adaptor
import time
__author__ = 'augusto'

class InOutAdaptor(Adaptor):
    def __init__(self,adaptor_id):
        super(InOutAdaptor,self).__init__(adaptor_id)
        self.sensor_in_timestamp = 0
        self.sensor_out_timestamp = 0
        self.maximum_distance = 100 #cm
        self.maximum_delta = 100 #ms

    def new_value_notification(self,sensor_id,value):

        ts = time.time()

        if value <= self.maximum_distance:
            if sensor_id == 0:
                self.sensor_in_timestamp = ts
            elif sensor_id == 1:
                self.sensor_out_timestamp = ts

        timedif = self.sensor_out_timestamp - self.sensor_in_timestamp

        if timedif >= 0 and timedif < self.maximum_delta: #out
            for listener in self.get_listeners():
                listener.remove_person(ts,self.adaptor_id)
        elif timedif < 0 and timedif > -self.maximum_delta: #in
            for listener in self.get_listeners():
                listener.add_person(ts,self.adaptor_id)
