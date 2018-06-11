"""
Emululats a small car with random effects
"""
from random import randint
import time
import pafy
#define car starting sound
url = "https://www.youtube.com/watch?v=N_5MMzx5rOs"
video = pafy.new(url)
best = video.getbest()
playurl = best.url
# Play sound while driving car
Video = vlc.Instance()
player = Video.media_player_new()
Car_start = Video.media_new(playurl)
Car_start.get_mrl()
#define car driving sound
url = "https://www.youtube.com/watch?v=6yCIDkFI7ew"
video = pafy.new(url)
best = video.getbest()
playurl = best.url
# Play sound while driving car
Video = vlc.Instance()
player = Video.media_player_new()
Car_drive = Video.media_new(playurl)
Car_drive.get_mrl()


class car(object):
    condition = "New"
    def __init__(self,model,speed, mileage):
        self.model= model
        self.speed = speed
        self.mileage = mileage
    def random_event(self):
        print("You have been visited by the spooky ghost")
    def drive_car(self,distance,music):
        self.mileage += distance
        self.condition = "used"

        print("Car is being driven.",end = "")
        player.set_media(Car_start)
        player.play()
        time.sleep(2)
        player.stop()
        if music == 'Yes':
            player.set_media(Car_drive)
            player.play()
        for i in range(distance):
            event = randint(0,100)
            if event <= 5:
                Car.random_event()

            print(".",end = "", flush=True)
            time.sleep(2)
            # Include random event of crashing
            # Include a random event where you can hit up a girl
            #
        print(" ")
        player.stop()


Lexus = car("Lexus", 120, 0)
print(Lexus.mileage)
print(Lexus.mileage)
print("Welcome to the care simulator, we will begin with determining what car of type you drive")
print("What model is your car:")
car_model = input()
print("Great! Now what is it top speed?")
car_speed = input()
print("Finally, how many kilometers can your car drive on one full tank?")
car_mileage = input()
print("Awesome! Your car is of model {} with a topspeed of {} and a radius of {}.".format(car_model, car_speed,
                                                                                          car_mileage))
time.sleep(1)
print("Now that we have determined what kind of car you are driving we will hit the road!")
print("How far do you want to go?")
estimated_distance = input()
print("{} kilometers it is! Would you like to listen to some music while driving?".format(estimated_distance))
music_parameter = input()
Car = car(car_model,int(car_speed),int(car_mileage))
Car.drive_car(int(estimated_distance),music_parameter)

