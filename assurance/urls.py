from django.contrib import admin
from django.urls import path, include
from assurance import *
from assurance import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    ### URLS authentification

    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),

    #path('logout/', auth_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),

    path('logout/', views.deconnecter, name="logout"),

    path('supprimer_compte/<int:pk>/', views.supprimerCompte, name="supprimer_compte"),


    #path('connecter/', views.connecter, name="connecter"),
    
    ### URLS des Pages de redirections

    path('', views.acceuil, name="acceuil"),
    path('agents_sancfis_admin/', views.agentSancfis_page_admin, name="agent_sancfis_admin"),
    path('assurance_admin/', views.assurance_page_admin, name="assurance_admin"),
    path('centre_soins_admin/', views.centreSoins_page_admin, name="centre_soins_admin"),
    path('pharmacie_admin/', views.pharmacie_page_admin, name="pharmacie_admin"),
    path('laboratoire_admin/', views.laboratoire_page_admin, name="laboratoire_admin"),
    path('assure_admin/', views.assure_page_admin, name="assure_admin"),
    path('souscripteur_admin/', views.souscripteur_page_admin, name="souscripteur_admin"),

    # URLs de creation des tables granulaires

    path('table_granulaire/', views.tableGranulaire, name="table_granulaire"),

    # URLs de modification des tables granulaires

    path('modifier_ville/<int:pk>/', views.modifierVille, name="modifier_ville"),
    path('modifier_prestation/<int:pk>/', views.modifierPrestation, name="modifier_prestation"),
    path('modifier_examen/<int:pk>/', views.modifierExamen, name="modifier_examen"),
    path('modifier_consultation/<int:pk>/', views.modifierConsultation, name="modifier_consultation"),
    path('modifier_med/<int:pk>/', views.modifierMedicament, name="modifier_med"),
    path('modifier_taille/<int:pk>/', views.modifierTaille, name="modifier_taille"),
    path('modifier_quantite/<int:pk>/', views.modifierQuantite, name="modifier_quantite"),
    path('modifier_forme/<int:pk>/', views.modifierForme, name="modifier_forme"),
    path('modifier_moment/<int:pk>/', views.modifierMoment, name="modifier_moment"),
    path('modifier_periode/<int:pk>/', views.modifierPeriode, name="modifier_periode"),
    path('modifier_profession/<int:pk>/', views.modifierProfession, name="modifier_profession"),
    path('modifier_masse/<int:pk>/', views.modifierMasse, name="modifier_masse"),
    path('modifier_nbr/<int:pk>/', views.modifierNombre, name="modifier_nbr"),
    path('modifier_unite/<int:pk>/', views.modifierUnite, name="modifier_unite"),
    path('modifier_frequence/<int:pk>/', views.modifierFrequence, name="modifier_frequence"),
    path('modifier_specialite/<int:pk>/', views.modifierSpecialite, name="modifier_specialite"),
    path('modifier_voie/<int:pk>/', views.modifierVoieAdmin, name="modifier_voie"),

    # URLs de suppression des tables granulaires

    path('supprimer_ville/<int:pk>/', views.supprimerVille, name="supprimer_ville"),
    path('supprimer_prestation/<int:pk>/', views.supprimerPrestation, name="supprimer_prestation"),
    path('supprimer_examen/<int:pk>/', views.supprimerExamen, name="supprimer_examen"),
    path('supprimer_consultation/<int:pk>/', views.supprimerConsultation, name="supprimer_consultation"),
    path('supprimer_med/<int:pk>/', views.supprimerMedicament, name="supprimer_med"),
    path('supprimer_taille/<int:pk>/', views.supprimerTaille, name="supprimer_taille"),
    path('supprimer_quantite/<int:pk>/', views.supprimerQuantite, name="supprimer_quantite"),
    path('supprimer_forme/<int:pk>/', views.supprimerForme, name="supprimer_forme"),
    path('supprimer_moment/<int:pk>/', views.supprimerMoment, name="supprimer_moment"),
    path('supprimer_periode/<int:pk>/', views.supprimerPeriode, name="supprimer_periode"),
    path('supprimer_profession/<int:pk>/', views.supprimerProfession, name="supprimer_profession"),
    path('supprimer_masse/<int:pk>/', views.supprimerMasse, name="supprimer_masse"),
    path('supprimer_nbr/<int:pk>/', views.supprimerNombre, name="supprimer_nbr"),
    path('supprimer_unite/<int:pk>/', views.supprimerUnite, name="supprimer_unite"),
    path('supprimer_frequence/<int:pk>/', views.supprimerFrequence, name="supprimer_frequence"),
    path('supprimer_specialite/<int:pk>/', views.supprimerSpecialite, name="supprimer_specialite"),
    path('supprimer_voie/<int:pk>/', views.supprimerVoieAdmin, name="supprimer_voie"),

    path('acceuil_sancfis/', views.acceuilSancfis, name="acceuil_sancfis"),
    path('agents_sancfis/', views.agentSancfis_page, name="agent_sancfis"),
    path('centre_soins_sancfis/', views.centreSoins_page_sancfis, name="centre_soins_sancfis"),
    path('pharmacie_sancfis/', views.pharmacie_page_sancfis, name="pharmacie_sancfis"),
    path('laboratoire_sancfis/', views.laboratoire_page_sancfis, name="laboratoire_sancfis"),
    path('assure_sancfis/', views.assure_page_sancfis, name="assure_sancfis"),
    path('souscripteur_sancfis/', views.souscripteur_page_sancfis, name="souscripteur_sancfis"),

    path('assurance/', views.assurance_page, name="assurance"),

    path('centre_soins/', views.centreSoins_page, name="centre_soins"),

    path('pharmacie/', views.pharmacie_page, name="pharmacie"),

    path('laboratoire/', views.laboratoire_page, name="laboratoire"),

    path('assure/', views.assure_page, name="assure"),

    path('souscripteur/', views.souscripteur_page, name="souscripteur"),

    path('agent_assurance/', views.agentAssurance_page, name="agent_assurance"),

    path('agent_cs/', views.agentCs_page, name="agent_cs"),

    path('agent_pharmacie/', views.agentPharmacie_page, name="agent_pharmacie"),

    path('agent_laboratoire/', views.agentLaboratoire_page, name="agent_laboratoire"),

    path('employe/', views.employe_page, name="employe"),

    ### URLS des Methodes

    # AGENTS SANCFIS

    path('creer_agent_sancfis/', views.creerAgentSancfis, name="creer_agent_sancfis"),
    path('modifier_agent_sancfis/<int:pk>/', views.modifierAgentSancfis, name="modifier_agent_sancfis"),
    path('supprimer_agent_sancfis/<int:pk>/', views.supprimerAgentSancfis, name="supprimer_agent_sancfis"),

    # AGENTS ASSURANCE

    path('creer_agent_assurance/', views.creerAgentAssurance, name="creer_agent_assurance"),
    path('modifier_agent_assurance/<int:pk>/', views.modifierAssurance, name="modifier_agent_assurance"),
    path('supprimer_agent_assurance/<int:pk>/', views.supprimerAssurance, name="supprimer_agent_assurance"),

    # AGENT CENTRES DE SOINS

    path('creer_agent_cs/', views.creerAgentCs, name="creer_agent_cs"),
    path('modifier_agent_cs/<int:pk>/', views.modifierAgentCs, name="modifier_agent_cs"),
    path('supprimer_agent_cs/<int:pk>/', views.supprimerAgentCs, name="supprimer_agent_cs"),

    # AGENTS PHARMACIES

    path('creer_agent_pharmacie/', views.creerAgentPharmacie, name="creer_agent_pharmacie"),
    path('modifier_agent_pharmacie/<int:pk>/', views.modifierAgentPharmacie, name="modifier_agent_pharmacie"),
    path('supprimer_agent_pharmacie/<int:pk>/', views.supprimerAgentPharmacie, name="supprimer_agent_pharmacie"),

    # AGENTS LABORATOIRES

    path('creer_agent_laboratoire/', views.creerAgentLaboratoire, name="creer_agent_laboratoire"),
    path('modifier_agent_laboratoire/<int:pk>/', views.modifierAgentLabo, name="modifier_agent_laboratoire"),
    path('supprimer_agent_laboratoire/<int:pk>/', views.supprimerAgentLabo, name="supprimer_agent_laboratoire"),

    # CENTRES DE SOINS

    path('creer_cs/', views.creerCentreSoins, name="creer_cs"),
    path('modifier_cs/<int:pk>/', views.modifierCentreSoins, name="modifier_cs"),
    path('supprimer_cs/<int:pk>/', views.supprimerCentreSoins, name="supprimer_cs"),

    # ASSURANCES

    path('creer_assurance/', views.creerAssurance, name="creer_assurance"),
    path('modifier_assurance/<int:pk>/', views.modifierAssurance, name="modifier_assurance"),
    path('supprimer_assurance/<int:pk>/', views.supprimerAssurance, name="supprimer_assurance"),

    # PHARMACIES

    path('creer_pharmacie/', views.creerPharmacie, name="creer_pharmacie"),
    path('modifier_pharmacie/<int:pk>/', views.modifierPharmacie, name="modifier_pharmacie"),
    path('supprimer_pharmacie/<int:pk>/', views.supprimerPharmacie, name="supprimer_pharmacie"),

    # LABORATOIRES

    path('creer_laboratoire/', views.creerLaboratoire, name="creer_laboratoire"),
    path('modifier_laboratoire/<int:pk>/', views.modifierLaboratoire, name="modifier_laboratoire"),
    path('supprimer_laboratoire/<int:pk>/', views.supprimerLaboratoire, name="supprimer_laboratoire"),

    # ASSURES

    path('creer_assure/', views.creerAssure, name="creer_assure"),
    path('modifier_assure/<int:pk>/', views.modifierAssure, name="modifier_assure"),
    path('supprimer_assure/<int:pk>/', views.supprimerAssure, name="supprimer_assure"),

    # SOUSCRIPTEUR

    path('creer_souscripteur/', views.creerSouscripteur, name="creer_souscripteur"),
    path('modifier_souscripteur/<int:pk>/', views.modifierSouscripteur, name="modifier_souscripteur"),
    path('supprimer_souscripteur/<int:pk>/', views.supprimerSouscripteur, name="supprimer_souscripteur"),

    # EMPLOYES

    path('creer_employe/', views.creerEmploye, name="creer_employe"),
    path('modifier_employe/<int:pk>/', views.supprimerEmploye, name="modifier_employe"),
    path('supprimer_employe/<int:pk>/', views.supprimerEmploye, name="supprimer_employe"),
]


