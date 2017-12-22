from __future__ import unicode_literals
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from . import models
from keras.applications.vgg16 import VGG16
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
import numpy as np
from keras.preprocessing.image import load_img

def load_model():
    """Loading model"""
    model = VGG16()
    return model

model = load_model()

class ShowProfile(LoginRequiredMixin, generic.TemplateView):
    template_name = "profiles/show_profile.html"
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')
        if slug:
            profile = get_object_or_404(models.Profile, slug=slug)
            user = profile.user
        else:
            user = self.request.user

        if user == self.request.user:
            kwargs["editable"] = True
        kwargs["show_user"] = user
        return super(ShowProfile, self).get(request, *args, **kwargs)


class EditProfile(LoginRequiredMixin, generic.TemplateView):
    template_name = "profiles/edit_profile.html"
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        user = self.request.user
        if "user_form" not in kwargs:
            kwargs["user_form"] = forms.UserForm(instance=user)
        if "profile_form" not in kwargs:
            kwargs["profile_form"] = forms.ProfileForm(instance=user.profile)
        return super(EditProfile, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        user_form = forms.UserForm(request.POST, instance=user)
        profile_form = forms.ProfileForm(request.POST,
                                         request.FILES,
                                         instance=user.profile)
        if not (user_form.is_valid() and profile_form.is_valid()):
            messages.error(request, "There was a problem with the form. "
                           "Please check the details.")
            user_form = forms.UserForm(instance=user)
            profile_form = forms.ProfileForm(instance=user.profile)
            return super(EditProfile, self).get(request,
                                                user_form=user_form,
                                                profile_form=profile_form)
        # Both forms are fine. Time to save!
        user_form.save()
        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()
        profile_data=models.Profile.objects.filter(user=user).first()
        print(profile_data)
        a= findtheobject(test_img = profile_data.picture)
        # messages.success(request, "Profile details saved!")
        messages.success(request, str(a))
        return redirect("profiles:show_self")


def load_image(image):
    """Loading image"""
    im = load_img(image, target_size=(224, 224))
    return im
def extend_size(image):
    image = np.expand_dims(image,size=(224,) axis=0)
    return image
size=(128,)# model = load_model()
# test_img = "car.jpg"
"""
target_x = 244
target_y = 244
resize_pixels = [target_x, target_y]
"""
def findtheobject(test_img = "bik.jpeg"):
    

    image = load_image("/home/pawan/machine_learning_imgage/Machine_Object_Identification/src/media/"+str(test_img))
    image = img_to_arunrray(image)
    image = preprocess_input(image)
    #image = load_image(test_img, )
    image = extend_size(image)
    y_pred = model.predict(image)
    label = decode_predictions(y_pred)
    print (label)
    return label

