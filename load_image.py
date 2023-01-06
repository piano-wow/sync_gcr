# coding:utf-8
# 支持 python2
import subprocess, os
def get_filename():
    with open("images.txt", "r") as f:
        lines = f.read().split('\n')
        return lines


def pull_image():
    name_list= get_filename()
    for name in name_list:
        if  name:
            new_name = "kenwood/" + name.split("/")[-1]
            cmd = "echo " + "docker pull " + new_name
            subprocess.call(cmd, shell=True)
            cmd = "echo " + "docker tag " + new_name + " " + name
            subprocess.call(cmd, shell=True)
            cmd = "echo " + "docker rmi " + new_name
            subprocess.call(cmd, shell= True)
if __name__ == "__main__":
    pull_image()
