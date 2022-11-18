from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *


class creerUtillisateur(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nom utilisateur',
            'email': 'Email',
            'password1': 'Mot de passe',
            'password2': 'Confirmer le mot de passe'
        }

class adminSystemeForm(forms.ModelForm):
    class Meta:
        model = AdminSysteme
        fields = ['nom', 'prenom', 'adresse', 'telephone', 'ville', 'pays','profession', 'genre'] 

class assureForm(forms.ModelForm):
    class Meta:
        model = Assure
        fields = ['agent_assurance', 'police_assurance', 'nom', 'prenom', 'numero', 'adresse', 'telephone', 'dateNaiss', 'lieuNaiss', 'taille', 
                        'masse', 'ville', 'defautSante', 'profession', 'ayantDroit', 'genre', 'statut']
        labels = {
            'agent_assurance': 'Agent assurance',
            'police_assurance': 'Police d\'assurance',
            'nom': 'Nom',
            'prenom': 'Prénom',
            'numero': 'Numéro',
            'dateNaiss': 'Date de Naissance',
            'lieuNaiss': 'Lieu de Naissance',
            'taille': 'Taille',
            'masse': 'Masse',
            'adresse': 'Adresse',
            'ville': 'Ville',
            'defautSante': 'Defaut de Santé',
            'telephone': 'Téléphone',
            'profession': 'Profession',
            'ayantDroit': '',
            'genre': 'Genre',
            'statut': 'Etat'
        }

    def __init__(self, *args, **kwargs):
            super(assureForm,self).__init__(*args, **kwargs)
            self.fields['ville'].empty_label = "Choisir"
            self.fields['agent_assurance'].empty_label = "Choisir"
            self.fields['police_assurance'].empty_label = "Choisir"

class assuranceForm(forms.ModelForm):
    class Meta:
        model = Assurance
        fields = ['agent_sancfis', 'designation', 'adresse', 'telephone', 'ville', 'longitude', 'latitude' ]
        labels = {
            'agent_sancfis': 'Agent sancfis',
            'designation': 'Designation',
            'adresse': 'Adresse',
            'ville': 'Ville',
            'telephone': 'Téléphone',
            'longitude': 'Longitude',
            'latitude': 'Latitude'
        }

    def __init__(self, *args, **kwargs):
            super(assuranceForm,self).__init__(*args, **kwargs)
            self.fields['ville'].empty_label = "Choisir"
            self.fields['agent_sancfis'].empty_label = "Choisir"

class pharmacieForm(forms.ModelForm):
    class Meta:
        model = Pharmacie
        fields = ['agent_sancfis', 'designation', 'adresse', 'telephone', 'ville', 'longitude', 'latitude' ]
        labels = {
            'agent_sancfis': 'Agent sancfis',
            'designation': 'Designation',
            'adresse': 'Adresse',
            'ville': 'Ville',
            'telephone': 'Téléphone',
            'longitude': 'Longitude',
            'latitude': 'Latitude'
        }

    def __init__(self, *args, **kwargs):
            super(pharmacieForm,self).__init__(*args, **kwargs)
            self.fields['ville'].empty_label = "Choisir"
            self.fields['agent_sancfis'].empty_label = "Choisir"

class laboratoireForm(forms.ModelForm):
    class Meta:
        model = Laboratoire
        fields = ['agent_sancfis', 'designation', 'adresse', 'telephone', 'ville', 'longitude', 'latitude' ]
        labels = {
            'agent_sancfis': 'Agent sancfis',
            'designation': 'Designation',
            'adresse': 'Adresse',
            'ville': 'Ville',
            'telephone': 'Téléphone',
            'longitude': 'Longitude',
            'latitude': 'Latitude'
        }

    def __init__(self, *args, **kwargs):
            super(laboratoireForm,self).__init__(*args, **kwargs)
            self.fields['ville'].empty_label = "Choisir"
            self.fields['agent_sancfis'].empty_label = "Choisir"

class csForm(forms.ModelForm):
    class Meta:
        model = centreDeSoins
        fields = ['agent_sancfis', 'designation', 'adresse', 'telephone', 'ville', 'longitude', 'latitude' ]
        labels = {
            'agent_sancfis': 'Agent sancfis',
            'designation': 'Designation',
            'adresse': 'Adresse',
            'ville': 'Ville',
            'telephone': 'Téléphone',
            'longitude': 'Longitude',
            'latitude': 'Latitude'
        }

    def __init__(self, *args, **kwargs):
            super(csForm,self).__init__(*args, **kwargs)
            self.fields['ville'].empty_label = "Choisir"
            self.fields['agent_sancfis'].empty_label = "Choisir"

