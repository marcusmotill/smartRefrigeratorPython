from PIL import Image
import zbarlight

file_path = 'mergedQR.png'
with open(file_path, 'rb') as image_file:
    image = Image.open(image_file)
    image.load()

codes = zbarlight.scan_codes('qrcode', image)

print('QR code: %s' % codes)

from parse_rest.connection import register
register('W4JNsYXU8rAyCKsvQL9a6LVPVmEJsuGYU3T7HQNa', 'RKqH5JjEzYJ3MctcR9OMvLNieqhBYrPt78qftknt')

from parse_rest.datatypes import Object

myClassName = "Refrigerator"
Refrigerator = Object.factory(myClassName)

for code in codes:
	print('QR code: %s' % code)
	refrigerator = Refrigerator(QRCode=code)
	refrigerator.save()