#! /bin/sh

HMC="$1"

serverlist=`ssh -q -o "BatchMode yes" $HMC lssyscfg -r sys -F "name" | sort`

for server in $serverlist; do
    echo " \"$HMC\" -- \"$server\" "
    lparlist=`ssh -q -o "BatchMode yes" $HMC lssyscfg -m $server -r lpar -F "name" | sort`
    for lpar in $lparlist; do
             echo "    \"$server\" -- \"$lpar\" "
    done
done
 
echo "}"