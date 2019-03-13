from PIL import Image
from PIL.ExifTags import TAGS
from PIL import ExifTags

info = {}


# image = (r'F:\workspace\pics\memory\documents\IMG_20181013_105815.jpg')
image = (r'siz.jpg')
# image = Image.open(r'F:\workspace\pics\memory\documents\IMG_20181013_105815.jpg')
# mdata = image._getexif()
# if mdata:
#     print('found mdata')
#     for (tag, value) in mdata.items():
#         tagname = TAGS.get(tag, tag)
#         info[tagname] = value

# for items in info:
#     print(items, '-', info[items])
# print(info['GPSInfo'])


def image_metadata(file):
    meta_data = {}
    image = Image.open(file)
    mdata = image._getexif()
    if mdata:
        for(tag, value) in mdata.items():
            tagname = TAGS.get(tag, tag)
            meta_data[tagname] = value
    return meta_data

all = image_metadata(image)
# print(all['GPSInfo'])
gpsinfo = {}
for key in all['GPSInfo'].keys():
    decode = ExifTags.GPSTAGS.get(key, key)
    gpsinfo[decode] = all['GPSInfo'][key]
    # print(gpsinfo)

lat = gpsinfo['GPSLatitude'][0][0] + gpsinfo['GPSLatitude'][1][0]/60.0 + gpsinfo['GPSLatitude'][2][0]/3600.0
lon = gpsinfo['GPSLongitude'][0][0] + gpsinfo['GPSLongitude'][1][0]/60.0 + gpsinfo['GPSLongitude'][2][0]/3600.0
# print(lat, lon)
# print(gpsinfo['GPSLatitude'][2][0])
# for items in gpsinfo:
    # print (items, '-', gpsinfo[items])

if gpsinfo['GPSLatitudeRef'] == 'S':
    lat = (gpsinfo['GPSLatitude'][0][0] + gpsinfo['GPSLatitude'][1][0]/60.0 + gpsinfo['GPSLatitude'][2][0]/3600.0) * -1.0
    print('south')
    print(lat)

else:
    lat = gpsinfo['GPSLatitude'][0][0] + gpsinfo['GPSLatitude'][1][0]/60.0 + gpsinfo['GPSLatitude'][2][0]/3600.0
    print('north')
    print(lat)

if gpsinfo['GPSLongitudeRef'] == 'W':
    print('west')
    lon = (gpsinfo['GPSLongitude'][0][0] + gpsinfo['GPSLongitude'][1][0]/60.0 + gpsinfo['GPSLongitude'][2][0]/3600.0) * -1.0

else:
    print('east')
    lon = gpsinfo['GPSLongitude'][0][0] + gpsinfo['GPSLongitude'][1][0]/60.0 + gpsinfo['GPSLongitude'][2][0]/3600.0
    print(lon)

# print(gpsinfo['GPSLatitudeRef'])

# def get_metadata(image):
#     metadata = {}
#     try:
#         image = Image.open(image)
#         mdata = image._getexif()
#         if mdata:
#             for (tag, value) in mdata.items():
#                 tagname = TAGS.get(tag, tag)
#                 meta_data[tagname] = value

