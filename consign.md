## Netfix

### Objectifs

Imaginez qu'il existe un endroit où vous pourriez demander à quelqu'un de réparer votre bidet tout en demandant en même temps un service pour peindre les murs de votre maison. Et pendant que vous y êtes, le ménage à la maison serait très pratique. Eh bien, dans ce projet, vous aiderez à créer un site web où tout cela, et bien plus encore, sera possible.

Ce site web est encore en cours de création, donc toutes les fonctionnalités ne sont pas encore disponibles. Vous allez implémenter certaines des fonctionnalités manquantes.

Vous devez également savoir que le site web est en cours de création avec Django, un framework Python pour le développement web. Vous pouvez en savoir plus sur ce framework sur son propre [site web](https://www.djangoproject.com/). Oui, vous allez jongler avec Python, alors soyez attentif à l'indentation. De plus, sachez que ce projet a été construit avec la version `v3.1.14` de Django, donc si vous avez des problèmes pour exécuter ce projet, veuillez vérifier votre version actuelle de Django et apporter les modifications nécessaires pour faire fonctionner le projet.

### Instructions

Le site web devrait contenir deux types d'utilisateurs :

- Entreprise : qui peut créer de nouveaux services
- Client : qui peut demander des services existants

Les deux utilisateurs devraient être en mesure de s'inscrire et de se connecter. Pour se connecter, les utilisateurs doivent entrer leur adresse e-mail et leur mot de passe. Cependant, pour s'inscrire, chaque type d'utilisateur doit fournir des informations différentes :

- Client :
    - e-mail
    - mot de passe
    - confirmation du mot de passe
    - nom d'utilisateur
    - date de naissance
- Entreprise :
    - e-mail
    - mot de passe
    - confirmation du mot de passe
    - nom d'utilisateur
    - domaine d'activité

> Chaque utilisateur doit avoir un e-mail et un nom d'utilisateur uniques. Ainsi, lors de l'inscription, un utilisateur doit être averti si l'e-mail et/ou le nom d'utilisateur ont déjà été enregistrés.

Chaque utilisateur devrait avoir sa propre page de profil sur laquelle ses informations devraient être affichées (à l'exception du mot de passe, évidemment). Et, dans le cas où l'utilisateur est un client, tous les services demandés précédemment doivent également être affichés. Dans le cas d'un profil d'entreprise, en plus de toutes leurs informations, les services qu'elle propose doivent également être présents.

L'attribut `domaine d'activité` des entreprises limitera le type de services qu'elle peut fournir. L'attribut `domaine d'activité` ne devrait accepter que ces valeurs :

- Climatisation
- Tout en un
- Menuiserie
- Électricité
- Jardinage
- Machines domestiques
- Ménage
- Design intérieur
- Serrures
- Peinture
- Plomberie
- Chauffe-eau

Une entreprise de `Menuiserie` ne peut créer que des services de menuiserie, tout comme une entreprise de `Ménage` ne peut fournir que des services de ménage. Cependant, les entreprises `Tout en un` peuvent créer n'importe quel type de services. Mais que contient un service ? Un service doit avoir :

- nom
- description
- domaine (peut avoir les mêmes catégories de domaines que les entreprises, sauf qu'un service Tout en un n'est pas autorisé)
- prix par heure
- date de création (cet attribut devrait automatiquement prendre une valeur lors de la création d'un service)

Le site web devrait avoir une page affichant les services les plus demandés. Il devrait également y avoir une page montrant tous les services dans l'ordre de création (les derniers créés en premier) et une page pour chaque catégorie de service, qui affiche les services disponibles pour cette catégorie.

Chaque service devrait avoir sa propre page, sur laquelle devraient être affichées les informations mentionnées ci-dessus ainsi que le nom de l'entreprise qui fournit ce service. Un utilisateur devrait pouvoir vérifier tous les services de cette entreprise en cliquant sur le nom affiché et voir le profil de l'entreprise.

Une fois qu'un service est créé par une entreprise, chaque utilisateur y a accès. Seuls les clients peuvent demander un service en fournissant l'`adresse` où le service est requis et le `temps de service` (en heures) nécessaire pour que le service soit terminé. Une fois qu'un client demande un service, il est ajouté à la liste des services demandés précédemment. Dans cette liste, pour chaque service demandé, le client peut voir le nom du service, le domaine du service, le coût du service calculé, la date à laquelle le service a été demandé et l'entreprise qui a fourni le service.

Vous pouvez consulter cette [vidéo](https://youtu.be/GyRo3CUWQzE) pour voir à quoi vous attendre de votre projet.

#### Django

Maintenant que vous savez de quoi parle le projet, nous allons vous expliquer l'architecture du système de fichiers. Un projet Django est organisé par un dossier principal du projet et différents modules.

En démarrant un nouveau projet Django (avec la commande `django-admin startproject <// nom du projet \\>`), le dossier principal (qui porte le même nom que le projet) et un fichier appelé `manage.py` sont créés. Ce fichier est utilisé pour exécuter diverses commandes. Les plus courantes sont :

- `python3 manage.py runserver` -> exécute un serveur sur le port 8000 par défaut, et sert votre projet.
- `python3 manage.py startapp <// nom du module \\>` -> crée un module, en d'autres termes, crée un répertoire avec la plupart des fichiers nécessaires pour un module.
- `python3 manage.py makemigrations` et `python3 manage.py migrate` -> ces deux commandes vont toujours de pair. Nous les utilisons pour déclarer les modifications apportées à la base de données Django (généralement effectuées dans le fichier `models.py` de chaque module).
- `python3 manage.py createsuperuser` -> crée un super utilisateur (administrateur) qui peut accéder et modifier les informations dans la base de données Django (accessible à l'URL `localhost:8000/admin`).
- `python3 manage.py` -> pour obtenir une liste de toutes les commandes disponibles.

> Vous remarquerez peut-être que nous utilisons la commande `python3`. Vous pourriez simplement utiliser la commande `python`, mais vous devez avoir la version 3.0 ou supérieure install

ée.

Chaque module est généralement lié à un aspect différent du projet. Par exemple, dans ce projet, il y a trois modules :

- services: gère les fonctionnalités essentielles liées aux services (création de service, affichage des services, demande de service ...)
- users: gère les fonctionnalités essentielles liées aux utilisateurs (inscription d'utilisateur, profil d'utilisateur, connexion d'utilisateur ...)
- main: gère les informations communes à tout le projet (page d'accueil, barre de navigation, page de déconnexion ...)

Par défaut, lors du démarrage d'un module, Django crée plusieurs fichiers qui sont très utiles pour le développement d'un site web. Ceux dans lesquels nous passons le plus de temps sont :

- `models.py` -> où vous pouvez ajouter des objets et définir leurs attributs dans la base de données Django
- `views.py` -> où vous pouvez manipuler le backend d'une page web sur le projet

En plus de ces deux fichiers, en règle générale, d'autres fichiers sont créés manuellement :

- `urls.py` -> ici, vous pouvez spécifier les URL de votre projet et les associer à une vue (du fichier `views.py`), afin d'afficher une page web. Par exemple, l'URL `profile/` est associée à la vue `views.ProfileView`)
- `forms.py` -> ici, vous pouvez créer vos formulaires à utiliser dans votre fichier `views.py`. Par exemple, vous pouvez créer un formulaire de connexion par défaut à utiliser dans la `LoginView` (présente dans le fichier `views.py`).

Généralement, nous créons également un dossier où nous pouvons stocker les modèles (en HTML). Ce dossier suit généralement la structure suivante :

```sh
netfix/                     # répertoire du projet
  ⌊ users/                  # répertoire du module users
    ⌊ __pycache__/
    ⌊ migrations/
    ⌊ templates/            # répertoire du modèle users
      ⌊ users/
        ⌊ login.html
        ⌊ profile.html
        ⌊ register.html
        ⌊   ...
    ⌊   ...
    ⌊ urls.py
    ⌊ views.py
```

Vous utiliserez également ce qui est appelé `templates Django`, qui est utilisé à l'intérieur des fichiers HTML. C'est une façon de coder à l'intérieur du HTML, permettant de parcourir les objets transmis (boucle for) ou même de faire des vérifications conditionnelles (instruction if/else), entre autres choses intéressantes. Pour en savoir plus à ce sujet, vous pouvez consulter la [documentation des templates Django](https://docs.djangoproject.com/en/3.1/topics/templates/).

Vous pouvez obtenir le code qui est déjà fait [ici](https://assets.01-edu.org/netfix/netfix.zip). Vous remarquerez qu'il manque du code, à la fois dans les fichiers HTML et Python. Votre tâche consiste à le compléter afin que le site fonctionne comme expliqué ci-dessus.

Un fichier CSS est déjà fourni (dans le chemin `netfix/static/css/style.css`), mais n'hésitez pas à le modifier et à créer votre propre design pour votre site. Cela signifie également que vous pouvez changer le HTML déjà fourni.

> Lors de la première tentative de lancer le projet avec la commande `python3 manage.py runserver`, vous remarquerez que vous obtiendrez une erreur. Vous devez commencer par définir le modèle client.

### Bonus

En bonus pour ce projet, il y a quelques choses que vous pourriez faire :

- ajouter un système de notation, où les clients pourraient noter les services qu'ils ont demandés
- ajouter des pages à la liste des services
- n'hésitez pas à mettre en œuvre vos propres bonus