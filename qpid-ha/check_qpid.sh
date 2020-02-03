#!/bin/bash
exit 0
if [ $(ps -C qpidd --no-header | wc -l) -eq 0 ]; then
    systemctl start qpidd
    systemctl start qpidd-primary
fi

sleep 2

if [ $(ps -C qpidd --no-header | wc -l) -eq 0 ]; then
    systemctl stop keepalived
fi

