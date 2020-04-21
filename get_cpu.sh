for eachfile in /sys/bus/vmbus/devices/*
do
        id=$(cat $eachfile/id)
        #echo $eachfile/channels/$id/cpu
        cat $eachfile/channels/$id/cpu
done
