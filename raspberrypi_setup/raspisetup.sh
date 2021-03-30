#! /bin/bash

#Flash image given by first arg
dd bs=4M if=$PWD/$1 of=/dev/sda conv=fsync
echo "Flash finished"

# mount boot partition
mkdir /mnt/raspi_boot
mount /dev/sda1 /mnt/raspi_boot

#enable ssh
touch /mnt/raspi_boot/ssh
touch /mnt/raspi_boot/wpa-supplicant.conf
#wifi config
cat wificonfig.secret > /mnt/raspi_boot/wpa-supplicant.conf

umount /mnt/raspi_boot
rmdir /mnt/raspi_boot

