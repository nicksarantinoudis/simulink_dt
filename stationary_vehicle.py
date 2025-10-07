import carla
from carla import *

def main():

	client = carla.Client('localhost',2000)
	client.set_timeout(10.0)
	
	world = client.get_world()
	blueprintLibrary = world.get_blueprint_library()
	
	vehicle = blueprintLibrary.filter('prius')[0]
	
	xPos = 300
	yPos = 59.5
	zPos = 0.6
	
	location = carla.Location(x=xPos, y=yPos, z=zPos)
	
	spawnPoint = carla.Transform(location, carla.Rotation(pitch=0, yaw=0, roll=0))
	
	world.spawn_actor(vehicle, spawnPoint)
   
	
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("Received Keyboard Interupt.")
