from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from PIL import ExifTags

from .forms import imageform
from .models import image, image_desc

# Create your views here.

def image_metadata(file):
    meta_data = {}
    image = Image.open(file)
    mdata = image._getexif()
    if mdata:
        for(tag, value) in mdata.items():
            tagname = TAGS.get(tag, tag)
            meta_data[tagname] = value
    return meta_data


def home(request):
    all_images = image.objects.all()
    return render(request, 'home.html', {'all_images' : all_images})

def image_form_upload(request):
    if request.method == 'POST':
        form = imageform(request.POST, request.FILES)
        # file = request.FILES
        # for item in file:
        #     print (item, ':', file[item])
        #     img = file[item]
        #     all = image_metadata(img)
        #     date_taken = all['DateTimeOriginal']
        #     print(type(date_taken))
        #     # time.strptime('2018:12:24 14:12:44', '%Y:%m:%d  %H:%M:%S')
        #     desc = image_desc(datetime =  datetime.strptime(date_taken, '%Y:%m:%d  %H:%M:%S'))
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
