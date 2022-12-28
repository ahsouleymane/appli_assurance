from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User, Group
from assurance.forms import *
from assurance.models import *
from .privileges import *

# AUTHENTIFICATION

''' @unauthenticated_user
def connecter(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('acceuil')
        else:
            messages.info(request, 'Email et ou mot de passe incorrect !!!')

    context = {} 
    return render(request, 'auth/login.html', context)'''
# Methode déconnexion

def deconnecter(request):
    
    logout(request)
    messages.info(request, 'User logout successfuly !!!')

    return redirect('login')

# Methode suppression compte utilisateur

def supprimerCompte(request, pk):

    util = User.objects.get(id=pk)
    if request.method == "POST":
        util.delete()
        return redirect('/')

    context = {'item': util}
    return render(request, 'auth/supprimerUtil_form.html', context)


######### ***** LES VUES ADMIN *****

# Vue acceuil administrateur

@droits_admin
@login_required(login_url='login')
def acceuil(request):
       
    utilisateur = User.objects.filter(groups__name='admin')

    context = {'utilisateur': utilisateur}
    return render(request, 'admin/acceuil.html', context)

# Vues creation des tables granulaires

@droits_admin
@login_required(login_url='login')
def tableGranulaire(request):

    # Recuperation de tout les objets de toutes les tables granulaires 
    
    ville = Ville.objects.all()
    prestation = Prestation.objects.all()
    examen = Examen.objects.all()
    consultation = Consultation.objects.all()
    medicament = Medicament.objects.all()
    taille = Taille.objects.all()
    qte = Quantite.objects.all()
    forme = Forme.objects.all()
    moment = Moment.objects.all()
    periode = Periode.objects.all()
    profession = Profession.objects.all()
    masse = Masse.objects.all()
    nbr = Nombre.objects.all()
    unite = Unite.objects.all()
    freq = Frequence.objects.all()
    specialite = Specialite.objects.all()
    voie = voieAdministration.objects.all()

    # Creation d'un object ville

    form1 = villeForm()
    if request.method == "POST":
        form1 = villeForm(request.POST)

        if form1.is_valid():            
            form1.save()

    # Creation d'un object prestation

    form2 = prestationForm()
    if request.method == "POST":
        form2 = prestationForm(request.POST)

        if form2.is_valid():            
            form2.save()

    # Creation d'un object examen

    form3 = examenForm()
    if request.method == "POST":
        form3 = examenForm(request.POST)

        if form3.is_valid():            
            form3.save()

    # Creation d'un object consultation

    form4 = consultationForm()
    if request.method == "POST":
        form4 = consultationForm(request.POST)

        if form4.is_valid():            
            form4.save()

    # Creation d'un object medicament

    form5 = medicamentForm()
    if request.method == "POST":
        form5 = medicamentForm(request.POST)

        if form5.is_valid():            
            form5.save()

    # Creation d'un object taille

    form6 = tailleForm()
    if request.method == "POST":
        form6 = tailleForm(request.POST)

        if form6.is_valid():            
            form6.save()

    # Creation d'un object quantité

    form7 = quantiteForm()
    if request.method == "POST":
        form7 = quantiteForm(request.POST)

        if form7.is_valid():            
            form7.save()

    # Creation d'un object forme

    form8 = formeForm()
    if request.method == "POST":
        form8 = formeForm(request.POST)

        if form8.is_valid():            
            form8.save()

    # Creation d'un object moment

    form9 = momentForm()
    if request.method == "POST":
        form9 = momentForm(request.POST)

        if form9.is_valid():            
            form9.save()

    # Creation d'un object periode

    form10 = periodeForm()
    if request.method == "POST":
        form10 = periodeForm(request.POST)

        if form10.is_valid():            
            form10.save()

    # Creation d'un object profession

    form11 = professionForm()
    if request.method == "POST":
        form11 = professionForm(request.POST)

        if form11.is_valid():            
            form11.save()

    # Creation d'un object masse

    form12 = masseForm()
    if request.method == "POST":
        form12 = masseForm(request.POST)

        if form12.is_valid():            
            form12.save()

    # Creation d'un object nombre

    form13 = nombreForm()
    if request.method == "POST":
        form13 = nombreForm(request.POST)

        if form13.is_valid():            
            form13.save()

    # Creation d'un object unite

    form14 = uniteForm()
    if request.method == "POST":
        form14 = uniteForm(request.POST)

        if form14.is_valid():            
            form14.save()

    # Creation d'un object frequence

    form15 = frequenceForm()
    if request.method == "POST":
        form15 = frequenceForm(request.POST)

        if form15.is_valid():            
            form15.save()

    # Creation d'un object specialite

    form16 = specialiteForm()
    if request.method == "POST":
        form16 = specialiteForm(request.POST)

        if form16.is_valid():            
            form16.save()

    # Creation d'un object voie administration

    form17 = voieAdministrationForm()
    if request.method == "POST":
        form17 = voieAdministrationForm(request.POST)

        if form17.is_valid():            
            form17.save()

    context = {'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4, 'form5': form5, 'form6': form6,
                'form7': form7, 'form8': form8, 'form9': form9, 'form10': form10, 'form11': form11, 'form12': form12, 
                'form13': form13, 'form14': form14, 'form15': form15, 'form16': form16, 'form17': form17,
                'ville': ville, 'prestation': prestation, 'examen': examen, 'consultation': consultation,
                'medicament': medicament, 'taille': taille, 'qte': qte, 'forme': forme,
                'moment': moment, 'periode': periode, 'profession': profession, 'masse': masse, 'nbr': nbr, 'unite': unite,
                'freq': freq, 'specialite': specialite, 'voie': voie}
    return render(request, 'admin/table_granulaire.html', context)

########## ***** Fonctions modifier des tables granulaires *****S

# modifier un object ville

def modifierVille(request, pk):

    form2 = prestationForm()
    form3 = examenForm()
    form4 = consultationForm()
    form5 = medicamentForm()
    form6 = tailleForm()
    form7 = quantiteForm()
    form8 = formeForm()
    form9 = momentForm()
    form10 = periodeForm()
    form11 = professionForm()
    form12 = masseForm()
    form13 = nombreForm()
    form14 = uniteForm()
    form15 = frequenceForm()
    form16 = specialiteForm()
    form17 = voieAdministrationForm()
    
    ville = Ville.objects.get(id=pk)
    form1 = villeForm(instance=ville)
    if request.method == "POST":
        form1 = villeForm(request.POST, instance=ville)

        if form1.is_valid():            
            form1.save()
            return redirect('/table_granulaire/')

    context = {'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4, 'form5': form5, 'form6': form6,
                'form7': form7, 'form8': form8, 'form9': form9, 'form10': form10, 'form11': form11, 'form12': form12, 
                'form13': form13, 'form14': form14, 'form15': form15, 'form16': form16, 'form17': form17}
    return render(request, 'admin/table_granulaire.html', context)


# modifier un object prestation

