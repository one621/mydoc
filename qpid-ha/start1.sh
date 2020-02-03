#!/bin/bash

systemctl restart qpidd
sleep 1
systemctl start qpidd-primary

