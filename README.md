# LA CASA RESTAURANTE

## Tecnologías utilizadas ##

Django 3.2.12 + PostgreSQL 11 + Dokku config (Production Ready)
HTML, CSS3, JavaScript, JQuery, Contenedor Docker, Droplet de DigitalOcean, LetsEncrypt 


### Resumen ###
```
El presente proyecto consiste en la implementación de una tienda virtual 
para el restaurante ubicado en la ciudad de Villavicencio. El cliente podrá ver y comprar
los productos disponibles pagando por medio de la pasarela de pago Paypal o por transacción
Nequi. De la misma manera, podrá solicitar haciendo clic en el botón de WhatsApp el menú del día, 
el administrador del sitio generará cada día dicho menú mediante la selección de los productos 
que varían (sopas, principios, ensaladas) y la disponibilidad de los productos que son fijos.

```
### Requerimiento Funcional Prioritario ###
```
ADMINISTRAR LOS PRODUCTOS: Se ha priorizado el requerimiento funcional enunciado debido a 
la importancia que tiene. Es el núcleo del desarrollo pues es necesario tener todos los productos
debidamente actualizados, con imágenes consistentes y de buena calidad. Así mismo se debe 
implementar la estrategia de marketing para dar a conocer el sitio web.

```

### Metodología de Desarrollo ###
```
El marco de trabajo para el desarrollo del presente producto de software es SCRUM.
Se tiene una hoja de cálculo que se denomina backlog donde al inicio del desarrollo 
se especificaron cada una de las posibles actividades que se llevarían a cabo y con la
puesta en ejecución del proyecto se han agregado nuevas actividades. También se tienen reuniones
de manera periódica (cada lunes) y entregas de resultados al cliente (cada miércoles). 
Las anteriores dos, son características de SCRUM.

```

### Roles ###
```
-Edgar David Lozada Gonzalez - Product Owner
-Carlos Danilo Núñez Gil - Desarrollador
-Jessica Gómez Manrique - Scrum Master

```

### Kanban ###
```
Se hace uso de un Tablero Kanban en GitHub que es una herramienta con 
la que se puede tener una mirada simplificada de todas las actividades 
que están pendientes, se estén desarrollando y se hayan desarrollado. 
Dicho tablero está compuesto de tres columnas de actividades:

- To Do (actividad pendiente) 
- In progress (actividad en proceso)
- Done (actividad completadas)

Cada actividad se puede trabajar con un Issues (que traduce incidencia),
asignar a un integrante del equipo de desarrollo para así disponer de
un registro en donde se pueda visualizar lo que se tiene pendiente en
cuanto a actividades según sea el rol.

```
### ------------------------------- ASPECTOS TÉCNICOS ------------------------------- ###
### Directory Tree ###
```

├── main (Main application of the project, use it to add main templates, statics and root routes)
│   ├── fixtures
│   │   ├── dev.json (Useful dev fixtures, by default it creates an `admin` user with password `admin`)
│   │   └── initial.json (Initial fixture loaded on each startup of the project)
│   ├── migrations
│   ├── static (Add here the main statics of the app)
│   ├── templates (Add here the main templates of the app)
│   ├── admin.py
│   ├── apps.py
│   ├── models.py (Main models like City, Config)
│   ├── tests.py (We hope you will put some tests here :D)
│   ├── urls.py (Main urls, place the home page here)
│   └── views.py
├── media
├── lacasarestaurante
│   ├── settings
│   │   ├── partials
│   │   │   └── util.py (Useful functions to be used in settings)
│   │   ├── common.py (Common settings for different environments)
│   │   ├── development.py (Settings for the development environment)
│   │   └── production.py (Settings for production)
│   ├── urls.py
│   └── wsgi.py
├── scripts
│   ├── command-dev.sh (Commands executed after the development containers are ready)
│   └── wait-for-it.sh (Dev script to wait for the database to be ready before starting the django app)
├── static
├── Dockerfile (Instructions to create the project image with docker)
├── Makefile (Useful commands)
├── Procfile (Dokku or Heroku file with startup command)
├── README.md (This file)
├── app.json (Dokku deployment configuration)
├── docker-compose.yml (Config to easily deploy the project in development with docker)
├── manage.py (Utility to run most django commands)
└── requirements.txt (Python dependencies to be installed)
```