def modifierPrestation(request, pk):

    form1 = villeForm()
    form3 = examenForm()
    form4 = consultationForm()
    form5 = medicamentForm()
    form6 = tailleForm()
    form7 = quantiteForm()
    form8 = formeForm()
    form9 = momentForm()
    form10 = periodeForm()
    form11 = professionForm()
    form12 = masseForm()
    form13 = nombreForm()
    form14 = uniteForm()
    form15 = frequenceForm()
    form16 = specialiteForm()
    form17 = voieAdministrationForm()

    prestation = Prestation.objects.get(id=pk)
    form2 = prestationForm(instance=prestation)
    if request.method == "POST":
        form2 = prestationForm(request.POST, instance=prestation)

        if form2.is_valid():            
            form2.save()
            return redirect('/table_granulaire/')

    context = {'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4, 'form5': form5, 'form6': form6,
                'form7': form7, 'form8': form8, 'form9': form9, 'form10': form10, 'form11': form11, 'form12': form12, 
                'form13': form13, 'form14': form14, 'form15': form15, 'form16': form16, 'form17': form17}
    return render(request, 'admin/table_granulaire.html', context)


# modifier un object examen

def modifierExamen(request, pk):

    form1 = villeForm()
    form2 = prestationForm()
    form4 = consultationForm()
    form5 = medicamentForm()
    form6 = tailleForm()
    form7 = quantiteForm()
    form8 = formeForm()
    form9 = momentForm()
    form10 = periodeForm()
    form11 = professionForm()
    form12 = masseForm()
    form13 = nombreForm()
    form14 = uniteForm()
    form15 = frequenceForm()
    form16 = specialiteForm()
    form17 = voieAdministrationForm()
    
    examen = Examen.objects.get(id=pk)
    form3 = examenForm(instance=examen)
    if request.method == "POST":
        form3 = examenForm(request.POST, instance=examen)

        if form3.is_valid():            
            form3.save()
            return redirect('/table_granulaire/')

    context = {'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4, 'form5': form5, 'form6': form6,
                'form7': form7, 'form8': form8, 'form9': form9, 'form10': form10, 'form11': form11, 'form12': form12, 
                'form13': form13, 'form14': form14, 'form15': form15, 'form16': form16, 'form17': form17}
    return render(request, 'admin/table_granulaire.html', context) 


# modifier un object consultation

def modifierConsultation(request, pk):

    form1 = villeForm()
    form2 = prestationForm()
    form3 = examenForm()
    form5 = medicamentForm()
    form6 = tailleForm()
    form7 = quantiteForm()
    form8 = formeForm()
    form9 = momentForm()
    form10 = periodeForm()
    form11 = professionForm()
    form12 = masseForm()
    form13 = nombreForm()
    form14 = uniteForm()
    form15 = frequenceForm()
    form16 = specialiteForm()
    form17 = voieAdministrationForm()
    
    consultation = Consultation.objects.get(id=pk)
    form4 = consultationForm(instance=consultation)
    if request.method == "POST":
        form4 = villeForm(request.POST, instance=consultation)

        if form4.is_valid():            
            form4.save()
            return redirect('/table_granulaire/')

    context = {'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4, 'form5': form5, 'form6': form6,
                'form7': form7, 'form8': form8, 'form9': form9, 'form10': form10, 'form11': form11, 'form12': form12, 
                'form13': form13, 'form14': form14, 'form15': form15, 'form16': form16, 'form17': form17}
    return render(request, 'admin/table_granulaire.html', context)


# modifier un object medicament

def modifierMedicament(request, pk):

    form1 = villeForm()
    form2 = prestationForm()
    form3 = examenForm()
    form4 = consultationForm()
    form6 = tailleForm()
    form7 = quantiteForm()
    form8 = formeForm()
    form9 = momentForm()
    form10 = periodeForm()
    form11 = professionForm()
    form12 = masseForm()
    form13 = nombreForm()
    form14 = uniteForm()
    form15 = frequenceForm()
    form16 = specialiteForm()
    form17 = voieAdministrationForm()
    
    medicament = Medicament.objects.get(id=pk)
    form5 = medicamentForm(instance=medicament)
    if request.method == "POST":
        form5 = medicamentForm(request.POST, instance=medicament)

        if form5.is_valid():            
            form5.save()
            return redirect('/table_granulaire/')

    context = {'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4, 'form5': form5, 'form6': form6,
                'form7': form7, 'form8': form8, 'form9': form9, 'form10': form10, 'form11': form11, 'form12': form12, 
                'form13': form13, 'form14': form14, 'form15': form15, 'form16': form16, 'form17': form17}
    return render(request, 'admin/table_granulaire.html', context)


# modifier un object taille

def modifierTaille(request, pk):

    form1 = villeForm()
    form2 = prestationForm()
    form3 = examenForm()
    form4 = consultationForm()
    form5 = medicamentForm()
    form7 = quantiteForm()
    form8 = formeForm()
    form9 = momentForm()
    form10 = periodeForm()
    form11 = professionForm()
    form12 = masseForm()
    form13 = nombreForm()
    form14 = uniteForm()
    form15 = frequenceForm()
    form16 = specialiteForm()
    form17 = voieAdministrationForm()
   
    taille = Taille.objects.get(id=pk)
    form6 = tailleForm(instance=taille)
    if request.method == "POST":
        form6 = tailleForm(request.POST, instance=taille)

        if form6.is_valid():            
            form6.save()
            return redirect('/table_granulaire/')

    context = {'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4, 'form5': form5, 'form6': form6,
                'form7': form7, 'form8': form8, 'form9': form9, 'form10': form10, 'form11': form11, 'form12': form12, 
                'form13': form13, 'form14': form14, 'form15': form15, 'form16': form16, 'form17': form17}
    return render(request, 'admin/table_granulaire.html', context)


# modifier un object quantité

def modifierQuantite(request, pk):

    form1 = villeForm()
    form2 = prestationForm()
    form3 = examenForm()
    form4 = consultationForm()
    form5 = medicamentForm()
    form6 = tailleForm()
    form8 = formeForm()
    form9 = momentForm()
    form10 = periodeForm()
    form11 = professionForm()
    form12 = masseForm()
    form13 = nombreForm()
    form14 = uniteForm()
    form15 = frequenceForm()
    form16 = specialiteForm()
    form17 = voieAdministrationForm()
    
    qte = Quantite.objects.get(id=pk)
    form7 = quantiteForm(instance=qte)
    if request.method == "POST":
        form7 = tailleForm(request.POST, instance=qte)

        if form7.is_valid():            
            form7.save()
            return redirect('/table_granulaire/')

    context = {'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4, 'form5': form5, 'form6': form6,
                'form7': form7, 'form8': form8, 'form9': form9, 'form10': form10, 'form11': form11, 'form12': form12, 
                'form13': form13, 'form14': form14, 'form15': form15, 'form16': form16, 'form17': form17}
    return render(request, 'admin/table_granulaire.html', context)


# modifier un object forme

def modifierForme(request, pk):

    form1 = villeForm()
    form2 = prestationForm()
    form3 = examenForm()
    form4 = consultationForm()
    form5 = medicamentForm()
    form6 = tailleForm()
    form7 = quantiteForm()
    form9 = momentForm()
    form10 = periodeForm()
    form11 = professionForm()
    form12 = masseForm()
    form13 = nombreForm()
    form14 = uniteForm()
    form15 = frequenceForm()
    form16 = specialiteForm()
    form17 = voieAdministrationForm()
    
    forme = Forme.objects.get(id=pk)
    form8 = formeForm(instance=forme)
    if request.method == "POST":
        form8 = formeForm(request.POST, instance=forme)

        if form8.is_valid():            
            form8.save()
            return redirect('/table_granulaire/')

    context = {'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4, 'form5': form5, 'form6': form6,
                'form7': form7, 'form8': form8, 'form9': form9, 'form10': form10, 'form11': form11, 'form12': form12, 
                'form13': form13, 'form14': form14, 'form15': form15, 'form16': form16, 'form17': form17}
    return render(request, 'admin/table_granulaire.html', context)


