BIG-IP HA Pair Configurations
#########################################################
This guide gives detailed information about configuring BIG-IP to HA pair.

Pre-requesites
-------------------------------
1. Couple of Standalone BIG-IPs should be available.

2. Couple of IP Address to connect both the BIG-IP.

Steps to bring up BIG-IP in HA mode
-------------------------------
Before proceeding, we can see both the BIG-IPs are in Standalone mode,

.. image:: ./assets/BIG-IP_HA/standalone_a.jpg

.. image:: ./assets/BIG-IP_HA/standalone_b.jpg

Let's have a look at Internal, External and HA IP addresses.

.. image:: ./assets/BIG-IP_HA/standalone_a_self_ips.jpg

.. image:: ./assets/BIG-IP_HA/standalone_b_self_ips.jpg

HA configuration follows series of steps which includes ConfigSync, Failover Network and Mirrorring. These need to be performed for both the BIG-IPs that are planned to form HA pair.

.. image:: ./assets/BIG-IP_HA/standalone_a_config_sync.jpg

.. image:: ./assets/BIG-IP_HA/standalone_a_network_failover.jpg

.. image:: ./assets/BIG-IP_HA/standalone_a_mirroring.jpg


