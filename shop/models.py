from django.db import models
# Create your models here.
class person(models.Model):
    pic=models.ImageField(blank=True)

    firstname=models.CharField(max_length=50,blank=False)
    choice=[
    ('https://chat.whatsapp.com/HpNnslElleO1DDvY8b4OHr','impact_patna'),
    ('https://chat.whatsapp.com/C3UuGHhhJj5KtxpwkdFElz','GaumataGroup'),
    ('https://chat.whatsapp.com/K3z9zjoBL9N0bvopL7hmzH','Impact_Original'),
    ('https://chat.whatsapp.com/ELTkQ1xDk5GKEcw3GLDxbl','Impact_Banswara'),
    ('https://chat.whatsapp.com/KKZkCJNCqH1G9IjlQTJr8S','Impact_Uttarakhand'),
    ('https://chat.whatsapp.com/DirSyjkmK1DHNjVQYjZ0sK','fivet_in_3 months'),
    ('https://chat.whatsapp.com/HcRTw8JMASB760KlhVkRP2','Impact_Mumbai'),
    ('https://chat.whatsapp.com/HiD9k4slVPV2Q0FlGrbfMW','IMPACT_DESK_2'),
    ('https://chat.whatsapp.com/Ebm33ZFOL1T33BxtMXmQwj','IMPACT_DESK'),
    ('https://chat.whatsapp.com/KvP27ZjMvDpB88xCMNm2pX','IMPACT_TIGER_TEAM',)]
    lastname=models.CharField(max_length=50,blank=False)
    phone=models.CharField(max_length=10,blank=False)
    email=models.EmailField(max_length=500,default="",blank=True)
    whtsapp=models.URLField(default="",choices=choice,blank=True)
    youtube1=models.URLField(default="",blank=True)
    youtube2=models.URLField(default="",blank=True)
    youtube3=models.URLField(default="",blank=True)
    joininglink=models.URLField(default="",blank=True)
    img1=models.ImageField(upload_to='product_img',blank=True)
    img2=models.ImageField(upload_to='product_img',blank=True)
    img3=models.ImageField(upload_to='product_img',blank=True)
    img4=models.ImageField(upload_to='product_img',blank=True)
    img5=models.ImageField(upload_to='product_img',blank=True)
    img6=models.ImageField(upload_to='product_img',blank=True)
    img7=models.ImageField(upload_to='product_img',blank=True)
    img8=models.ImageField(upload_to='product_img',blank=True)
    img9=models.ImageField(upload_to='product_img',blank=True)
    img10=models.ImageField(upload_to='product_img',blank=True)


    def __str__(self):
        return self.firstname
