from detector import LclsDetector
from ophyd.sim import SynAxis
from ophyd import Device, Component as Cpt
import bluesky.plans as bp
# from bluesky.run_engine import RunEngine
from bluesky import RunEngine
from bluesky.callbacks.best_effort import BestEffortCallback
from databroker import Broker
from bluesky.utils import install_kicker
# import matplotlib
# matplotlib.use("agg")  # so that matplotlib doesnot look for display environment
import matplotlib.pyplot as plt
plt.switch_backend('agg')


RE = RunEngine({})

# prepare live visualization
bec = BestEffortCallback()
# Send all metadata/data captured to the BestEffortCallback.
RE.subscribe(bec)
# # make plots update live while scan runs
plt.ioff()
# plt.ion()
# install_kicker()
# temporary sqlite backend
db = Broker.named('temp')

# Insert all metadata/data captured into db.
RE.subscribe(db.insert)


class FakeSlits(Device):
    xwidth = Cpt(SynAxis, delay=0.01)
    ywidth = Cpt(SynAxis, delay=0.02)

fs = FakeSlits(name = 'fs')

detector = LclsDetector('slitdetector', fs.xwidth, 'fsxwidth', fs.ywidth, 'fsywidth', sim_id = '7IK2W59z')

RE(bp.grid_scan([detector], fs.xwidth, 0, 1e-3, 10, fs.ywidth, 0, 1e-3, 10, True))

plt.savefig("scanimage.png")
