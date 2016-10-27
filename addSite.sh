#!/bin/bash
clear
echo ""
echo "Ajout d'un site dans la configuration."
echo "Apache et dans le dossier web."
echo ""
read -p "Nom du site : " NOM_SITE
read -p "Adresse du site : " ADDR_SITE
echo ""

APACHE_CONF="/etc/apache2/sites-available/$NOM_SITE.conf"
WEB_DIR="/var/www/$NOM_SITE"


if [ -f $APACHE_CONF ];
then
   echo "File $NOM_SITE.conf already exists."
else
	echo "Ajout de la configuration Apache."
	cat >> $APACHE_CONF <<EOF
<VirtualHost *:80>
		ServerName  $ADDR_SITE
		DocumentRoot $WEB_DIR

		ErrorLog ${APACHE_LOG_DIR}/site-error.log
		LogLevel warn
		CustomLog ${APACHE_LOG_DIR}/site-access.log combined
</VirtualHost>
EOF
	if [ -d $WEB_DIR ]
	then
		echo "Le dossier exist deja."
	else
		echo "Creation du dossier web"
		mkdir $WEB_DIR
		echo "Ajout d'un index.html"
		echo -e "Hello World !" >> $WEB_DIR/index.html
	fi
	
	echo "Add site in Apache Conf."
	a2ensite $NOM_SITE.conf
	echo "Reload Apache Server."
	service apache2 reload

	echo ""
	echo "Detail de la configuration du site $NOM_SITE :"
	echo ""
	echo "Url : $ADDR_SITE"
	echo "Dossier : $WEB_DIR"
	echo "Fichier de conf : $APACHE_CONF"
	echo ""
fi
