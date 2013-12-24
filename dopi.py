import initio, time

config = initio.InitioConfiguration();
dopi = initio.Initio(config);

def irCallback(l, r):
	print "IR change: (%s, %s)" % (str(l), str(r));

dopi.ir.addCallback(irCallback);

def floorCallback(l, r):
	print "Floor change: (%s, %s)" % (str(l), str(r));

dopi.floor.addCallback(floorCallback);

dopi.drive.forwards();

dopi.head.pan(-100);

time.sleep(1);

dopi.drive.stop();

time.sleep(1);

dopi.drive.clockwise();

dopi.head.pan(100);

time.sleep(1);

dopi.drive.stop();
dopi.head.pan(0);

time.sleep(1);

dopi.drive.anticlockwise();
dopi.head.tilt(-100);

time.sleep(1);

dopi.drive.stop();

time.sleep(1);

dopi.drive.reverse();
dopi.head.tilt(100);

time.sleep(1);

dopi.head.tilt(0);
dopi.drive.stop();

time.sleep(3);

print "Ultrasonic"
print dopi.ultrasonic.query();

time.sleep(3);