# modifier un object moment

def modifierMoment(request, pk):

    form1 = villeForm()
    form2 = prestationForm()
    form3 = examenForm()
    form4 = consultationForm()
    form5 = medicamentForm()
    form6 = tailleForm()
    form7 = quantiteForm()
    form8 = formeForm()
    form10 = periodeForm()
    form11 = professionForm()
    form12 = masseForm()
    form13 = nombreForm()
    form14 = uniteForm()
    form15 = frequenceForm()
    form16 = specialiteForm()
    form17 = voieAdministrationForm()
    
    moment = Moment.objects.get(id=pk)
    form9 = momentForm(instance=moment)
    if request.method == "POST":
        form9 = momentForm(request.POST, instance=moment)

        if form9.is_valid():            
            form9.save()
            return redirect('/table_granulaire/')

    context = {'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4, 'form5': form5, 'form6': form6,
                'form7': form7, 'form8': form8, 'form9': form9, 'form10': form10, 'form11': form11, 'form12': form12, 
                'form13': form13, 'form14': form14, 'form15': form15, 'form16': form16, 'form17': form17}
    return render(request, 'admin/table_granulaire.html', context)


# modifier un object periode

def modifierPeriode(request, pk):

    form1 = villeForm()
    form2 = prestationForm()
    form3 = examenForm()
    form4 = consultationForm()
    form5 = medicamentForm()
    form6 = tailleForm()
    form7 = quantiteForm()
    form8 = formeForm()
    form9 = momentForm()
    form11 = professionForm()
    form12 = masseForm()
    form13 = nombreForm()
    form14 = uniteForm()
    form15 = frequenceForm()
    form16 = specialiteForm()
    form17 = voieAdministrationForm()
    
    periode = Periode.objects.get(id=pk)
    form10 = periodeForm(instance=periode)
    if request.method == "POST":
        form10 = periodeForm(request.POST, instance=periode)

        if form10.is_valid():            
            form10.save()
            return redirect('/table_granulaire/')

    context = {'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4, 'form5': form5, 'form6': form6,
                'form7': form7, 'form8': form8, 'form9': form9, 'form10': form10, 'form11': form11, 'form12': form12, 
                'form13': form13, 'form14': form14, 'form15': form15, 'form16': form16, 'form17': form17}
    return render(request, 'admin/table_granulaire.html', context)


# modifier un object prefession

def modifierProfession(request, pk):

    form1 = villeForm()
    form2 = prestationForm()
    form3 = examenForm()
    form4 = consultationForm()
    form5 = medicamentForm()
    form6 = tailleForm()
    form7 = quantiteForm()
    form8 = formeForm()
    form9 = momentForm()
    form10 = periodeForm()
    form12 = masseForm()
    form13 = nombreForm()
    form14 = uniteForm()
    form15 = frequenceForm()
    form16 = specialiteForm()
    form17 = voieAdministrationForm()
    
    profession = Profession.objects.get(id=pk)
    form11 = professionForm(instance=profession)
    if request.method == "POST":
        form11 = professionForm(request.POST, instance=profession)

        if form11.is_valid():            
            form11.save()
            return redirect('/table_granulaire/')

    context = {'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4, 'form5': form5, 'form6': form6,
                'form7': form7, 'form8': form8, 'form9': form9, 'form10': form10, 'form11': form11, 'form12': form12, 
                'form13': form13, 'form14': form14, 'form15': form15, 'form16': form16, 'form17': form17}
    return render(request, 'admin/table_granulaire.html', context)


# modifier un object masse

def modifierMasse(request, pk):

    form1 = villeForm()
    form2 = prestationForm()
    form3 = examenForm()
    form4 = consultationForm()
    form5 = medicamentForm()
    form6 = tailleForm()
    form7 = quantiteForm()
    form8 = formeForm()
    form9 = momentForm()
    form10 = periodeForm()
    form11 = professionForm()
    form13 = nombreForm()
    form14 = uniteForm()
    form15 = frequenceForm()
    form16 = specialiteForm()
    form17 = voieAdministrationForm()
    
    masse = Masse.objects.get(id=pk)
    form12 = masseForm(instance=masse)
    if request.method == "POST":
        form12 = masseForm(request.POST, instance=masse)

        if form12.is_valid():            
            form12.save()
            return redirect('/table_granulaire/')

    context = {'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4, 'form5': form5, 'form6': form6,
                'form7': form7, 'form8': form8, 'form9': form9, 'form10': form10, 'form11': form11, 'form12': form12, 
                'form13': form13, 'form14': form14, 'form15': form15, 'form16': form16, 'form17': form17}
    return render(request, 'admin/table_granulaire.html', context)


# modifier un object nombre

def modifierNombre(request, pk):

    form1 = villeForm()
    form2 = prestationForm()
    form3 = examenForm()
    form4 = consultationForm()
    form5 = medicamentForm()
    form6 = tailleForm()
    form7 = quantiteForm()
    form8 = formeForm()
    form9 = momentForm()
    form10 = periodeForm()
    form11 = professionForm()
    form12 = masseForm()
    form14 = uniteForm()
    form15 = frequenceForm()
    form16 = specialiteForm()
    form17 = voieAdministrationForm()
    
    nombre = Nombre.objects.get(id=pk)
    form13 = nombreForm(instance=nombre)
    if request.method == "POST":
        form13 = nombreForm(request.POST, instance=nombre)

        if form13.is_valid():            
            form13.save()
            return redirect('/table_granulaire/')

    context = {'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4, 'form5': form5, 'form6': form6,
                'form7': form7, 'form8': form8, 'form9': form9, 'form10': form10, 'form11': form11, 'form12': form12, 
                'form13': form13, 'form14': form14, 'form15': form15, 'form16': form16, 'form17': form17}
    return render(request, 'admin/table_granulaire.html', context)


# modifier un object unité

def modifierUnite(request, pk):

    form1 = villeForm()
    form2 = prestationForm()
    form3 = examenForm()
    form4 = consultationForm()
    form5 = medicamentForm()
    form6 = tailleForm()
    form7 = quantiteForm()
    form8 = formeForm()
    form9 = momentForm()
    form10 = periodeForm()
    form11 = professionForm()
    form12 = masseForm()
    form13 = nombreForm()
    form15 = frequenceForm()
    form16 = specialiteForm()
    form17 = voieAdministrationForm()
    
    unite = Unite.objects.get(id=pk)
    form14 = periodeForm(instance=periode)
    if request.method == "POST":
        form14 = uniteForm(request.POST, instance=unite)

        if form14.is_valid():            
            form14.save()
            return redirect('/table_granulaire/')

    context = {'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4, 'form5': form5, 'form6': form6,
                'form7': form7, 'form8': form8, 'form9': form9, 'form10': form10, 'form11': form11, 'form12': form12, 
                'form13': form13, 'form14': form14, 'form15': form15, 'form16': form16, 'form17': form17}
    return render(request, 'admin/table_granulaire.html', context)


# modifier un object frequence

