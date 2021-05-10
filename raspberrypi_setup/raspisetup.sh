#! /bin/bash

# Fetch list of possible block devices
blkdev=`lsblk | grep disk | tr -s ' ' | cut -d ' ' -f 1 | tr '\n' ','`
# Check args
if [ $# -lt 2 ]; then
    cat << EOF
Usage: ${0##*/} <image> <device>
  Flash a .img to an SD card.

  image     The .img OS image you want to flash.
  device    The device you want to flash it to.
            Available devices are: $blkdev

Error: propositional argument missing!
EOF
exit 1
fi

#Flash image given by first arg
s=`lsblk -b | grep "$2" | tr -s ' ' | cut -d ' ' -f4` #try to find device size
if [ "$s" == "" ]; then
    echo "$2 not found. Possible devices are: $blkdev"
    echo "Exiting.."
    exit 1
elif [ "$s" -gt "35000000000" ]; then #check device less than 35G
    #if bigger, ask for additinal confirmation
    while true; do
    read -p "$2 is bigger than a typical drive. Are you sure you want \
to overwrite it? [y/n]" yn
    case $yn in
        [Yy]* ) echo "Start flashing..."; break;;
        [Nn]* ) echo "Aborting..."; exit;;
        * ) echo "Please answer yes or no.";;
    esac
    done
fi
# Check for root privileges
if [ $(whoami) != "root" ]; then
    echo "Are you root?"
    exit 1
fi
# check that $1 is indeed a file
dd bs=4M if="$PWD/$1" of="/dev/$2" conv=fsync status=progress
echo "Flash finished"

# mount boot partition
mkdir /mnt/raspi_boot
mount "/dev/$21" /mnt/raspi_boot
sleep 0.5
touch /mnt/raspi_boot/ssh
touch /mnt/raspi_boot/wpa_supplicant.conf
#wifi config
#check existence of .secret file to copy
cat wificonfig.secret > /mnt/raspi_boot/wpa_supplicant.conf

umount /mnt/raspi_boot
sleep 0.5
rmdir /mnt/raspi_boot

