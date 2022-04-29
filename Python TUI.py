import os
    
os.system("tput setaf 4; tput setab 7; clear")

while True:
        os.system(" clear; tput setab 7 ; tput setaf 1 ")
        print("\n\t\t\t\t\t\t\t\tWELCOME TO TUI")
        os.system("tput setaf 2")
        print("\t\t\t\t\t\t\t\t~~~~~~~~~~~~~~~")
        os.system("tput setaf 4")
        print("""
        \t===========================================================================================================
        \t||    *:::::::::::: SOFTWARE / PACKAGES ::::::::::::*       *::::::::::::::: DOCKER :::::::::::::::*     ||    
        \t||    1.1 See all installed packages                        4.1 Install docker CE                        ||
        \t||    1.2 Check if particular package is installed          4.2 Start docker services                    ||
        \t||    1.3 Install a package                                 4.3 Stop docker services                     ||
        \t||    1.4 Uninstall a package                               4.4 Download a container image               ||
        \t||                                                          4.5 Images available                         ||
        \t||    *:::::::::::::::: PARTITIONS :::::::::::::::::*       4.6 Run a new docker container               ||
        \t||    2.1 Disks attached to the system                      4.7 See all containers                       ||
        \t||    2.2 Get inside a disk to create partitons             4.8 Start and attach a container             ||
        \t||    2.3 See all blocks                                    4.9 Remove an image                          || 
        \t||    2.4 Create driver for devices(partions created)       4.10 Remove a container                      ||
        \t||                                                          4.11 Clone a container and create image      ||
        \t||    *:::::;;;;;;;;;;: WEB SERVER :;;;;;;;;::::::::*                                                    ||                      
        \t||    3.1 Configure Web Server                                                                           ||         
        \t||    3.2 Start Web Server                                  *::::::::::::::::::::::::::::::::::::::*     ||
        \t||    3.3 stop web server                                                                                ||
        \t||    3.4 edit/create webpage                                         Enter 0 to EXIT TUI                ||
        \t||    3.5 Your Webpages                                                                                  ||
        \t||    3.6 Disable firewall(temp)                            *::::::::::::::::::::::::::::::::::::::*     ||
        \t||                                                                                                       || 
        \t===========================================================================================================""")
        
        os.system("tput setaf 1")
        print("\n>> Enter your choice:", end=' ')
        os.system("tput setaf 4")
        ch=float(input())
        if ch == 1.1:
            os.system("rpm -q -a")
        elif ch == 1.2:
            a = input("Enter package name: ")
            os.system("rpm -q {}".format(a))
        elif ch == 1.3:
            a = input("Enter package name to install: ")
            os.system("yum install {}".format(a))
        elif ch == 1.4:
            a = input("Enter package name you want to uninstall: ")
            os.system("yum remove {}".format(a))
        elif ch == 2.1:
            os.system("fdisk -l")
        elif ch == 2.2:
            a = input("Enter disk name(like /dev/sdb): ")
            os.system("fdisk {}".format(a))
        elif ch == 2.3:
            os.system("lsblk")
        elif ch == 2.4:
            os.system("udevadm settle")
        elif ch == 3.1:
            os.system("yum install httpd")
        elif ch == 3.2:
            os.system("systemctl start httpd")
        elif ch == 3.3:
            os.system("systemctl stop httpd")
        elif ch == 3.4:
            a = input("Enter name(like page.html): ")
            os.system("cd /var/www/html; gedit {}".format(a))
        elif ch == 3.5:
            os.system("ls /var/www/html")
        elif ch == 3.6:
            os.system("systemctl stop firewalld")

        elif ch == 4.1:
            print("""
                   First you have to ensure that you have the docker repository to install docker-ce,
                   to do so follow these steps:-
                   1) Go to yum repository directory-  cd/etc/yum.repos.d/
                   2) create and edit a repo file-  gedit docker.repo
                   3) Type the following in the editor,
                        [docker]
                        baseurl=https://download.docker.com/linux/centos/7/x86_64/stable/
                        gpgcheck=0 """)
            a = input("Have you done the above steps(y/n): ")
            if a=='y' or a=='Y':
                os.system("yum install docker-ce --nobest")
        elif ch == 4.2:
            os.system("systemctl start docker")
        elif ch == 4.3:
            os.system("systemctl stop docker")
        elif ch == 4.4:
            a = input("Enter image name: ")
            os.system("docker pull {}".format(a))
        elif ch == 4.5:
            os.system("docker images")
        elif ch == 4.6:
            a = input("Enter container image: ")
            b = input("What name do you want to give to the container: ")
            os.system("docker run -it --name {0} {1}".format(b,a))
        elif ch == 4.7:
            os.system("docker ps -a")
        elif ch == 4.8:
            a = input("Enter name of the container: ")
            os.system("docker start {}".format(a))
            os.system("docker attach {}".format(a))
        elif ch == 4.9:
            a = input("Enter image to be removed: ")
            os.system("docker rmi {}".format(a))
        elif ch == 4.10:
            a = input("Enter container to be removed: ")
            os.system("docker rm {}".format(a))
        elif ch == 4.11:
            a = input("Which container do you want to clone: ")
            b = input("Enter the image name you want to give: ")
            os.system("docker commit {0} {1}".format(a,b))

        elif ch == 0.0:
            os.system("tput setaf 2")
            input("\n THANK YOU for using !!! press ENTER to exit...")
            os.system("tput setaf 4")
            exit()
        else:
            print("\n Sorry!!! choice not available")
        os.system("tput setaf 1")
        input("\n Press ENTER to continue...")