class agentSancfisForm(forms.ModelForm):
    class Meta:
        model = AgentSancfis
        fields = ['nom', 'prenom', 'adresse', 'ville', 'telephone', 'profession', 'genre']
        labels = {
            'nom': 'Nom',
            'prenom': 'Prénom',
            'nom': 'Nom',
            'prenom': 'Prénom',
            'adresse': 'Adresse',
            'ville': 'Ville',
            'telephone': 'Téléphone',
            'profession': 'Profession',
            'genre': 'Genre'
        }

    def __init__(self, *args, **kwargs):
            super(agentSancfisForm,self).__init__(*args, **kwargs)
            self.fields['ville'].empty_label = "Choisir"

class agentAssuranceForm(forms.ModelForm):
    class Meta:
        model = AgentAssurance
        fields = ['assurance', 'nom', 'prenom', 'adresse', 'ville', 'telephone', 'profession', 'genre']
        labels = {
            'assurance': 'Assurance',
            'nom': 'Nom',
            'prenom': 'Prénom',
            'adresse': 'Adresse',
            'ville': 'Ville',
            'telephone': 'Téléphone',
            'profession': 'Profession',
            'genre': 'Genre'
        }

    def __init__(self, *args, **kwargs):
            super(agentAssuranceForm,self).__init__(*args, **kwargs)
            self.fields['ville'].empty_label = "Choisir"
            self.fields['assurance'].empty_label = "Choisir"

class agentCsForm(forms.ModelForm):
    class Meta:
        model = AgentCs
        fields = ['cs', 'nom', 'prenom', 'adresse', 'ville', 'telephone', 'profession', 'genre']
        labels = {
            'cs': 'Centre de soins',
            'nom': 'Nom',
            'prenom': 'Prénom',
            'adresse': 'Adresse',
            'ville': 'Ville',
            'telephone': 'Téléphone',
            'profession': 'Profession',
            'genre': 'Genre'
        }

    def __init__(self, *args, **kwargs):
            super(agentCsForm,self).__init__(*args, **kwargs)
            self.fields['ville'].empty_label = "Choisir"
            self.fields['cs'].empty_label = "Choisir"

class agentLaboratoireForm(forms.ModelForm):
    class Meta:
        model = AgentLaboratoire
        fields = ['laboratoire', 'nom', 'prenom', 'adresse', 'ville', 'telephone', 'profession', 'genre']
        labels = {
            'laboratoire': 'Laboratoire',
            'nom': 'Nom',
            'prenom': 'Prénom',
            'adresse': 'Adresse',
            'ville': 'Ville',
            'telephone': 'Téléphone',
            'profession': 'Profession',
            'genre': 'Genre'
        }

    def __init__(self, *args, **kwargs):
            super(agentLaboratoireForm,self).__init__(*args, **kwargs)
            self.fields['ville'].empty_label = "Choisir"
            self.fields['laboratoire'].empty_label = "Choisir"


class agentPharmacieForm(forms.ModelForm):
    class Meta:
        model = AgentPharmacie
        fields = ['pharmacie', 'nom', 'prenom', 'adresse', 'ville', 'telephone', 'profession', 'genre']
        labels = {
            'pharmacie': 'Pharmacie',
            'nom': 'Nom',
            'prenom': 'Prénom',
            'adresse': 'Adresse',
            'ville': 'Ville',
            'telephone': 'Téléphone',
            'profession': 'Profession',
            'genre': 'Genre'
        }

    def __init__(self, *args, **kwargs):
            super(agentPharmacieForm,self).__init__(*args, **kwargs)
            self.fields['ville'].empty_label = "Choisir"
            self.fields['pharmacie'].empty_label = "Choisir"

class souscripteurForm(forms.ModelForm):
    class Meta:
        model = Souscripteur
        fields = ['agent_assurance', 'assurance', 'police_assurance',
            'designation', 'adresse', 'telephone', 'ville', 'longitude', 'latitude' ]
        labels = {
            'agent_assurance': 'Agent assurance',
            'assurance': 'Assurance',
            'police_assurance': 'Police assurance',
            'designation': 'Designation',
            'adresse': 'Adresse',
            'ville': 'Ville',
            'telephone': 'Téléphone',
            'longitude': 'Longitude',
            'latitude': 'Latitude'
        }

    def __init__(self, *args, **kwargs):
            super(souscripteurForm,self).__init__(*args, **kwargs)
            self.fields['ville'].empty_label = "Choisir"
            self.fields['agent_assurance'].empty_label = "Choisir"
            self.fields['assurance'].empty_label = "Choisir"
            self.fields['police_assurance'].empty_label = "Choisir"

class employeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = ['nom', 'prenom', 'dateEmbauche', 'dateResiliation', 'statut', 'genre']
        labels = {
            'nom': 'Nom',
            'prenom': 'Prénom',
            'dateEmbauche': 'Date Embauche',
            'dateResiliation': 'Date Resiliation',
            'statut': 'Statut',
            'genre': 'Genre',
        }