def modifierFrequence(request, pk):

    form1 = villeForm()
    form2 = prestationForm()
    form3 = examenForm()
    form4 = consultationForm()
    form5 = medicamentForm()
    form6 = tailleForm()
    form7 = quantiteForm()
    form8 = formeForm()
    form9 = momentForm()
    form10 = periodeForm()
    form11 = professionForm()
    form12 = masseForm()
    form13 = nombreForm()
    form14 = uniteForm()
    form16 = specialiteForm()
    form17 = voieAdministrationForm()
    
    frequence = Frequence.objects.get(id=pk)
    form15 = frequenceForm(instance=frequence)
    if request.method == "POST":
        form15 = frequenceForm(request.POST, instance=frequence)

        if form15.is_valid():            
            form15.save()
            return redirect('/table_granulaire/')

    context = {'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4, 'form5': form5, 'form6': form6,
                'form7': form7, 'form8': form8, 'form9': form9, 'form10': form10, 'form11': form11, 'form12': form12, 
                'form13': form13, 'form14': form14, 'form15': form15, 'form16': form16, 'form17': form17}
    return render(request, 'admin/table_granulaire.html', context)


# modifier un object specialité

def modifierSpecialite(request, pk):

    form1 = villeForm()
    form2 = prestationForm()
    form3 = examenForm()
    form4 = consultationForm()
    form5 = medicamentForm()
    form6 = tailleForm()
    form7 = quantiteForm()
    form8 = formeForm()
    form9 = momentForm()
    form10 = periodeForm()
    form11 = professionForm()
    form12 = masseForm()
    form13 = nombreForm()
    form14 = uniteForm()
    form15 = frequenceForm()
    form17 = voieAdministrationForm()
    
    specialite = Specialite.objects.get(id=pk)
    form16 = specialiteForm(instance=specialite)
    if request.method == "POST":
        form16 = specialiteForm(request.POST, instance=specialite)

        if form16.is_valid():            
            form16.save()
            return redirect('/table_granulaire/')

    context = {'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4, 'form5': form5, 'form6': form6,
                'form7': form7, 'form8': form8, 'form9': form9, 'form10': form10, 'form11': form11, 'form12': form12, 
                'form13': form13, 'form14': form14, 'form15': form15, 'form16': form16, 'form17': form17}
    return render(request, 'admin/table_granulaire.html', context)


# modifier un object voie administration

def modifierVoieAdmin(request, pk):

    form1 = villeForm()
    form2 = prestationForm()
    form3 = examenForm()
    form4 = consultationForm()
    form5 = medicamentForm()
    form6 = tailleForm()
    form7 = quantiteForm()
    form8 = formeForm()
    form9 = momentForm()
    form10 = periodeForm()
    form11 = professionForm()
    form12 = masseForm()
    form13 = nombreForm()
    form14 = uniteForm()
    form15 = frequenceForm()
    form16 = specialiteForm()
    
    voie = voieAdministration.objects.get(id=pk)
    form17 = voieAdministrationForm(instance=voie)
    if request.method == "POST":
        form17 = voieAdministrationForm(request.POST, instance=voie)

        if form17.is_valid():            
            form17.save()
            return redirect('/table_granulaire/')

    context = {'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4, 'form5': form5, 'form6': form6,
                'form7': form7, 'form8': form8, 'form9': form9, 'form10': form10, 'form11': form11, 'form12': form12, 
                'form13': form13, 'form14': form14, 'form15': form15, 'form16': form16, 'form17': form17}
    return render(request, 'admin/table_granulaire.html', context)


########## ***** Methodes suppression des tables granulaires *****

# supprimer un object ville

def supprimerVille(request, pk):

    supprimer_ville = Ville.objects.get(id = pk)
    supprimer_ville.delete()

    return redirect('table_granulaire')


# supprimer un object prestation

def supprimerPrestation(request, pk):

    supprimer_prestation = Prestation.objects.get(id = pk)
    supprimer_prestation.delete()

    return redirect('table_granulaire')


# supprimer un object examen

def supprimerExamen(request, pk):

    supprimer_examen = Examen.objects.get(id = pk)
    supprimer_examen.delete()

    return redirect('table_granulaire')


# supprimer un object consultation

def supprimerConsultation(request, pk):

    supprimer_consultation = Consultation.objects.get(id = pk)
    supprimer_consultation.delete()

    return redirect('table_granulaire')


# supprimer un object moment

def supprimerMoment(request, pk):

    supprimer_moment = Moment.objects.get(id = pk)
    supprimer_moment.delete()

    return redirect('table_granulaire')


# supprimer un object periode

def supprimerPeriode(request, pk):

    supprimer_periode = Periode.objects.get(id = pk)
    supprimer_periode.delete()

    return redirect('table_granulaire')


# supprimer un object profession

def supprimerProfession(request, pk):

    supprimer_profession = Profession.objects.get(id = pk)
    supprimer_profession.delete()

    return redirect('table_granulaire')


# supprimer un object masse

def supprimerMasse(request, pk):

    supprimer_masse = Masse.objects.get(id = pk)
    supprimer_masse.delete()

    return redirect('table_granulaire')


# supprimer un object unité

def supprimerUnite(request, pk):

    supprimer_unite = Unite.objects.get(id = pk)
    supprimer_unite.delete()

    return redirect('table_granulaire')


# supprimer un object frequence

def supprimerFrequence(request, pk):

    supprimer_frequence = Frequence.objects.get(id = pk)
    supprimer_frequence.delete()

    return redirect('table_granulaire')


# supprimer un object specialité

def supprimerSpecialite(request, pk):

    supprimer_specialite = Specialite.objects.get(id = pk)
    supprimer_specialite.delete()

    return redirect('table_granulaire')


# supprimer un object voie administration

def supprimerVoieAdmin(request, pk):

    supprimer_voie = voieAdministration.objects.get(id = pk)
    supprimer_voie.delete()

    return redirect('table_granulaire')


# supprimer un object medicament

def supprimerMedicament(request, pk):

    supprimer_med = Medicament.objects.get(id = pk)
    supprimer_med.delete()

    return redirect('table_granulaire')


# supprimer un object taille

def supprimerTaille(request, pk):

    supprimer_taille = Taille.objects.get(id = pk)
    supprimer_taille.delete()

    return redirect('table_granulaire')


# supprimer un object quantité

def supprimerQuantite(request, pk):

    supprimer_quantite = Quantite.objects.get(id = pk)
    supprimer_quantite.delete()

    return redirect('table_granulaire')


# supprimer un object nombre

def supprimerNombre(request, pk):

    supprimer_nbr = Nombre.objects.get(id = pk)
    supprimer_nbr.delete()

    return redirect('table_granulaire')


# supprimer un object forme

def supprimerForme(request, pk):

    supprimer_forme = Forme.objects.get(id = pk)
    supprimer_forme.delete()

    return redirect('table_granulaire')


########## ***** Les pages et les methodes de l'administrateur systeme

# liste des agents sancfis

@droits_admin
@login_required(login_url='login')
def agentSancfis_page_admin(request):
       
    agentsancfis = AgentSancfis.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_agent_sancfis')

    context = {'agentsancfis': agentsancfis, 'utilisateur': utilisateur}
    return render(request, 'admin/admin_systeme.html', context)


# liste des assurances et des agents assurances

@droits_admin
@login_required(login_url='login')
def assurance_page_admin(request):

    assurances = Assurance.objects.all()
    utilisateur1 = User.objects.filter(groups__name='groupe_assurance')

    agentassurance = AgentAssurance.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_agent_assurance')
    
    context = {'agentassurance': agentassurance, 'utilisateur': utilisateur,
                'assurances': assurances, 'utilisateur1': utilisateur1}
    return render(request, 'admin/assurance.html', context)


