---
id: d388d41d-13e7-466b-9be5-532c3a6c1a8f
---

# [Ubuntu] 우분투 ROOT 접속
#Omnivore
 
[Read on Omnivore](https://omnivore.app/me/https-growupcoding-tistory-com-m-39-190432a8c94)
[Read Original](https://growupcoding.tistory.com/m/39)
 
basicinfo119 

## Ubuntu ROOT 접속 방법 

우분투는 설치 시 ssh 나 GUI에서 root 로그인 접속이 제한되어 있습니다. 

ssh로 리모트 ubuntu 서버에 접속하는 방법과 

GUI 로그인 리스트에서 root 계정 활성화 하는 방법에 대해 알아보겠습니다. 

### ROOT 접속 계정 비빌 번호 설정 

sudo passwd root 명령으로 root 비밀번호를 생성합니다. 

ubuntu@ubuntu:\~$ pwd   
/home/ubuntu   
ubuntu@ubuntu:\~$ whoami   
**ubuntu**   
ubuntu@ubuntu:\~$ **sudo passwd root**   
\[sudo\] password for ubuntu:   
New password:   
Retype new password:   
passwd: password updated successfully   
ubuntu@ubuntu:\~$ su - root   
Password:   
root@ubuntu:\~# whoami   
**root**   
root@ubuntu:\~#

### SSH Root 접속 허용 설정 (/etc/ssh/sshd\_config)

#PermitRootLogin prohibit-password => PermitRootLogin yes 설정 

```coffeescript
root@ubuntu:~# vi /etc/ssh/sshd_config
#       $OpenBSD: sshd_config,v 1.103 2018/04/09 20:41:22 tj Exp $

# This is the sshd server system-wide configuration file.  See
# sshd_config(5) for more information.

# This sshd was compiled with PATH=/usr/bin:/bin:/usr/sbin:/sbin

# The strategy used for options in the default sshd_config shipped with
# OpenSSH is to specify options with their default value where
# possible, but leave them commented.  Uncommented options override the
# default value.

Include /etc/ssh/sshd_config.d/*.conf

#Port 22
#AddressFamily any
#ListenAddress 0.0.0.0
#ListenAddress ::

#HostKey /etc/ssh/ssh_host_rsa_key
#HostKey /etc/ssh/ssh_host_ecdsa_key
#HostKey /etc/ssh/ssh_host_ed25519_key

# Ciphers and keying
#RekeyLimit default none

# Logging
#SyslogFacility AUTH
#LogLevel INFO

# Authentication:

#LoginGraceTime 2m
#PermitRootLogin prohibit-password
PermitRootLogin yes
#StrictModes yes
#MaxAuthTries 6
#MaxSessions 10
```

### SSH 서비스 재 시작 후 접속

```routeros
sudo service ssh restart
```

일반계정 ssh ROOT 접속 

일반계정에서 접속이 가능 한지 확인해보겠습니다. 

ubuntu 계정에서 root 로 정상적으로 접속이 되고 있습니다. 

ubuntu@ubuntu:\~$ ssh root@192.168.58.130   
The authenticity of host '192.168.58.130 (192.168.58.130)' can't be established.   
ECDSA key fingerprint is SHA256:HXSV8v929Lw15GM4sjnyr8Od6Y/84S1jrajWaC7PFtk. 

Are you sure you want to continue connecting (yes/no/\[fingerprint\])? yes 

Warning: Permanently added '192.168.58.130' (ECDSA) to the list of known hosts.   
root@192.168.58.130's password:   
tiberoPermission denied, please try again.   
root@192.168.58.130's password:   
Welcome to Ubuntu 20.04.4 LTS (GNU/Linux 5.13.0-37-generic x86\_64) 

 \* Documentation: [https://help.ubuntu.com](https://help.ubuntu.com/)   
 \* Management: [https://landscape.canonical.com](https://landscape.canonical.com/)   
 \* Support: <https://ubuntu.com/advantage>

17 updates can be applied immediately.   
To see these additional updates run: apt list --upgradable 

Your Hardware Enablement Stack (HWE) is supported until April 2025\.   
\*\*\* System restart required \*\*\*   
Last login: Sat Mar 26 07:13:22 2022 from 192.168.58.130   
root@ubuntu:\~# whoami   
root

### GUI 리스트에서 root 접속 활성화 하기 

아래 3개의 파일을 수정 하면 gui 리스트에 root 계정 접속도 가능합니다.

주석 처리 (#) 를 해주세요.

#### 1./etc/gdm3/custom.conf 수정

![](https://proxy-prod.omnivore-image-cache.app/0x0,srnfnmJANxwUvyWyG3Jx74uOUTyH25GiNrOd6kMOplMQ/https://blog.kakaocdn.net/dn/bOOwZ2/btryY9I0j9E/OJaxKzeKjNt3k4NhokrklK/img.png)

#### 2./etc/pam.d/gdm-password 

![](https://proxy-prod.omnivore-image-cache.app/0x0,sb97QHnBfD-wql7TIXCezPP7rYU9K4N3hHau7Oi-B4i4/https://blog.kakaocdn.net/dn/c9Rh5d/btry0cepbb9/NWbvbBGsUA7IqwmwKOadLK/img.png)

#### 3./etc/pam.d/gdm-autologin 

![](https://proxy-prod.omnivore-image-cache.app/0x0,sXW9tHI9_ruZ28y15KNAP0lzU-uwQKni_BqE3LjlUaS0/https://blog.kakaocdn.net/dn/dJfI7B/btryRRjhmqb/NLi0kmBKLRpNhFyKcyMIIk/img.png)

```makefile
vi /etc/gdm3/custom.conf 

# Enabling automatic login
AutomaticLoginEnable = true
AutomaticLogin = root

[security]
AllowRoot=true

vi /etc/pam.d/gdm-password 
#auth   required        pam_succeed_if.so user != root quiet_success

vi /etc/pam.d/gdm-autologin 
#auth   required        pam_succeed_if.so user != root quiet_success
```

서버 재기동 후 접속 

root@ubuntu:\~# shutdown -r now 

Notlited 클릭수 username root /비번 입력 후 접속을 진행합니다. 

이제 root 도 접속이 가능합니다. 

![](https://proxy-prod.omnivore-image-cache.app/0x0,sL_hQEG3ndEO11YVA0lPwrvAY-QySWtDs0fAv7fSrBzc/https://blog.kakaocdn.net/dn/btwkUb/btrxu9jcTgL/BIQgSnpUH3GommWKqYdp50/img.png)