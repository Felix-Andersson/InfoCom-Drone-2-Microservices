import requests
import time
import random
import click
from sense_hat import SenseHat as Shat

sense = Shat()

def get_direction():
    step_length = 5
    d_long = 0
    d_la = 0
    send_vel = False
    for event in sense.stick.get_events():
        if event.direction == "up":
            send_vel = True
            d_long = 0
            d_la = step_length
        elif event.direction == "down":
            send_vel = True
            d_long = 0
            d_la = -step_length
        elif event.direction == "left":
            send_vel = True
            d_long = -step_length
            d_la = 0
        elif event.direction == "right":
            send_vel = True
            d_long = step_length
            d_la = 0
        else:
            d_long = 0
            d_la = 0
            click.echo('Invalid input :(')
            send_vel = False
    return d_long, d_la, send_vel


if __name__ == "__main__":
    SERVER_URL = "http://127.0.0.1:5001/drone"
    while True:
        d_long, d_la, send_vel = get_direction()
        if send_vel:
            with requests.Session() as session:
                current_location = {'longitude': d_long,
                                    'latitude': d_la
                                    }
                resp = session.post(SERVER_URL, json=current_location)