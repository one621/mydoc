# centos7下安装glusterfs  
### 安装提供glusterfs的yum源
yum install centos-release-gluster

    # mkfs.xfs -i size=512 /dev/sdb1
    # mkdir -p /bricks/brick1
    # vi /etc/fstab



# docker 下安装glusterfs

docker安装centos7镜像  
docker pull centos:7  

使用特权等级启动centos7的docker  
docker run --privileged -id --name glusterfs docker.io/centos:7 /usr/sbin/init  
docker exec -it glusterfs  /bin/bash  


### 安装提供glusterfs的yum源
yum install centos-release-gluster  

docker run -id --name glusterfs1 -v /bricks/docker/gv0:/bricks/disk myglusterfs /usr/sbin/init  
docker exec -it glusterfs1 bash  

docker run --privileged=true -i -t -v /bricks/docker/gv2:/bricks/disk myglusterfs /bin/bash  
/usr/sbin/glusterd  
172.17.0.4      server3  
172.17.0.5      server4  
server4执行  
    gluster peer probe server3  
server3执行 
    gluster peer probe server4  
双端执行  
    mkdir /bricks/disk/gv0  
server4或者server4执行    
    gluster volume create gv0 replica 2 server3:/bricks/disk/gv0 server4:/bricks/disk/gv0
    gluster volume start gv0  
vi /etc/hosts  
172.17.0.2      server1  
172.17.0.3      server2  

