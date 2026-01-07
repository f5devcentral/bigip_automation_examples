Application Migration from VMware to Nutanix
#########################################################
In this article, the detailed description of migrating BIG-IP VE from VMware to Nutanix Platform,

Below are the details steps that are followed to perform migration from VMware to Nutanix,

Installation of BIG-IP on VMware is mentioned in doc here.

Simillary, Installation of BIG-IP on Nutanix is mentioned in the doc here.

Steps to migrate BIG-IP from VMware to Nutanix
--------------
The migraiton is breakdown into 5 detailed steps for better understanding,

1) Deploy BIG-IP in HA pair in VMware
2) Migrate Standby BIG_IP VE to Nutanix
3) Failover the Active BIG-IP
4) Migration of application workloads
5) Migratate VMware BIG-IP to Nutanix

**Step 1**: Deploying BIG-IP in HA pair in VMware

Step 1.1: Deploying BIG-IP in HA pair

BIG-IP is deployed as HA pair in VMware.

.. image:: ../Assets/device_details_active.jpg