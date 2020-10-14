" @author: everydaycodings"
# A Program To Generate ORCode

import pyqrcode
import math
# String which represent the QR code
s = "@everydaycodings"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the png file naming "smg.png"
url.svg("smg.svg", scale = 8)
