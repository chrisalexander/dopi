import initio, time, signal

config = initio.InitioConfiguration();
config.head = None;
dopi = initio.Initio(config);

class Antibump:
	"""Don't crash into things (too much)"""

	def __init__(self, initio):
		self.initio = initio;
		self.cont = True;
		signal.signal(signal.SIGINT, self._end);
		self.left = None;
		self.right = None;
		self.initio.ir.addCallback(self._handleSignal);

	def _end(self, signal, frame):
		self.cont = False;

	def _handleSignal(self, left, right):
		self.left = left;
		self.right = right;

	def run(self):
		while self.cont:
			if self.left == 0 and self.right == 0:
				self.initio.drive.reverse();
			elif self.left == 1 and self.right == 0:
				self.initio.drive.anticlockwise();
			elif self.left == 0 and self.right == 1:
				self.initio.drive.clockwise();
			else:
				self.initio.drive.forwards();
			time.sleep(0.5);

ab = Antibump(dopi);
ab.run();

dopi.drive.stop();
