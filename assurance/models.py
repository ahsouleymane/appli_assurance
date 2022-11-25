from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Prestation(models.Model):
    libellePrestation=models.CharField(max_length=40)

    def __str__(self):
        return self.libellePrestation

class Examen(models.Model):
    libelleExamen=models.CharField(max_length=40)

    def __str__(self):
        return self.libelleExamen

class Consultation(models.Model):
    libelleConsultation=models.CharField(max_length=40)

    def __str__(self):
        return self.libelleConsultation

class Medicament(models.Model):
    libelleMedicament=models.CharField(max_length=40)

    def __str__(self):
        return self.libelleMedicament

class Ville(models.Model):
    pays=models.CharField(max_length=40)
    ville=models.CharField(max_length=40)

    def __str__(self):
        return self.ville + ', ' + self.pays
    
class Taille(models.Model):
    taille=models.CharField(max_length=5)

    def __str__(self):
        return self.taille

class Quantite(models.Model):
    qte=models.CharField(max_length=20)

    def __str__(self):
        return self.qte

class Forme(models.Model):
    forme=models.CharField(max_length=30)

    def __str__(self):
        return self.forme

class Moment(models.Model):
    moment=models.CharField(max_length=20)

    def __str__(self):
        return self.moment

class Periode(models.Model):
    periode=models.CharField(max_length=20)

    def __str__(self):
        return self.periode

class Profession(models.Model):
    profession=models.CharField(max_length=40)

    def __str__(self):
        return self.profession

class Masse(models.Model):
    masse=models.CharField(max_length=8)

    def __str__(self):
        return self.masse

class Nombre(models.Model):
    nbr=models.FloatField(max_length=20)

    def __str__(self):
        return self.nbr

class Unite(models.Model):
    unite=models.CharField(max_length=20)

    def __str__(self):
        return self.unite

class Frequence(models.Model):
    frequence=models.CharField(max_length=20)

    def __str__(self):
        return self.frequence

class Specialite(models.Model):
    specialite=models.CharField(max_length=40)

    def __str__(self):
        return self.specialite

class voieAdministration(models.Model):
    voie=models.CharField(max_length=40)

    def __str__(self):
        return self.voie

class Ordonnance(models.Model):
    numeroOrdonnance=models.CharField(max_length=40)

    examen = models.ForeignKey(Examen, on_delete=models.CASCADE)
    medicament = models.ForeignKey(Medicament, on_delete=models.CASCADE)
    quantite = models.ForeignKey(Quantite, on_delete=models.CASCADE)
    forme = models.ForeignKey(Forme, on_delete=models.CASCADE)
    moment = models.ForeignKey(Moment, on_delete=models.CASCADE)
    periode = models.ForeignKey(Periode, on_delete=models.CASCADE)
    nombre = models.ForeignKey(Nombre, on_delete=models.CASCADE)
    unite = models.ForeignKey(Unite, on_delete=models.CASCADE)
    frequence = models.ForeignKey(Frequence, on_delete=models.CASCADE)
    voie = models.ForeignKey(voieAdministration, on_delete=models.CASCADE)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.numeroOrdonnance


