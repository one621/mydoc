# coding=utf-8


import argparse
import os
import subprocess

from log import INFO,DEBUG,ERROR

def exec_system_cmd(cmd):
    INFO("cmd:{}".format(cmd))
    ret = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    err = ret.stderr.read()
    result= ret.stdout.read()
    INFO("result:{},err:{}".format(result,err))

    return result

def deploy_qpidd_conf():
    qpid_dir = "/etc/qpid"
    if not os.path.exists(qpid_dir):
        os.mkdir(qpid_dir)
    exec_system_cmd("cp -f qpidd.conf /etc/qpid/qpidd.conf")

def deploy_qpid_service():
    exec_system_cmd("cp -f qpidd.service /usr/lib/systemd/system/qpidd.service")
    exec_system_cmd("cp -f qpidd-primary.service /usr/lib/systemd/system/qpidd-primary.service")

def deploy_keepalived_master():
    keepalived_dir = "/etc/keepalived/"
    if not os.path.exists(keepalived_dir):
        os.mkdir(keepalived_dir)
    exec_system_cmd("cp -f keepalived-MASTER.conf /etc/keepalived/keepalived.conf")

def deploy_keepalived_backup():
    keepalived_dir = "/etc/keepalived/"
    if not os.path.exists(keepalived_dir):
        os.mkdir(keepalived_dir)
    exec_system_cmd("cp -f keepalived-BACKUP.conf /etc/keepalived/keepalived.conf")

def create_qpid_queue(queue_name):
    cmd= "qpid-config add queue {} --durable ".format(queue_name)
    INFO("cmd:{}".format(cmd))
    exec_system_cmd(cmd)

def start_service(ismaster=False):
    cmd= "systemctl restart qpidd.service"
    exec_system_cmd(cmd)
    cmd= "systemctl restart keepalived.service"
    exec_system_cmd(cmd)
    if ismaster:
        cmd= "systemctl restart qpidd-primary.service"
        exec_system_cmd(cmd)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("action",help="action")
    parser.add_argument("name",help="action")
    args = parser.parse_args()
    action = args.action
    name = args.name
    INFO("action:{},name:{}".format(action,name))
    if action == "deploy":
        INFO("deploy")
        deploy_qpidd_conf()
        deploy_qpid_service()
        if name == "master":
            deploy_keepalived_master()
            start_service(True)
        else:
            deploy_keepalived_backup()
            start_service(False)

    elif action == "setvip":
        INFO("set vip")
    else:
        INFO("1111")
    #exec_system_cmd("dir")