# liste des assurés et des employés

@droits_admin
@login_required(login_url='login')
def assure_page_admin(request):
    
    assures = Assure.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_assure')

    employes = Employe.objects.all()
    
    context = {'assures': assures, 'employes': employes, 'utilisateur': utilisateur}
    return render(request, 'admin/assure.html', context)


# liste des agents pharmacies et des agents pharmacies

@droits_admin
@login_required(login_url='login')
def pharmacie_page_admin(request):

    pharmacies = Pharmacie.objects.all()
    utilisateur1 = User.objects.filter(groups__name='groupe_pharmacie')

    agentpharmacie = AgentPharmacie.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_agent_pharmacie')
    
    context = {'agentpharmacie': agentpharmacie, 'utilisateur': utilisateur,
                'pharmacies': pharmacies, 'utilisateur1': utilisateur1}
    return render(request, 'admin/pharmacies.html', context)


# liste des laboratoires et des agents des laboratoires

@droits_admin
@login_required(login_url='login')
def laboratoire_page_admin(request):

    laboratoires = Laboratoire.objects.all()
    utilisateur1 = User.objects.filter(groups__name='groupe_labo')

    agentlaboratoire = AgentLaboratoire.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_agent_labo')
    
    context = {'agentlaboratoire': agentlaboratoire, 'utilisateur': utilisateur,
                'laboratoires': laboratoires, 'utilisateur1': utilisateur1}
    return render(request, 'admin/labo.html', context)


# liste des centres de soins et des agents des centres de soins

@droits_admin
@login_required(login_url='login')
def centreSoins_page_admin(request):

    centredesoins = centreDeSoins.objects.all()
    utilisateur1 = User.objects.filter(groups__name='groupe_cs')

    agentcs = AgentCs.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_agent_cs')
    
    context = {'agentcs': agentcs, 'utilisateur': utilisateur,
                'centredesoins': centredesoins, 'utilisateur1': utilisateur1}
    return render(request, 'admin/centresdesoins.html', context)


# liste des souscripteurs

@droits_admin
@login_required(login_url='login')
def souscripteur_page_admin(request):

    souscripteurs = Souscripteur.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_souscripteur')

    context = {'souscripteurs': souscripteurs, 'utilisateur': utilisateur}
    return render(request, 'admin/souscripteurs.html', context)


########## ***** Les pages et les methodes des agents sancfis *****

@droits_utilisateur_type1(droit_agent_sancfis=['groupe_agent_sancfis'])
@login_required(login_url='login')
def acceuilSancfis(request):
       
    utilisateur = User.objects.filter(groups__name='groupe_agent_sancfis')

    context = {'utilisateur': utilisateur}
    return render(request, 'sancfis/acceuil.html', context)

@droits_utilisateur_type1(droit_agent_sancfis=['groupe_agent_sancfis'])
@login_required(login_url='login')
def assure_page_sancfis(request):
    
    assures = Assure.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_assure')

    employes = Employe.objects.all()
    
    context = {'assures': assures, 'employes': employes, 'utilisateur': utilisateur}
    return render(request, 'sancfis/assure.html', context)


@droits_utilisateur_type1(droit_agent_sancfis=['groupe_agent_sancfis'])
@login_required(login_url='login')
def pharmacie_page_sancfis(request):

    pharmacies = Pharmacie.objects.all()
    utilisateur1 = User.objects.filter(groups__name='groupe_pharmacie')

    agentpharmacie = AgentPharmacie.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_agent_pharmacie')
    
    context = {'agentpharmacie': agentpharmacie, 'utilisateur': utilisateur,
                'pharmacies': pharmacies, 'utilisateur1': utilisateur1}
    return render(request, 'sancfis/pharmacies.html', context)

@droits_utilisateur_type1(droit_agent_sancfis=['groupe_agent_sancfis'])
@login_required(login_url='login')
def laboratoire_page_sancfis(request):

    laboratoires = Laboratoire.objects.all()
    utilisateur1 = User.objects.filter(groups__name='groupe_labo')

    agentlaboratoire = AgentLaboratoire.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_agent_labo')
    
    context = {'agentlaboratoire': agentlaboratoire, 'utilisateur': utilisateur,
                'laboratoires': laboratoires, 'utilisateur1': utilisateur1}
    return render(request, 'sancfis/labo.html', context)

@droits_utilisateur_type1(droit_agent_sancfis=['groupe_agent_sancfis'])
@login_required(login_url='login')
def centreSoins_page_sancfis(request):

    centredesoins = centreDeSoins.objects.all()
    utilisateur1 = User.objects.filter(groups__name='groupe_cs')

    agentcs = AgentCs.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_agent_cs')
    
    context = {'agentcs': agentcs, 'utilisateur': utilisateur,
                'centredesoins': centredesoins, 'utilisateur1': utilisateur1}
    return render(request, 'sancfis/centresdesoins.html', context)

@droits_utilisateur_type1(droit_agent_sancfis=['groupe_agent_sancfis'])
@login_required(login_url='login')
def souscripteur_page_sancfis(request):

    souscripteurs = Souscripteur.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_souscripteur')

    context = {'souscripteurs': souscripteurs, 'utilisateur': utilisateur}
    return render(request, 'sancfis/souscripteurs.html', context)

@droits_utilisateur_type1(droit_agent_sancfis=['groupe_agent_sancfis'])
@login_required(login_url='login')
def agentSancfis_page(request):

    assurances = Assurance.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_assurance')

    context = {'assurances': assurances, 'utilisateur': utilisateur}
    return render(request, 'sancfis/agents_sancfis.html', context)

@droits_admin
def creerAgentSancfis(request):

    form = agentSancfisForm()
    form1 = creerUtillisateur()
    if request.method == "POST":
        form = agentSancfisForm(request.POST)
        form1 = creerUtillisateur(request.POST)


        if form.is_valid() and form1.is_valid():
            user = form1.save()
            
            form.save()

            email = form1.cleaned_data.get('email')

            groupe = Group.objects.get(name='groupe_agent_sancfis')
            user.groups.add(groupe)

            return redirect('/')


    context = {'form': form, 'form1': form1}
    return render(request, 'sancfis/agentSancfis_form.html', context)

@droits_utilisateur_type1(droit_agent_sancfis=['groupe_agent_sancfis', 'admin'])
@login_required(login_url='login')
def modifierAgentSancfis(request, pk):

    agentsancfis = AgentSancfis.objects.get(id=pk)
    form = agentSancfisForm(instance=agentsancfis)

    if request.method == "POST":
        form = agentSancfisForm(request.POST, instance=agentsancfis)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {'form': form}
    return render(request, 'sancfis/modifier_agentSancfis_form.html', context)

@droits_admin
@login_required(login_url='login')
def supprimerAgentSancfis(request, pk):

    agentsancfis = AgentSancfis.objects.get(id=pk)
    if request.method == "POST":
        agentsancfis.delete()
        return redirect('/agents_sancfis_admin/')

    context = {'item': agentsancfis}
    return render(request, 'sancfis/supprimerAgentSancfis_form.html', context)

def supprimerCompte_agentSancfis(request, pk):

    util = User.objects.get(id=pk)
    if request.method == "POST":
        util.delete()
        return redirect('/agents_sancfis_admin/')

    context = {'item': util}
    return render(request, 'auth/supprimerCompte_form.html', context)

