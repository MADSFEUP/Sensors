from room import Room
from datetime import datetime, timedelta


def test_all():
    test_get_temperature()
    test_get_people()
    test_get_noise()


def test_get_temperature():
    room = Room()
    
    room.set_temperature(datetime.now(), 0, 20)
    assert(room.get_temperature(datetime.now()) == 20)
    
    room.set_temperature(datetime.now(), 1, 30)
    assert(room.get_temperature(datetime.now()) == 25)

    room.set_temperature(datetime.now() + timedelta(hours=9), 0, 50)
    assert(room.get_temperature(datetime.now() + timedelta(hours=9)) == 50)

    assert(room.get_temperature(datetime.now() + timedelta(days=9)) is None)


def test_get_people():
    room = Room()

    room.remove_person(datetime.now(), 0)
    assert(room.get_people() == 0)

    room.add_person(datetime.now(), 0)
    assert(room.get_people() == 1)

    room.remove_person(datetime.now(), 0)
    assert(room.get_people() == 0)

    room.add_person(datetime.now(), 0)
    assert(room.get_people() == 1)

    room.add_person(datetime.now(), 0)
    assert(room.get_people() == 2)

    room.remove_person(datetime.now(), 0)
    assert(room.get_people() == 1)


def test_get_noise():
    room = Room()

    room.set_noise(datetime.now(), 0, 20)
    assert(room.get_noise(datetime.now()) == 20)

    room.set_noise(datetime.now(), 1, 30)
    assert(room.get_noise(datetime.now()) == 25)

    room.set_noise(datetime.now() + timedelta(hours=1), 0, 30)
    assert(room.get_noise(datetime.now() + timedelta(hours=1)) == 30)

    assert(room.get_temperature(datetime.now() + timedelta(days=9)) is None)
