import initio, time

config = initio.InitioConfiguration();
dopi = initio.Initio(config);

dopi.forwards();

time.sleep(1);

dopi.stop();
