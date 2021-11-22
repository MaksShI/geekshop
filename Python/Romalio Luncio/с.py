from collections import  namedtuple
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.936, LatLong(28, 77))
delhi._asdict()