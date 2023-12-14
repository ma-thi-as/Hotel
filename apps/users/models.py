from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,first_name,last_name, email,document, password = None, **extra_fields):
        if not email or not first_name or not last_name:
            raise Exception("Campos obligatorios!")

        self.email = self.normalize_email(email)
        self.first_name = first_name
        self.last_name = last_name
        self.document = document


        user = self.model(first_name= self.first_name, last_name=self.email,email=email, document=self.document , **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get('is_staff') is not True:
            raise Exception("Es necesario el is_staff en true ")

        if extra_fields.get('is_superuser') is not True:
            raise Exception("Es necesario el is_staff en true ")
        
        return self.create_user(email=email, password=password, **extra_fields)

class User(AbstractUser):
    username = None
    first_name = models.CharField("Priemr nombre", max_length=50)
    last_name = models.CharField("Primer apellido", max_length=50)
    email = models.EmailField(unique=True, max_length=254)
    document = models.CharField("Documento de la persona/Cedula de identidad", max_length=9)

    objects = UserManager() #Inicializar el manager para evitar pasar el username

    REQUIRED_FIELDS = ['first_name', 'last_name', 'document']
    USERNAME_FIELD = 'email'

    class Meta: 
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("User_detail", kwargs={"pk": self.pk})
