import initio, time

config = initio.InitioConfiguration();
dopi = initio.Initio(config);

dopi.drive.forwards();

time.sleep(1);

dopi.drive.stop();

time.sleep(1);

dopi.drive.clockwise();

time.sleep(1);

dopi.drive.stop();

time.sleep(1);

dopi.drive.anticlockwise();

time.sleep(1);

dopi.drive.stop();

time.sleep(1);

dopi.drive.reverse();

time.sleep(1);

dopi.drive.stop();