class policeAssuranceForm(models.Model):
    class Meta:
        model = policeAssurance
        fields = ['agent_assurance', 'souscripteur', 'numero', 'taux', 'datePriseEffet', 'dateFin',
                'statutModification']
        labels = {
            'agent_assurance': 'Agent assurance',
            'souscripteur': 'Souscripteur',
            'numero': 'Numéro',
            'taux': 'Taux',
            'datePriseEffet': 'Date de prise d\'effet',
            'dateFin': 'Date fin',
            'statutModification': 'Statut modification',
        }

class ordonnanceForm(forms.ModelForm):
    class Meta:
        model = Ordonnance
        fields = ['numeroOrdonnance', 'examen', 'medicament', 'quantite', 'forme', 'moment',
                 'periode', 'nombre', 'unite', 'frequence', 'voie']
        labels = {
            'numeroOrdonnance': 'Numero ordonnance',
            'examen': 'Examen',
            'medicament': 'Médicament',
            'quantite': 'Quantité',
            'forme': 'Forme',
            'moment': 'Moment',
            'periode': 'Période',
            'nombre': 'Nombre',
            'unite': 'Unité',
            'frequence': 'Fréquence',
            'voie': 'Voie'
        }

    def __init__(self, *args, **kwargs):
            super(ordonnanceForm,self).__init__(*args, **kwargs)
            self.fields['numeroOrdonnance'].empty_label = "Choisir"
            self.fields['examen'].empty_label = "Choisir"
            self.fields['medicament'].empty_label = "Choisir"
            self.fields['quantite'].empty_label = "Choisir"
            self.fields['forme'].empty_label = "Choisir"
            self.fields['moment'].empty_label = "Choisir"
            self.fields['periode'].empty_label = "Choisir"
            self.fields['nombre'].empty_label = "Choisir"
            self.fields['unite'].empty_label = "Choisir"
            self.fields['frequence'].empty_label = "Choisir"
            self.fields['voie'].empty_label = "Choisir"

class prestationForm(forms.ModelForm):
    class Meta:
        model = Prestation
        fields = '__all__'
        labels = {
            'libellePrestation': 'Prestation',
        }

class examenForm(forms.ModelForm):
    class Meta:
        model = Examen
        fields = '__all__'
        labels = {
            'libelleExamen': 'Type Examen',
        }

class consultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = '__all__'
        labels = {
            'libelleConsultation': 'Type consultation',
        }

class medicamentForm(forms.ModelForm):
    class Meta:
        model = Medicament
        fields = '__all__'
        labels = {
            'libelleMedicament': 'Medicament',
        }

class villeForm(forms.ModelForm):
    class Meta:
        model = Ville
        fields = '__all__'
        labels = {
            'ville': 'Ville',
            'pays': 'Pays',
        }

class tailleForm(forms.ModelForm):
    class Meta:
        model = Taille
        fields = '__all__'
        labels = {
            'taille': 'Taille',
        }

class quantiteForm(forms.ModelForm):
    class Meta:
        model = Quantite
        fields = '__all__'
        labels = {
            'qtite': 'Quantite',
        }

class formeForm(forms.ModelForm):
    class Meta:
        model = Forme
        fields = '__all__'
        labels = {
            'forme': 'Forme',
        }

class momentForm(forms.ModelForm):
    class Meta:
        model = Moment
        fields = '__all__'
        labels = {
            'moment': 'Moment de prise',
        }

class periodeForm(forms.ModelForm):
    class Meta:
        model = Periode
        fields = '__all__'
        labels = {
            'periode': 'Periode de prise',
        }

class professionForm(forms.ModelForm):
    class Meta:
        model = Profession
        fields = '__all__'
        labels = {
            'profession': 'Profession',
        }

class masseForm(forms.ModelForm):
    class Meta:
        model = Masse
        fields = '__all__'
        labels = {
            'masse': 'Masse',
        }

class nombreForm(forms.ModelForm):
    class Meta:
        model = Nombre
        fields = '__all__'
        labels = {
            'nbr': 'Nombre',
        }

class uniteForm(forms.ModelForm):
    class Meta:
        model = Unite
        fields = '__all__'
        labels = {
            'unite': 'Unite de prise',
        }

class frequenceForm(forms.ModelForm):
    class Meta:
        model = Frequence
        fields = '__all__'
        labels = {
            'frequence': 'Frequence de prise',
        }

class specialiteForm(forms.ModelForm):
    class Meta:
        model = Specialite
        fields = '__all__'
        labels = {
            'specialite': 'Specialite medecin',
        }

class voieAdministrationForm(forms.ModelForm):
    class Meta:
        model = voieAdministration
        fields = '__all__'
        labels = {
            'voie': 'Voie administration',
        }