# LES VUES ASSURANCE

@login_required(login_url='login')
@droits_utilisateur_type6(droit_assurance=['groupe_assurance'])
def assurance_page(request):

    agentassurance = AgentAssurance.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_agent_assurance')
    
    context = {'agentassurance': agentassurance, 'utilisateur': utilisateur}
    return render(request, 'assurance/assurance.html', context)

@droits_utilisateur_type1(droit_agent_sancfis=['groupe_agent_sancfis'])
def creerAssurance(request):
    
    form = assuranceForm()
    form1 = creerUtillisateur()
    if request.method == "POST":
        form = assuranceForm(request.POST)
        form1 = creerUtillisateur(request.POST)


        if form.is_valid() and form1.is_valid():
            util = form1.save()
            
            form.save()

            email = form1.cleaned_data.get('email')

            groupe = Group.objects.get(name='groupe_assurance')
            util.groups.add(groupe)

            return redirect('/agents_sancfis/')

    context = {'form': form, 'form1': form1}
    return render(request, 'assurance/assurance_form.html', context)

def modifierAssurance(request, pk):

    assurance = Assurance.objects.get(id=pk)
    form = assuranceForm(instance=assurance)

    if request.method == "POST":
        form = assuranceForm(request.POST, instance=assurance)
        if form.is_valid():
            form.save()
            return redirect("/agent_sancfis/")

    context = {'form': form}
    return render(request, 'assurance/modifier_assurance_form.html', context)

def supprimerAssurance(request, pk):

    assurance = Assurance.objects.get(id=pk)
    if request.method == "POST":
        assurance.delete()
        return redirect('/agent_sancfis/')

    context = {'item': assurance}
    return render(request, 'assurance/supprimerAssurance_form.html', context)

def supprimerCompte_assurance(request, pk):

    util = User.objects.get(id=pk)
    if request.method == "POST":
        util.delete()
        return redirect('/agent_sancfis/')

    context = {'item': util}
    return render(request, 'auth/supprimerCompte_form.html', context)


# LES VUES AGENTS ASSURANCE

@login_required(login_url='login')
@droits_utilisateur_type2(droit_agent_assurance=['groupe_agent_assurance'])
def agentAssurance_page(request):

    assures = Assure.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_assure')
    
    context = {'assures': assures, 'utilisateur': utilisateur}
    return render(request, 'assurance/agents_assurance.html', context)

@droits_utilisateur_type2(droit_agent_assurance=['groupe_agent_assurance'])
def souscripteur_page_agentAssurance(request):

    souscripteurs = Souscripteur.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_souscripteur')
    
    context = {'souscripteurs': souscripteurs, 'utilisateur': utilisateur}
    return render(request, 'assurance/souscripteurs.html', context)

@droits_utilisateur_type6(droit_assurance=['groupe_assurance'])
def creerAgentAssurance(request):
    
    form = agentAssuranceForm()
    form1 = creerUtillisateur()
    if request.method == "POST":
        form = agentAssuranceForm(request.POST)
        form1 = creerUtillisateur(request.POST)


        if form.is_valid() and form1.is_valid():
            util = form1.save()
            
            form.save()

            email = form1.cleaned_data.get('email')

            groupe = Group.objects.get(name='groupe_agent_assurance')
            util.groups.add(groupe)

            return redirect('/assurance/')

    context = {'form': form, 'form1': form1}
    return render(request, 'assurance/agentAssurance_form.html', context)

def modifierAgentAssurance(request, pk):

    agentAssurance = AgentAssurance.objects.get(id=pk)
    form = agentAssuranceForm(instance=agentAssurance)

    if request.method == "POST":
        form = agentAssuranceForm(request.POST, instance=agentAssurance)
        if form.is_valid():
            form.save()
            return redirect("/agent_assurance_assurance/")

    context = {'form': form}
    return render(request, 'assurance/modifier_agentAssurance_form.html', context)

def supprimerAgentAssurance(request, pk):

    agentAssurance = AgentAssurance.objects.get(id=pk)
    if request.method == "POST":
        agentAssurance.delete()
        return redirect('/agent_assurance_assurance/')

    context = {'item': agentAssurance}
    return render(request, 'assurance/supprimerAgentAssurance_form.html', context)

def supprimerCompte_agentAssurance(request, pk):

    util = User.objects.get(id=pk)
    if request.method == "POST":
        util.delete()
        return redirect('/agent_assurance_assurance/')

    context = {'item': util}
    return render(request, 'auth/supprimerCompte_form.html', context)

# LES VUES ASSURE

@login_required(login_url='login')
@droits_utilisateur_type7(droit_assure=['groupe_assure'])
def assure_page(request):
    
    context = {}
    return render(request, 'assure/assure.html', context)

@droits_utilisateur_type2(droit_agent_assurance=['groupe_agent_assurance'])
def creerAssure(request):
    
    form = assureForm()
    form1 = creerUtillisateur()
    if request.method == "POST":
        form = assureForm(request.POST)
        form1 = creerUtillisateur(request.POST)


        if form.is_valid() and form1.is_valid():
            util = form1.save()
            
            form.save()

            email = form1.cleaned_data.get('email')

            groupe = Group.objects.get(name='groupe_assure')
            util.groups.add(groupe)

            messages.success(request, 'Compte crée pour' + email)


            return redirect('/assure_agent_assurance/')

    context = {'form': form, 'form1': form1}
    return render(request, 'assure/assure_form.html', context)

def modifierAssure(request, pk):

    assure = Assure.objects.get(id=pk)
    form = assureForm(instance=assure)

    if request.method == "POST":
        form = assureForm(request.POST, instance=assure)
        if form.is_valid():
            form.save()
            return redirect("/assure_agent_assurance/")

    context = {'form': form}
    return render(request, 'assure/modifier_assure_form.html', context)

def supprimerAssure(request, pk):

    assure = Assure.objects.get(id=pk)
    if request.method == "POST":
        assure.delete()
        return redirect('/assure_agent_assurance/')

    context = {'item': assure}
    return render(request, 'assure/supprimerAssure_form.html', context)

def supprimerCompte_assure(request, pk):

    util = User.objects.get(id=pk)
    if request.method == "POST":
        util.delete()
        return redirect('/assure_agent_assurance/')

    context = {'item': util}
    return render(request, 'auth/supprimerCompte_form.html', context)

# LES VUES PHARMACIES

@login_required(login_url='login')
@droits_utilisateur_type8(droit_pharmacie=['groupe_pharmacie'])
def pharmacie_page(request):

    agentpharmacie = AgentPharmacie.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_agent_pharmacie')
    
    context = {'agentpharmacie': agentpharmacie, 'utilisateur': utilisateur}
    return render(request, 'pharmacie/pharmacies.html', context)

@droits_utilisateur_type1(droit_agent_sancfis=['groupe_agent_sancfis'])
def creerPharmacie(request):
    
    form = pharmacieForm()
    form1 = creerUtillisateur()
    if request.method == "POST":
        form = pharmacieForm(request.POST)
        form1 = creerUtillisateur(request.POST)


        if form.is_valid() and form1.is_valid():
            util = form1.save()
            
            form.save()

            email = form1.cleaned_data.get('email')

            groupe = Group.objects.get(name='groupe_pharmacie')
            util.groups.add(groupe)

            messages.success(request, 'Compte crée pour' + email)


            return redirect('/pharmacie_sancfis/')

    context = {'form': form, 'form1': form1}
    return render(request, 'pharmacie/pharmacie_form.html', context)

