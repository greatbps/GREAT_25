---
id: 66048161-81c8-4706-85f1-2fdcf0906b64
---

# [Docker] MariaDB 백업/복구 (mysqldump)
#Omnivore
 
[Read on Omnivore](https://omnivore.app/me/https-nasn-tistory-com-m-110-1904897cbd4)
[Read Original](https://nasn.tistory.com/m/110)
 
Codit Develop 

## Container 외부에서 MariaDB Data Backup

Container에 접속하지 않고 MariaDB 데이터를 SQL로 저장.

## 명령어

### 기본 실행문

```inform7
# docker exec [Container Name] /usr/bin/mysqldump -u [UID] --password=[Password] [DB Name] > [Backup File Full Path]
docker exec con_mariadb /usr/bin/mysqldump -u root -password=system workspace_db > /usr/bin/backup/backup_20210112.sql
```

### 옵션

```inform7
#  전체 DB Backup
docker exec [Container Name] /usr/bin/mysqldump -u [UID] 
    --password=[Password] 
    --all-databases > [Backup File Full Path]

# 특정 DB Backup
docker exec [Container Name] /usr/bin/mysqldump -u [UID] 
    --password=[Password] [DB Name] > [Backup File Full Path]

# DDL Backup
docker exec [Container Name] /usr/bin/mysqldump -u [UID] 
    --password=[Password] 
    --all-databases 
    --no-data > [Backup File Full Path]

# 특정 DB 프로시저 포함 Backup
docker exec [Container Name] /usr/bin/mysqldump -u [UID] 
    --password=[Password] 
    --routines [DB Name] > [Backup File Full Path]

# 특정 DB 프로시저만 Backup
docker exec [Container Name] /usr/bin/mysqldump -u [UID] 
    --password=[Password] 
    --routines 
    --triggers [DB Name] > [Backup File Full Path]

# 특정 Table Backup  
docker exec [Container Name] /usr/bin/mysqldump -u [UID] 
    --password=[Password] [DB Name] [Table Name1] > [Backup File Full Path]


# 특정 Table Data만 Backup
docker exec [Container Name] /usr/bin/mysqldump -u [UID] 
    --password=[Password] 
    --no-create [DB Name] [Table Name1] > [Backup File Full Path]

```