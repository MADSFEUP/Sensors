from datetime import *


class Room:
    def __init__(self):
        self.temperatures = {}
        self.noises = {}
        self.people = {}
        self.previous_nr_people = 0

    def set_temperature(self, time, adapter_id, temperature):
        if adapter_id not in self.temperatures:
            self.temperatures[adapter_id] = {}
        self.temperatures[adapter_id][time] = temperature

    def set_noise(self, time, adapter_id, noise):
        if adapter_id not in self.noises:
            self.noises[adapter_id] = {}
        self.noises[adapter_id][time] = noise

    def add_person(self, time, adapter_id):
        if adapter_id not in self.people:
            self.people[adapter_id] = {}
        self.previous_nr_people += 1
        self.people[adapter_id][time] = self.previous_nr_people

    def remove_person(self, time, adapter_id):
        if adapter_id not in self.people:
            self.people[adapter_id] = {}
        self.previous_nr_people -= 1
        self.previous_nr_people = max(self.previous_nr_people, 0)
        self.people[adapter_id][time] = self.previous_nr_people

    def get_people(self):
        return self.previous_nr_people

    def get_temperature(self, at_time):
        sum_temperatures = 0
        count = 0
        for (adapter_id, value) in self.temperatures.items():
            latest_time = None
            latest_temperature = None
            for (entry_time, temperature) in value.items():
                if not latest_time or entry_time > latest_time:
                    latest_time = entry_time
                    latest_temperature = temperature
            if at_time > latest_time and at_time - latest_time < timedelta(hours=1):
                sum_temperatures += latest_temperature
                count += 1

        return sum_temperatures / float(count) if count > 0 else None

    def get_noise(self, at_time):
        sum_noises = 0
        count = 0
        for (adapter_id, value) in self.noises.items():
            latest_time = None
            latest_noise = None
            for (entry_time, temperature) in value.items():
                if not latest_time or entry_time > latest_time:
                    latest_time = entry_time
                    latest_noise = temperature
            if at_time > latest_time and at_time - latest_time < timedelta(hours=1):
                sum_noises += latest_noise
                count += 1

        return sum_noises / float(count) if count > 0 else None