def modifierPharmacie(request, pk):

    pharmacie = Pharmacie.objects.get(id=pk)
    form = pharmacieForm(instance=pharmacie)

    if request.method == "POST":
        form = pharmacieForm(request.POST, instance=pharmacie)
        if form.is_valid():
            form.save()
            return redirect("/pharmacie_sancfis/")

    context = {'form': form}
    return render(request, 'pharmacie/modifier_pharmacie_form.html', context)

def supprimerPharmacie(request, pk):

    pharmacie = Pharmacie.objects.get(id=pk)
    if request.method == "POST":
        pharmacie.delete()
        return redirect('/pharmacie_sancfis/')

    context = {'item': pharmacie}
    return render(request, 'pharmacie/supprimerPharmacie_form.html', context)

def supprimerCompte_pharmacie(request, pk):

    util = User.objects.get(id=pk)
    if request.method == "POST":
        util.delete()
        return redirect('/pharmacie_sancfis/')

    context = {'item': util}
    return render(request, 'auth/supprimerCompte_form.html', context)

# LES VUES AGENTS PHARMACIES

@login_required(login_url='login')
@droits_utilisateur_type5(droit_agent_pharmacie=['groupe_agent_pharmacie'])
def agentPharmacie_page(request):

    assure = Assure.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_assure')
    
    context = {'assure': assure, 'utilisateur': utilisateur}
    return render(request, 'pharmacie/agents_pharmacie.html', context)

def creerAgentPharmacie(request):
    
    form = agentPharmacieForm()
    form1 = creerUtillisateur()
    if request.method == "POST":
        form = agentPharmacieForm(request.POST)
        form1 = creerUtillisateur(request.POST)


        if form.is_valid() and form1.is_valid():
            util = form1.save()
            
            form.save()

            email = form1.cleaned_data.get('email')

            groupe = Group.objects.get(name='groupe_agent_pharmacie')
            util.groups.add(groupe)

            messages.success(request, 'Compte crée pour' + email)


            return redirect('/agent_pharmacie_pharmacie/')

    context = {'form': form, 'form1': form1}
    return render(request, 'pharmacie/agentPharmacie_form.html', context)

def modifierAgentPharmacie(request, pk):

    agentPharmacie = AgentPharmacie.objects.get(id=pk)
    form = agentPharmacieForm(instance=agentPharmacie)

    if request.method == "POST":
        form = agentPharmacieForm(request.POST, instance=agentPharmacie)
        if form.is_valid():
            form.save()
            return redirect("/agent_pharmacie_pharmacie/")

    context = {'form': form}
    return render(request, 'pharmacie/modifier_agentPharmacie_form.html', context)

def supprimerAgentPharmacie(request, pk):

    agentPharmacie = AgentPharmacie.objects.get(id=pk)
    if request.method == "POST":
        agentPharmacie.delete()
        return redirect('/agent_pharmacie_pharmacie/')

    context = {'item': agentPharmacie}
    return render(request, 'pharmacie/supprimerAgentPharmacie_form.html', context)

def supprimerCompte_pharmacie(request, pk):

    util = User.objects.get(id=pk)
    if request.method == "POST":
        util.delete()
        return redirect('/agent_pharmacie_pharmacie/')

    context = {'item': util}
    return render(request, 'auth/supprimerCompte_form.html', context)
    
# LES VUES LABORATOIRES

@login_required(login_url='login')
@droits_utilisateur_type9(droit_laboratoire=['groupe_laboratoire'])
def laboratoire_page(request):

    agentlaboratoire = AgentLaboratoire.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_agent_labo')
    
    context = {'agentlaboratoire': agentlaboratoire, 'utilisateur': utilisateur}
    return render(request, 'labo/labo.html', context)

@droits_utilisateur_type1(droit_agent_sancfis=['groupe_agent_sancfis'])
def creerLaboratoire(request):
    
    form = laboratoireForm()
    form1 = creerUtillisateur()
    if request.method == "POST":
        form = laboratoireForm(request.POST)
        form1 = creerUtillisateur(request.POST)


        if form.is_valid() and form1.is_valid():
            util = form1.save()
            
            form.save()

            email = form1.cleaned_data.get('email')

            groupe = Group.objects.get(name='groupe_laboratoire')
            util.groups.add(groupe)

            return redirect('/laboratoire_sancfis/')

    context = {'form': form, 'form1': form1}
    return render(request, 'labo/labo_form.html', context)

def modifierLaboratoire(request, pk):

    laboratoire = Laboratoire.objects.get(id=pk)
    form = laboratoireForm(instance=laboratoire)

    if request.method == "POST":
        form = laboratoireForm(request.POST, instance=laboratoire)
        if form.is_valid():
            form.save()
            return redirect("/laboratoire_sancfis/")

    context = {'form': form}
    return render(request, 'labo/modifier_labo_form.html', context)

def supprimerLaboratoire(request, pk):

    labo = Laboratoire.objects.get(id=pk)
    if request.method == "POST":
        labo.delete()
        return redirect('/laboratoire_sancfis/')

    context = {'item': labo}
    return render(request, 'labo/supprimerLabo_form.html', context)

def supprimerCompte_laboratoire(request, pk):

    util = User.objects.get(id=pk)
    if request.method == "POST":
        util.delete()
        return redirect('/laboratoire_sancfis/')

    context = {'item': util}
    return render(request, 'auth/supprimerCompte_form.html', context)

# LES VUES AGENTS LABORATOIRES

@login_required(login_url='login')
@droits_utilisateur_type3(droit_agent_labo=['groupe_agent_labo'])
def agentLaboratoire_page(request):

    assures = Assure.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_assure')
    
    context = {'assures': assures, 'utilisateur': utilisateur}
    return render(request, 'labo/agents_labo.html', context)

def creerAgentLaboratoire(request):
    
    form = agentLaboratoireForm()
    form1 = creerUtillisateur()
    if request.method == "POST":
        form = agentLaboratoireForm(request.POST)
        form1 = creerUtillisateur(request.POST)


        if form.is_valid() and form1.is_valid():
            util = form1.save()
            
            form.save()

            email = form1.cleaned_data.get('email')

            groupe = Group.objects.get(name='groupe_agent_labo')
            util.groups.add(groupe)

            return redirect('/agent_laboratoire_laboratoire/')

    context = {'form': form, 'form1': form1}
    return render(request, 'labo/agentLabo_form.html', context)

def modifierAgentLabo(request, pk):

    agentLabo = AgentLaboratoire.objects.get(id=pk)
    form = agentLaboratoireForm(instance=agentLabo)

    if request.method == "POST":
        form = agentLaboratoireForm(request.POST, instance=agentLabo)
        if form.is_valid():
            form.save()
            return redirect("/agent_laboratoire_laboratoire/")

    context = {'form': form}
    return render(request, 'labo/modifier_agentLabo_form.html', context)

def supprimerAgentLabo(request, pk):

    agentLabo = AgentLabo.objects.get(id=pk)
    if request.method == "POST":
        agentLabo.delete()
        return redirect('/agent_laboratoire_laboratoire/')

    context = {'item': agentLabo}
    return render(request, 'labo/supprimerAgentLabo_form.html', context)

