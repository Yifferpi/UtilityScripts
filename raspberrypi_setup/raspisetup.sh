#! /bin/bash

if [ $(whoami) != "root" ]; then
    echo "Are you root?"
    exit 1
fi

if [ $# -eq 0 ]; then
    echo "two args required: first: image, second: disk"
    exit 1
fi


#Flash image given by first arg
dd bs=4M if="$PWD/$1" of="/dev/sde" conv=fsync
echo "Flash finished"

# mount boot partition
mkdir /mnt/raspi_boot
mount "/dev/sde1" /mnt/raspi_boot
sleep 0.5
#enable ssh
touch /mnt/raspi_boot/ssh
touch /mnt/raspi_boot/wpa_supplicant.conf
#wifi config
cat wificonfig.secret > /mnt/raspi_boot/wpa_supplicant.conf

umount /mnt/raspi_boot
sleep 0.5
rmdir /mnt/raspi_boot