class AdminSysteme(models.Model):

    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)

    nom = models.CharField(max_length=40, null=True)
    prenom = models.CharField(max_length=40, null=True)
    adresse = models.CharField(max_length=40, null=True)
    telephone = models.CharField(max_length=20, null=True)
    ville = models.CharField(max_length=40, null=True)
    pays = models.CharField(max_length=40, null=True)
    profession = models.CharField(max_length=40, null=True)
    CHOIX = (
        ('MASCULIN', 'masculin'),
        ('FEMININ', 'feminin'),
    )
    genre = models.CharField(max_length=10, choices=CHOIX, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.prenom + ' ' + self.nom

class AgentSancfis(models.Model):

    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)

    admin = models.ForeignKey(AdminSysteme, null=True, on_delete=models.CASCADE)

    nom = models.CharField(max_length=40, null=True)
    prenom = models.CharField(max_length=40, null=True)
    adresse = models.CharField(max_length=40, null=True)
    ville = models.ForeignKey(Ville, null=True, on_delete=models.SET_NULL)
    telephone = models.CharField(max_length=20, null=True)
    profession = models.CharField(max_length=40, null=True)
    CHOIX = (
        ('MASCULIN', 'masculin'),
        ('FEMININ', 'feminin'),
    )
    genre = models.CharField(max_length=10, choices=CHOIX, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.prenom + ' ' + self.nom

    def save(self, *args, **kwargs):
        try:
            self.utilisateur
        except:
            self.utilisateur = User.objects.last()
        super().save(*args, **kwargs)

class Assurance(models.Model):

    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)

    agent_sancfis = models.ForeignKey(AgentSancfis, on_delete=models.CASCADE)

    designation = models.CharField(max_length=40, null=True)
    adresse = models.CharField(max_length=40, null=True)
    telephone = models.CharField(max_length=15, null=True)
    ville = models.ForeignKey(Ville, null=True, on_delete=models.SET_NULL)
    longitude = models.FloatField(max_length=20, null=True)
    latitude = models.FloatField(max_length=20, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.designation

    def save(self, *args, **kwargs):
        try:
            self.utilisateur
        except:
            self.utilisateur = User.objects.last()
        super().save(*args, **kwargs)


class Laboratoire(models.Model):

    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)

    agent_sancfis = models.ForeignKey(AgentSancfis, on_delete=models.CASCADE)

    designation = models.CharField(max_length=40, null=True)
    adresse = models.CharField(max_length=40, null=True)
    telephone = models.CharField(max_length=15, null=True)
    ville = models.ForeignKey(Ville, null=True, on_delete=models.SET_NULL)
    longitude = models.FloatField(max_length=40, null=True)
    latitude = models.FloatField(max_length=40, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.designation

    def save(self, *args, **kwargs):
        try:
            self.utilisateur
        except:
            self.utilisateur = User.objects.last()
        super().save(*args, **kwargs)


class Pharmacie(models.Model):

    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)

    agent_sancfis = models.ForeignKey(AgentSancfis, on_delete=models.CASCADE)

    designation = models.CharField(max_length=40, null=True)
    adresse = models.CharField(max_length=40, null=True)
    telephone = models.CharField(max_length=15, null=True)
    ville = models.ForeignKey(Ville, null=True, on_delete=models.SET_NULL)
    longitude = models.FloatField(max_length=40, null=True)
    latitude = models.FloatField(max_length=40, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.designation

    def save(self, *args, **kwargs):
        try:
            self.utilisateur
        except:
            self.utilisateur = User.objects.last()
        super().save(*args, **kwargs)

    
class centreDeSoins(models.Model):

    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)

    agent_sancfis = models.ForeignKey(AgentSancfis, on_delete=models.CASCADE)

    designation = models.CharField(max_length=40, null=True)
    adresse = models.CharField(max_length=40, null=True)
    telephone = models.CharField(max_length=15, null=True)
    ville = models.ForeignKey(Ville, null=True, on_delete=models.SET_NULL)
    longitude = models.FloatField(max_length=40, null=True)
    latitude = models.FloatField(max_length=40, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.designation

    def save(self, *args, **kwargs):
        try:
            self.utilisateur
        except:
            self.utilisateur = User.objects.last()
        super().save(*args, **kwargs)


class AgentAssurance(models.Model):

    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)

    assurance = models.ForeignKey(Assurance, on_delete=models.CASCADE)

    nom = models.CharField(max_length=40, null=True)
    prenom = models.CharField(max_length=40, null=True)
    adresse = models.CharField(max_length=40, null=True)
    ville = models.ForeignKey(Ville, null=True, on_delete=models.SET_NULL)
    telephone = models.CharField(max_length=15, null=True)
    profession = models.CharField(max_length=40, null=True)
    CHOIX = (
        ('MASCULIN', 'masculin'),
        ('FEMININ', 'feminin'),
    )
    genre = models.CharField(max_length=10, choices=CHOIX, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.prenom + ' ' + self.nom

    def save(self, *args, **kwargs):
        try:
            self.utilisateur
        except:
            self.utilisateur = User.objects.last()
        super().save(*args, **kwargs)


class AgentLaboratoire(models.Model):

    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)

    laboratoire = models.ForeignKey(Laboratoire, on_delete=models.CASCADE)

    nom = models.CharField(max_length=40, null=True)
    prenom = models.CharField(max_length=40, null=True)
    adresse = models.CharField(max_length=40, null=True)
    ville = models.ForeignKey(Ville, null=True, on_delete=models.SET_NULL)
    telephone = models.CharField(max_length=15, null=True)
    profession = models.CharField(max_length=40, null=True)
    CHOIX = (
        ('MASCULIN', 'masculin'),
        ('FEMININ', 'feminin'),
    )
    genre = models.CharField(max_length=10, choices=CHOIX, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.prenom + ' ' + self.nom
     
    def save(self, *args, **kwargs):
        try:
            self.utilisateur
        except:
            self.utilisateur = User.objects.last()
        super().save(*args, **kwargs)
    
class AgentPharmacie(models.Model):

    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)

    pharmacie = models.ForeignKey(Pharmacie, on_delete=models.CASCADE)

    nom = models.CharField(max_length=40, null=True)
    prenom = models.CharField(max_length=40, null=True)
    adresse = models.CharField(max_length=40, null=True)
    ville = models.ForeignKey(Ville, null=True, on_delete=models.SET_NULL)
    telephone = models.CharField(max_length=15, null=True)
    profession = models.CharField(max_length=40, null=True)
    CHOIX = (
        ('MASCULIN', 'masculin'),
        ('FEMININ', 'feminin'),
    )
    genre = models.CharField(max_length=10, choices=CHOIX, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.prenom + ' ' + self.nom

    def save(self, *args, **kwargs):
        try:
            self.utilisateur
        except:
            self.utilisateur = User.objects.last()
        super().save(*args, **kwargs)
    

class AgentCs(models.Model):

    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)

    cs = models.ForeignKey(centreDeSoins, on_delete=models.CASCADE)

    nom = models.CharField(max_length=40, null=True)
    prenom = models.CharField(max_length=40, null=True)
    adresse = models.CharField(max_length=40, null=True)
    ville = models.ForeignKey(Ville, null=True, on_delete=models.SET_NULL)
    telephone = models.CharField(max_length=15, null=True)
    profession = models.CharField(max_length=40, null=True)
    CHOIX = (
        ('MASCULIN', 'masculin'),
        ('FEMININ', 'feminin'),
    )
    genre = models.CharField(max_length=10, choices=CHOIX, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.prenom + ' ' + self.nom

    def save(self, *args, **kwargs):
        try:
            self.utilisateur
        except:
            self.utilisateur = User.objects.last()
        super().save(*args, **kwargs)
    
    
class Employe(models.Model):

    nom = models.CharField(max_length=40, null=True)
    prenom = models.CharField(max_length=40, null=True)
    dateEmbauche = models.DateField()
    dateResiliation = models.DateField()
    statut = models.BooleanField()
    CHOIX = (
        ('MASCULIN', 'masculin'),
        ('FEMININ', 'feminin'),
    )
    genre = models.CharField(max_length=10, choices=CHOIX, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.prenom + ' ' + self.nom

class policeAssurance(models.Model):

    agent_assurance = models.ForeignKey(AgentAssurance, on_delete=models.CASCADE)

    numero = models.CharField(max_length=40)
    taux = models.IntegerField()
    datePriseEffet = models.DateField()
    dateFin = models.DateField()
    statutModification = models.BooleanField()
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.numero

    
class Souscripteur(models.Model):

    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)

    agent_assurance = models.ForeignKey(AgentAssurance, on_delete=models.CASCADE)
    assurance = models.ForeignKey(Assurance, on_delete=models.CASCADE)
    police_assurance = models.ForeignKey(policeAssurance, on_delete=models.CASCADE)

    designation = models.CharField(max_length=40, null=True)
    adresse = models.CharField(max_length=40, null=True)
    telephone = models.CharField(max_length=15, null=True)
    ville = models.ForeignKey(Ville, null=True, on_delete=models.SET_NULL)
    longitude = models.FloatField(max_length=40, null=True)
    latitude = models.FloatField(max_length=40, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.designation

    def save(self, *args, **kwargs):
        try:
            self.utilisateur
        except:
            self.utilisateur = User.objects.last()
        super().save(*args, **kwargs) 

    
class Assure(models.Model):

    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)
    
    agent_assurance = models.ForeignKey(AgentAssurance, on_delete=models.CASCADE)
    police_assurance = models.ForeignKey(policeAssurance, on_delete=models.CASCADE)

    nom = models.CharField(max_length=40, null=True)
    prenom = models.CharField(max_length=40, null=True)
    numero = models.CharField(max_length=40, null=True)
    adresse = models.CharField(max_length=40, null=True)
    telephone = models.CharField(max_length=15, null=True)
    dateNaiss = models.DateField()
    lieuNaiss = models.CharField(max_length=40, null=True)
    taille = models.FloatField(max_length=4, null=True)
    masse = models.FloatField(max_length=6, null=True)
    ville = models.ForeignKey(Ville, null=True, on_delete=models.SET_NULL)
    defautSante = models.CharField(max_length=40, null=True)
    profession = models.CharField(max_length=40, null=True)  
    ayantDroit = models.BooleanField()    
    statut = models.BooleanField()
    CHOIX = (
        ('MASCULIN', 'masculin'),
        ('FEMININ', 'feminin'),
    )
    genre = models.CharField(max_length=10, choices=CHOIX, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.numero

    def save(self, *args, **kwargs):
        try:
            self.utilisateur
        except:
            self.utilisateur = User.objects.last()
        super().save(*args, **kwargs)