### How to install the template ###

Clone the repository, and update your origin url: 
```
git clone https://github.com/altixco/django-postgres-dokku lacasarestaurante
cd lacasarestaurante
```

Merge the addons required by your project (Optional):
```
git merge origin/rest
git merge origin/webpack
git merge origin/push-notifications
```

Rename your project files and directorys:
```
make name=lacasarestaurante init
```
> Info: Make is required, for mac run `brew install make`

> After this command you can already delete the init command inside the `Makefile` 

The command before will remove the `.git` folder so you will have to initialize it again:
```
git init
git remote add origin <repository-url>
```

### How to run the project ###

The project use docker, so just run:

```
docker-compose up
```

> If it's first time, the images will be created. Sometimes the project doesn't run at first time because the init of postgres, just run again `docker-compose up` and it will work.

*Your app will run in url `localhost:8000`*

To recreate the docker images after dependencies changes run:

```
docker-compose up --build
```

To remove the docker containers including database (Useful sometimes when dealing with migrations):

```
docker-compose down
```

### Accessing Administration

The django admin site of the project can be accessed at `localhost:8000/admin`

By default the development configuration creates a superuser with the following credentials:

```
Username: admin
Password: admin
```

## Production Deployment: ##

The project is dokku ready, this are the steps to deploy it in your dokku server:

#### Server Side: ####

> This docs does not cover dokku setup, you should already have configured the initial dokku config including ssh keys

Create app and configure postgres:
```
dokku apps:create lacasarestaurante
dokku postgres:create lacasarestaurante
dokku postgres:link lacasarestaurante lacasarestaurante
```

> If you don't have dokku postgres installed, run this before:
> `sudo dokku plugin:install https://github.com/dokku/dokku-postgres.git`

Create the required environment variables:
```
dokku config:set lacasarestaurante ENVIRONMENT=production DJANGO_SECRET_KEY=....
```

Current required environment variables are:

* ENVIRONMENT
* DJANGO_SECRET_KEY
* EMAIL_PASSWORD

Use the same command to configure secret credentials for the app

#### Local Side: ####

Configure the dokku remote:

```
git remote add dokku dokku@<my-dokku-server.com>:lacasarestaurante
```

Push your changes and just wait for the magic to happens :D:

```
git push dokku master
```

Optional: To add SSL to the app check:
https://github.com/dokku/dokku-letsencrypt

Optional: Additional nginx configuration (like client_max_body_size) should be placed server side in:
```
/home/dokku/<app>/nginx.conf.d/<app>.conf
```

> Further dokku configuration can be found here: http://dokku.viewdocs.io/dokku/

## Create volume for file storage (jpg, pdf, mp3, mp4, txt): ##

First we must connect to the server, with the following command.
``` 
ssh root@137.184.18.181 
```
Once inside the server we list the dokku applications.
```
dokku apps:list
```
After identifying the application to be connected to the volume, we proceed to create the directory (cms-media).
```
mkdir -p /var/dir/dokku/data/storage/cms-media
```
Then we grant access permissions to the folder and link the project directory to the folder.
```
chown -R dokku:dokku /var/dir/dokku/data/storage/cms-media
chown -R 32767:32767 /var/dir/dokku/data/storage/cms-media
dokku storage:mount lacasarestaurante /var/dir/dokku/data/storage/cms-media:/src/media
```
Then we restart the application.
```
dokku ps:restart lacasarestaurante
```
To verify that the volume was created successfully.
```
dokku storage:report
cd /var/dir/dokku/data/storage/cms-media
ls -la
```
> For more documentation: https://dokku.com/docs~v0.26.8/advanced-usage/persistent-storage/
