import initio, time

config = initio.InitioConfiguration();
dopi = initio.Initio(config);

dopi.forwards();

time.sleep(1);

dopi.stop();

time.sleep(1);

dopi.clockwise();

time.sleep(1);

dopi.stop();

time.sleep(1);

dopi.anticlockwise();

time.sleep(1);

dopi.stop();

time.sleep(1);

dopi.reverse();

time.sleep(1);

dopi.stop();
