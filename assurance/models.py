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

    centre_soins = models.CharField(max_length=150, null=True)
    medecin = models.CharField(max_length=150, null=True)
    patient = models.CharField(max_length=150, null=True)
    medicament1 = models.ForeignKey(Medicament, related_name='medicament1', on_delete=models.CASCADE)
    medicament2 = models.ForeignKey(Medicament, related_name='medicament2', on_delete=models.CASCADE, null=True, blank=True)
    medicament3 = models.ForeignKey(Medicament, related_name='medicament3', on_delete=models.CASCADE, null=True, blank=True)
    medicament4 = models.ForeignKey(Medicament, related_name='medicament4', on_delete=models.CASCADE, null=True, blank=True)
    medicament5 = models.ForeignKey(Medicament, related_name='medicament5', on_delete=models.CASCADE, null=True, blank=True)
    medicament6 = models.ForeignKey(Medicament, related_name='medicament6', on_delete=models.CASCADE, null=True, blank=True)
    medicament7 = models.ForeignKey(Medicament, related_name='medicament7', on_delete=models.CASCADE, null=True, blank=True)
    medicament8 = models.ForeignKey(Medicament, related_name='medicament8', on_delete=models.CASCADE, null=True, blank=True)
    medicament9 = models.ForeignKey(Medicament, related_name='medicament9', on_delete=models.CASCADE, null=True, blank=True)
    medicament10 = models.ForeignKey(Medicament, related_name='medicament10', on_delete=models.CASCADE, null=True, blank=True)
    forme_med1 = models.ForeignKey(Forme, related_name='form_med1', on_delete=models.CASCADE)
    forme_med2 = models.ForeignKey(Forme, related_name='form_med2', on_delete=models.CASCADE, null=True, blank=True)
    forme_med3 = models.ForeignKey(Forme, related_name='form_med3', on_delete=models.CASCADE, null=True, blank=True)
    forme_med4 = models.ForeignKey(Forme, related_name='form_med4', on_delete=models.CASCADE, null=True, blank=True)
    forme_med5 = models.ForeignKey(Forme, related_name='form_med5', on_delete=models.CASCADE, null=True, blank=True)
    forme_med6 = models.ForeignKey(Forme, related_name='form_med6', on_delete=models.CASCADE, null=True, blank=True)
    forme_med7 = models.ForeignKey(Forme, related_name='form_med7', on_delete=models.CASCADE, null=True, blank=True)
    forme_med8 = models.ForeignKey(Forme, related_name='form_med8', on_delete=models.CASCADE, null=True, blank=True)
    forme_med9 = models.ForeignKey(Forme, related_name='form_med9', on_delete=models.CASCADE, null=True, blank=True)
    forme_med10 = models.ForeignKey(Forme, related_name='form_med10', on_delete=models.CASCADE, null=True, blank=True)
    prise_min1 = models.FloatField()
    prise_min2 = models.FloatField(null=True, blank=True)
    prise_min3 = models.FloatField(null=True, blank=True)
    prise_min4 = models.FloatField(null=True, blank=True)
    prise_min5 = models.FloatField(null=True, blank=True)
    prise_min6 = models.FloatField(null=True, blank=True)
    prise_min7 = models.FloatField(null=True, blank=True)
    prise_min8 = models.FloatField(null=True, blank=True)
    prise_min9 = models.FloatField(null=True, blank=True)
    prise_min10 = models.FloatField(null=True, blank=True)
    prise_max1 = models.FloatField()
    prise_max2 = models.FloatField(null=True, blank=True)
    prise_max3 = models.FloatField(null=True, blank=True)
    prise_max4 = models.FloatField(null=True, blank=True)
    prise_max5 = models.FloatField(null=True, blank=True)
    prise_max6 = models.FloatField(null=True, blank=True)
    prise_max7 = models.FloatField(null=True, blank=True)
    prise_max8 = models.FloatField(null=True, blank=True)
    prise_max9 = models.FloatField(null=True, blank=True)
    prise_max10 = models.FloatField(null=True, blank=True)
    unite1 = models.ForeignKey(Unite, related_name='unite1', on_delete=models.CASCADE)
    unite2 = models.ForeignKey(Unite, related_name='unite2', on_delete=models.CASCADE, null=True, blank=True)
    unite3 = models.ForeignKey(Unite, related_name='unite3', on_delete=models.CASCADE, null=True, blank=True)
    unite4 = models.ForeignKey(Unite, related_name='unite4', on_delete=models.CASCADE, null=True, blank=True)
    unite5 = models.ForeignKey(Unite, related_name='unite5', on_delete=models.CASCADE, null=True, blank=True)
    unite6 = models.ForeignKey(Unite, related_name='unite6', on_delete=models.CASCADE, null=True, blank=True)
    unite7 = models.ForeignKey(Unite, related_name='unite7', on_delete=models.CASCADE, null=True, blank=True)
    unite8 = models.ForeignKey(Unite, related_name='unite8', on_delete=models.CASCADE, null=True, blank=True)
    unite9 = models.ForeignKey(Unite, related_name='unite9', on_delete=models.CASCADE, null=True, blank=True)
    unite10 = models.ForeignKey(Unite, related_name='unite10', on_delete=models.CASCADE, null=True, blank=True)
    qte1 = models.ForeignKey(Quantite, related_name='qte1', on_delete=models.CASCADE)
    qte2 = models.ForeignKey(Quantite, related_name='qte2', on_delete=models.CASCADE, null=True, blank=True)
    qte3 = models.ForeignKey(Quantite, related_name='qte3', on_delete=models.CASCADE, null=True, blank=True)
    qte4 = models.ForeignKey(Quantite, related_name='qte4', on_delete=models.CASCADE, null=True, blank=True)
    qte5 = models.ForeignKey(Quantite, related_name='qte5', on_delete=models.CASCADE, null=True, blank=True)
    qte6 = models.ForeignKey(Quantite, related_name='qte6', on_delete=models.CASCADE, null=True, blank=True)
    qte7 = models.ForeignKey(Quantite, related_name='qte7', on_delete=models.CASCADE, null=True, blank=True)
    qte8 = models.ForeignKey(Quantite, related_name='qte8', on_delete=models.CASCADE, null=True, blank=True)
    qte9 = models.ForeignKey(Quantite, related_name='qte9', on_delete=models.CASCADE, null=True, blank=True)
    qte10 = models.ForeignKey(Quantite, related_name='qte10', on_delete=models.CASCADE, null=True, blank=True)

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

    auteur = models.ForeignKey(User, related_name='auteur', null=True, on_delete=models.CASCADE)

    nom = models.CharField(max_length=40, null=True)
    prenom = models.CharField(max_length=40, null=True)
    adresse = models.CharField(max_length=40, null=True)
    ville = models.ForeignKey(Ville, null=True, on_delete=models.SET_NULL)
    telephone = models.CharField(max_length=20, null=True)
    profession = models.ForeignKey(Profession, null=True, on_delete=models.SET_NULL)
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

    agent_sancfis = models.CharField(max_length=40, null=True)
    #agent_sancfis = models.ForeignKey(AgentSancfis, on_delete=models.CASCADE)

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

    agent_sancfis = models.CharField(max_length=40, null=True)
    #agent_sancfis = models.ForeignKey(AgentSancfis, on_delete=models.CASCADE)

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

    agent_sancfis = models.CharField(max_length=40, null=True)
    #agent_sancfis = models.ForeignKey(AgentSancfis, on_delete=models.CASCADE)

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

    agent_sancfis = models.CharField(max_length=40, null=True)
    #agent_sancfis = models.ForeignKey(AgentSancfis, on_delete=models.CASCADE)

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

    assurance = models.CharField(max_length=40, null=True)
    #assurance = models.ForeignKey(Assurance, on_delete=models.CASCADE)

    nom = models.CharField(max_length=40, null=True)
    prenom = models.CharField(max_length=40, null=True)
    adresse = models.CharField(max_length=40, null=True)
    ville = models.ForeignKey(Ville, null=True, on_delete=models.SET_NULL)
    telephone = models.CharField(max_length=15, null=True)
    profession = models.ForeignKey(Profession, null=True, on_delete=models.SET_NULL)
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

    laboratoire = models.CharField(max_length=40, null=True)
    #laboratoire = models.ForeignKey(Laboratoire, on_delete=models.CASCADE)

    nom = models.CharField(max_length=40, null=True)
    prenom = models.CharField(max_length=40, null=True)
    adresse = models.CharField(max_length=40, null=True)
    ville = models.ForeignKey(Ville, null=True, on_delete=models.SET_NULL)
    telephone = models.CharField(max_length=15, null=True)
    profession = models.ForeignKey(Profession, null=True, on_delete=models.SET_NULL)
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

    pharmacie = models.CharField(max_length=40, null=True)
    #pharmacie = models.ForeignKey(Pharmacie, on_delete=models.CASCADE)

    nom = models.CharField(max_length=40, null=True)
    prenom = models.CharField(max_length=40, null=True)
    adresse = models.CharField(max_length=40, null=True)
    ville = models.ForeignKey(Ville, null=True, on_delete=models.SET_NULL)
    telephone = models.CharField(max_length=15, null=True)
    profession = models.ForeignKey(Profession, null=True, on_delete=models.SET_NULL)
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

    cs = models.CharField(max_length=40, null=True)
    #cs = models.ForeignKey(centreDeSoins, on_delete=models.CASCADE)

    nom = models.CharField(max_length=40, null=True)
    prenom = models.CharField(max_length=40, null=True)
    adresse = models.CharField(max_length=40, null=True)
    ville = models.ForeignKey(Ville, null=True, on_delete=models.SET_NULL)
    telephone = models.CharField(max_length=15, null=True)
    profession = models.ForeignKey(Profession, null=True, on_delete=models.SET_NULL)
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

    agent_assurance = models.CharField(max_length=40, null=True)
    #agent_assurance = models.ForeignKey(AgentAssurance, on_delete=models.CASCADE)

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

    agent_assurance = models.CharField(max_length=40, null=True)
    #agent_assurance = models.ForeignKey(AgentAssurance, on_delete=models.CASCADE)
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
    
    agent_assurance = models.CharField(max_length=40, null=True)
    #agent_assurance = models.ForeignKey(AgentAssurance, on_delete=models.CASCADE)
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
    profession = models.ForeignKey(Profession, null=True, on_delete=models.SET_NULL)  
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