def supprimerCompte_agentLabo(request, pk):

    util = User.objects.get(id=pk)
    if request.method == "POST":
        util.delete()
        return redirect('/agent_laboratoire_laboratoire/')

    context = {'item': util}
    return render(request, 'auth/supprimerCompte_form.html', context)


# LES VUES CENTRES DE SOINS

@login_required(login_url='login')
@droits_utilisateur_type10(droit_cs=['groupe_cs'])
def centreSoins_page(request):

    agentcs = AgentCs.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_agent_cs')
    
    context = {'agentcs': agentcs, 'utilisateur': utilisateur}
    return render(request, 'cs/centresdesoins.html', context)

@droits_utilisateur_type1(droit_agent_sancfis=['groupe_agent_sancfis'])
def creerCentreSoins(request):
    
    form = csForm()
    form1 = creerUtillisateur()
    if request.method == "POST":
        form = csForm(request.POST)
        form1 = creerUtillisateur(request.POST)


        if form.is_valid() and form1.is_valid():
            util = form1.save()
            
            form.save()

            email = form1.cleaned_data.get('email')

            groupe = Group.objects.get(name='groupe_cs')
            util.groups.add(groupe)

            return redirect('/centre_soins_sancfis/')

    context = {'form': form, 'form1': form1}
    return render(request, 'cs/cs_form.html', context)

def modifierCentreSoins(request, pk):

    cs = centreDeSoins.objects.get(id=pk)
    form = csForm(instance=cs)

    if request.method == "POST":
        form = csForm(request.POST, instance=cs)
        if form.is_valid():
            form.save()
            return redirect("/centre_soins_sancfis/")

    context = {'form': form}
    return render(request, 'cs/modifier_cs_form.html', context)

def supprimerCentreSoins(request, pk):

    cs = centreDeSoins.objects.get(id=pk)
    if request.method == "POST":
        cs.delete()
        return redirect('/centre_soins_sancfis/')

    context = {'item': cs}
    return render(request, 'cs/supprimerCs_form.html', context)

def supprimerCompte_centreSoins(request, pk):

    util = User.objects.get(id=pk)
    if request.method == "POST":
        util.delete()
        return redirect('/centre_soins_sancfis/')

    context = {'item': util}
    return render(request, 'auth/supprimerCompte_form.html', context)

# LES VUES AGENTS CENTRES DE SOINS

@login_required(login_url='login')
@droits_utilisateur_type4(droit_agent_cs=['groupe_agent_cs'])
def agentCs_page(request):

    assures = Assure.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_assure')
    
    context = {'assures': assures, 'utilisateur': utilisateur}
    return render(request, 'cs/agents_cs.html', context)

def creerAgentCs(request):
    
    form = agentCsForm()
    form1 = creerUtillisateur()
    if request.method == "POST":
        form = agentCsForm(request.POST)
        form1 = creerUtillisateur(request.POST)


        if form.is_valid() and form1.is_valid():
            util = form1.save()
            
            form.save()

            email = form1.cleaned_data.get('email')

            groupe = Group.objects.get(name='groupe_agent_cs')
            util.groups.add(groupe)

            return redirect('/agent_cs_centre_soins/')

    context = {'form': form, 'form1': form1}
    return render(request, 'cs/agentCs_form.html', context)

def modifierAgentCs(request, pk):

    agentCs = AgentCs.objects.get(id=pk)
    form = agentCsForm(instance=agentCs)

    if request.method == "POST":
        form = agentCsForm(request.POST, instance=agentCs)
        if form.is_valid():
            form.save()
            return redirect("/agent_cs_centre_soins/")

    context = {'form': form}
    return render(request, 'cs/modifier_agentCs_form.html', context)

def supprimerAgentCs(request, pk):

    agentCs = AgentCs.objects.get(id=pk)
    if request.method == "POST":
        agentCs.delete()
        return redirect('/agent_cs_centre_soins/')

    context = {'item': agentCs}
    return render(request, 'cs/supprimerAgentCs_form.html', context)

def supprimerCompte_agentCs(request, pk):

    util = User.objects.get(id=pk)
    if request.method == "POST":
        util.delete()
        return redirect('/agent_cs_centre_soins/')

    context = {'item': util}
    return render(request, 'auth/supprimerCompte_form.html', context)

# LES VUES SOUSCRIPTEURS

@login_required(login_url='login')
@droits_utilisateur_type11(droit_souscripteur=['goupe_souscripteur'])
def souscripteur_page(request):

    assures = Assure.objects.all()
    employes = Employe.objects.all()
    
    context = {'assures': assures, 'employes': employes}
    return render(request, 'souscripteur/souscripteurs.html', context)

def creerSouscripteur(request):
    
    form = souscripteurForm()
    form1 = creerUtillisateur()
    if request.method == "POST":
        form = souscripteurForm(request.POST)
        form1 = creerUtillisateur(request.POST)


        if form.is_valid() and form1.is_valid():
            util = form1.save()
            
            form.save()

            email = form1.cleaned_data.get('email')

            groupe = Group.objects.get(name='groupe_souscripteur')
            util.groups.add(groupe)

            return redirect('/souscripteur_agent_assurance/')

    context = {'form': form, 'form1': form1}
    return render(request, 'souscripteur/souscripteur_form.html', context)

def modifierSouscripteur(request, pk):

    souscripteur = Souscripteur.objects.get(id=pk)
    form = souscripteurForm(instance=souscripteur)

    if request.method == "POST":
        form = souscripteurForm(request.POST, instance=souscripteur)
        if form.is_valid():
            form.save()
            return redirect("/souscripteur_agent_assurance/")

    context = {'form': form}
    return render(request, 'souscripteur/modifier_souscripteur_form.html', context)

def supprimerSouscripteur(request, pk):

    souscripteur = Souscripteur.objects.get(id=pk)
    if request.method == "POST":
        souscripteur.delete()
        return redirect('/souscripteur_agent_assurance/')

    context = {'item': souscripteur}
    return render(request, 'souscripteur/supprimerSouscripteur_form.html', context)

def supprimerCompte_souscripteur(request, pk):

    util = User.objects.get(id=pk)
    if request.method == "POST":
        util.delete()
        return redirect('/souscripteur_agent_assurance/')

    context = {'item': util}
    return render(request, 'auth/supprimerCompte_form.html', context)

# LES VUES EMPLOYES

@login_required(login_url='login')
def employe_page(request):
    
    context = {}
    return render(request, 'employe/employe.html', context)

def creerEmploye(request):
    
    form = employeForm()
    if request.method == "POST":
        form = employeForm(request.POST)


        if form.is_valid():            
            form.save()

            return redirect('/employe_souscripteur/')

    context = {'form': form}
    return render(request, 'employe/employe_form.html', context)

def modifierEmploye(request, pk):
    
    employe = Employe.objects.get(id=pk)
    form = employeForm(instance=employe)
    if request.method == "POST":
        form = employeForm(request.POST, instance=employe)


        if form.is_valid():            
            form.save()

            return redirect('/employe_souscripteur/')

    context = {'form': form}
    return render(request, 'employe/employe_form.html', context)

def supprimerEmploye(request, pk):

    employe = Employe.objects.get(id=pk)
    if request.method == "POST":
        employe.delete()
        return redirect('/employe_souscripteur/')

    context = {'item': employe}
    return render(request, 'employe/supprimerAgentSancfis_form.html', context)

