# Backup script

# Mysql conf
USER="root"
PASS="root"

# File name conf
TIME=`date +%y-%m-%d`

# SCP conf
SRV_USER="root"
SRV_PASS="root"
SRV_HOST="10.0.10.0"
SRV_PORT=22
SRV_PATH="/opt/backups/"


function aptNotYetInstalled() {
	set +e;
	return $(dpkg-query -W --showformat='${Status}\n' $1 2>/dev/null | grep -c "install ok installed");
	set -e;
}

TAR_DIR="/opt/backups/backup-${TIME}"
mkdir -p $TAR_DIR
# Tar /var/www
echo "-- Taring /var/www"
cd /var/www
tar -zcf "${TAR_DIR}/web.tar.gz" .
cd $TAR_DIR

# Backup sql
echo "-- Backing up sql"
databases=`mysql --user=$USER --password=$PASS -e "SHOW DATABASES;" | tr -d "| " | grep -v Database`

# Remove internal mysql stuff
databases=$(echo $databases | sed 's/information_schema\ //g')
databases=$(echo $databases | sed 's/performance_schema\ //g')

for db in $databases; do
	echo "- ${db}"
	mysqldump --force --opt --user=$USER --password=$PASS --databases $db > $db.sql
done

# Tar all of that
tar -zcf "${TAR_DIR}.tar.gz" .

# Check if sshpass is install
if aptNotYetInstalled "sshpass"; then
	apt-get install -y sshpass
fi

# Share tar.gz to another server
sshpass -p $SRV_PASS scp -P $SRV_PORT "${TAR_DIR}.tar.gz" $SRV_USER@$SRV_HOST:$SRV_PATH

# remove useless things
rm -rf ${TAR_DIR}
echo -e "\nDone !"
