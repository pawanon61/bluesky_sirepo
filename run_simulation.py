from simulate import Simulate

sim_id = '7IK2W59z'
sim = Simulate('http://10.10.10.10:8000')

data = sim.auth('srw', sim_id)

watch1 = sim.find_element(data['models']['beamline'], 'title', 'AUX')
data['report'] = 'watchpointReport{}'.format(watch1['id'])
sim.run_simulation()
f1 = sim.get_datafile()
# save the data file for this watchpoint
dec = f1.decode('UTF-8')
datafile = open("data_aux.txt", "w+")
datafile.write(dec)
datafile.close()

watch2 = sim.find_element(data['models']['beamline'], 'title', 'Sample')
data['report'] = 'watchpointReport{}'.format(watch2['id'])
sim.run_simulation()
f2 = sim.get_datafile()
# save data file for this watchpoint
dec = f2.decode('UTF-8')
datafile = open("data_sample.txt", "w+")
datafile.write(dec)
datafile.close()
