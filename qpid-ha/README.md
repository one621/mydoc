# qpid-ha

安装qpid-cpp-server-ha
#安装rpm -i https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm  
安装qpid和qpidd-primary  
yum install -y qpidd qpidd-primary  
修改/usr/lib/systemd/system/qpidd-primary.service  
修改下面2行  
#EnvironmentFile=/etc/sysconfig/qpidd  
ExecStart=/usr/bin/qpid-ha --cluster-manager promote  
修改后的[qpidd.service](https://github.com/one621/mydoc/blob/master/qpid-ha/qpidd.service)和[qpidd-primary.service](https://github.com/one621/mydoc/blob/master/qpid-ha/qpidd-primary.service)  

修改/etc/qpid/qpidd.conf文件  
auth=no  
ha-cluster=yes  
ha-brokers-url=node1,node2  
ha-queue-replication=yes  
ha-replicate=all  
ha-backup-timeout=30  

双端执行systemctl start qpidd  
主端执行systemctl start qpidd-primary  

## 安装最新的keepalived
https://www.keepalived.org/software/keepalived-2.0.20.tar.gz

## 双端启动keepalived  
systemctl start keepalived.service
[主端keepalived.conf](https://github.com/one621/mydoc/blob/master/qpid-ha/keepalived-MASTER.conf)和[从端keepalived.conf](https://github.com/one621/mydoc/blob/master/qpid-ha/keepalived-BACKUP.conf)  
##  创建持久化队列  
qpid-config -b 192.168.1.244 add queue one --durable  
spout -b 192.168.1.244 one "asdfasdfsaf" --durable  
drain -b 192.168.1.244 one  

[keepalived介绍](https://segmentfault.com/a/1190000020144590?utm_source=tag-newest)