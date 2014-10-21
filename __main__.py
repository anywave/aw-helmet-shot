import os, sys, anywave

print sys.path


__file__ = sys.argv[-1]
here = os.path.dirname(__file__)
sys.path.append(os.path.join(here, 'mne-python'))

import mne
