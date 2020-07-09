import os
from django import forms
import magic
from django import forms

class ImageUploadForm(forms.Form):
    """
        2.5MB - 2621440
        5MB - 5242880
        10MB - 10485760
        20MB - 20971520
        50MB - 5242880
        100MB 104857600
        250MB - 214958080
        500MB - 429916160
    """
    file = forms.FileField(required=True)
    maxUploadSize = 104852760
    def validate_size(self,*args, **kwargs):
        data = self.clean(*args, **kwargs)
        file = data['file']
        try:
            if file.size > self.maxUploadSize:
                print("File size exceeded")
                return False
            return True
        except AttributeError:#toast message not displayed even on errors.
            print("Attribute Error")
            return False
    def validate_file_type(self, *args,**kwargs):
        data = self.clean(*args, **kwargs)
        file = data['file']
        valid_mime_types = ['image/jpg', 'image/png', 'image/gif']
        valid_file_extensions = ['.jpg', '.png', '.gif'] 
        ext = os.path.splitext(file.name)[1]
        if ext.lower() not in valid_file_extensions:
            print("Invalid file extensions")
            return False
        file_mime_type = magic.from_buffer(file.read(1024), mime = True)
        if file_mime_type not in valid_mime_types:
            print("Invalid mime types")
            return False
        return True