#!/bin/bash
. ./lab_env.sh
#config=`cat project/config.yml | grep -m1  "\- id:"|cut -d " " -f  3`

while [ "$APPLY" !=  "Y" ]
do
        clear
        echo "Variables : "
        echo ""
        echo "0) export DT_TENANT_URL="$DT_TENANT_URL
        echo "1) export DT_API_TOKEN="$DT_API_TOKEN
        echo "2) export HostGroup="$HostGroup
        echo "3) export DonainName="$DonainName
        echo "4) export Email="$Email
        echo "5) project/config.yaml, need a unique id: "$config 
        echo "A) Apply the configuration (Ctrl/c to quit)"
        echo ""
        sleep 0.2
        read  -p "Input Selection (0, 1, 2, 3, 4, 5 or A ): " reponse

        case "$reponse" in
                "0") read  -p "0) export DT_TENANT_URL=https://" value
                     sed -i 's/DT_TENANT_URL=.*$/DT_TENANT_URL=\"https\:\/\/'$value'\"/g' ./lab_env.sh;. ./lab_env.sh
                ;;
                "1") read  -p "1) export DT_API_TOKEN=" value
                     sed -i s/DT_API_TOKEN=.*$/DT_API_TOKEN=\"$value\"/g ./lab_env.sh;. ./lab_env.sh
                ;;
                "2") read  -p "2) export HostGroup=" value
                     sed -i s/HostGroup=.*$/HostGroup=\"$value\"/g ./lab_env.sh;. ./lab_env.sh
                ;;
                "3") read  -p "3) export DonainName=" value
                     sed -i s/DonainName=.*$/DonainName=\"$value\"/g ./lab_env.sh;. ./lab_env.sh
                ;;
                "4") read  -p "4) export Email=" value
                     sed -i s/Email=.*$/Email=\"$value\"/g ./lab_env.sh;. ./lab_env.sh
                ;;
                "5") if [[ $config == "config-id" ]];then
                      config=`uuidgen`
                      sed -i "s/config-id/$config/g" project/config.yml
                      sed -i "s/config-id/$config/g" ./lab_env.sh;. ./lab_env.sh
                     fi
                     
                ;;
                "A") APPLY="Y"
                     . ./lab_env.sh
                ;;
        esac
done
echo "Let's start deployment: "
echo " 1. run local variables:   . lab_env.sh"
echo " 2. run monaco v2:         ./monaco deploy manifest.yaml"
