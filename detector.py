import datetime
from simulate import Simulate
from ophyd import Device
from ophyd.sim import NullStatus

class LclsDetector(Device):

	# TODO initialize sets of components for device and add the information about those components at the end of program

	def __init__(self, name, x_motor, x_value, y_motor, y_value, sim_id=None, sirepo_server='http://10.10.10.10:8000', **kwargs):
		super().__init__(name=name, **kwargs)
		self._x_motor = x_motor
		self._y_motor = y_motor
		self._x_value = x_value
		self._y_value = y_value
		self._sim_id = sim_id
		self._sirepo_server = sirepo_server
		assert sim_id, 'Simulation ID must be provided'

	def trigger(self):
		# TODO. see if super() works. should work
		# super.trigger()
		super()
		# x = self._x_motor.read()[self._x_value]['value']  # read function reads data from device. it is defined on Device class on ophyd device.py
		# y = self._y_motor.read()[self._y_value]['value']

		# sim_id = '7IK2W59z'
		sim = Simulate(self._sirepo_server)
		data = sim.auth('srw', self._sim_id)

		watch2 = sim.find_element(data['models']['beamline'], 'title', 'Sample')
		data['report'] = 'watchpointReport{}'.format(watch2['id'])
		sim.run_simulation()
		f2 = sim.get_datafile() # data as byte object
		# save data file for this watchpoint
		dec = f2.decode('UTF-8')
		# datafile = open("data_sample_%s.txt" %(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")), "w+")
		# datafile.write(dec)
		# datafile.close()
		return NullStatus()

