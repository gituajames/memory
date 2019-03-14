from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from PIL import ExifTags

from .forms import imageform
from .models import image

# Create your views here.

def image_metadata(file):
    ''' functioin to get image exif data and store them as a dict object '''
    meta_data = {}
    image = Image.open(file)
    mdata = image._getexif()
    if mdata:
        for(tag, value) in mdata.items():
            tagname = TAGS.get(tag, tag)

            if tagname == 'GPSInfo':
                gpsinfo = {}
                for t in value:
                    sub_decoded = GPSTAGS.get(t, t)
                    gpsinfo[sub_decoded] = value[t]

                    meta_data[tagname] = gpsinfo

            else:
                meta_data[tagname] = value
    return meta_data

def home(request):
    all_images = image.objects.all()
    return render(request, 'index.html', {'all_images' : all_images})

def image_form_upload(request):
    if request.method == 'POST':
        form = imageform(request.POST, request.FILES)
        # print('this is the clas of the post you are looking for', type(request.POST))
        # postd = request.POST
        # print(postd)
        # named = postd['description']
        # for key in postd:
        #     print(key, ':', postd[key])
        #
        # file = request.FILES
        # upload_image = file['image']
        # for item in file:
        #     print (item, ':', file[item])
        #     img = file[item]
        #     all = image_metadata(img)
        #     date_taken = all['DateTimeOriginal']
        #     print(type(date_taken))
        #     # time.strptime('2018:12:24 14:12:44', '%Y:%m:%d  %H:%M:%S')
        #     datetime = datetime.strptime(date_taken, '%Y:%m:%d  %H:%M:%S'), name = named, image = request.FILES
        #     desc = image_metadata(upload_image)
        #     desc.save()
        #     print('image aquired on: ', date_taken)
        #
        #     for attr in all:
        #         print(attr, ':', all[attr])

        # print (type(request.FILES))
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = imageform()

    return render(request, 'image_form_upload.html', {'form': form})
