# qpid-ha

安装qpid-cpp-server-ha
#安装rpm -i https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
修改/usr/lib/systemd/system/qpidd-primary.service
修改下面2行
#EnvironmentFile=/etc/sysconfig/qpidd
ExecStart=/usr/bin/qpid-ha --cluster-manager promote

修改/etc/qpid/qpidd.conf文件
auth=no
ha-cluster=yes
ha-brokers-url=node1,node2
ha-queue-replication=yes
ha-replicate=all
ha-backup-timeout=30

双端执行systemctl start qpidd
主端执行systemctl start qpidd-primary

安装最新的keepalived
https://www.keepalived.org/software/keepalived-2.0.20.tar.gz