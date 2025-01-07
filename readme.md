# Cloudinary with Django Rest Framework
This is a basic usage of cloudinary in a DRF environement. The image file is upload on a Cloudinary server and the image URL is registred in the DataBase

### Instalation of this project
Required :
- A Cloudinary account
- Postman or similar tool

1.  In your virtual env:
    Install the requirement with `pip install -r requirement.txt`

2. Do the migrations.
    In the CloudinaryWithDRF folder use the command
    `python manage.py makemigrations`
    then
    `python manage.py migrate`

3.  Copy your cloudinary credential in a .env file.
    You can see a template for exemple as env.py

### Running this project and usage
Start your venv then go in CloudinaryWithDRF folder. 
Start the project with `python manage.py runserver` 

In Postman ( not on DRF ) try the POST method on the url http://127.0.0.1:8000/api/upload/ 
Now you can test with *imageFile* as key with a type of File. And put any image in the value.


## Creation process

1.  in settings.py copy theses lines.
    notes: I use python-dotenv to keep my crendtials secret and safe. A template for the .env is in the git you just have to add the "." to use it

    ```python
    import cloudinary
    import cloudinary.uploader
    from cloudinary.utils import cloudinary_url

    cloudinary.config( 
        cloud_name = "your cloud name", 
        api_key = "your api key", 
        api_secret = "<your_api_secret>",
        secure=True
    )
    ```

2. Create your app. imageUpload in our exemple
    `python manage.py startapp imageUpload`
    Dont forget to add your app in the INSTALLED_APPS in settings.py 

3. Create a model in you app with this code
    ```python
    from django.db import models
    from cloudinary.models import CloudinaryField

    class Image(models.Model):
        imageFile = CloudinaryField('image', folder='exmple/')
    ```

    The CloudinaryField will send the file to the distant server and generate a result with the image url

4. Do your Serializer and view as usued