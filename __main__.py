import os, sys, anywave
import pyqtgraph as pg

# need matplotlib!
sys.path.append('/usr/lib/pymodules/python2.7')


# plugin deps
__file__ = sys.argv[-1]
here = os.path.dirname(__file__)
sys.path.append(os.path.join(here, 'mne-python'))

import mne

# run
app = pg.mkQApp()
raw = mne.io.read_raw_bti(sys.argv[-2], read_header_only=True)
raw.info['filename'] = sys.argv[-2]
mne.viz._3d.pg_plot_meg_and_dig(raw)
app.exec_()
