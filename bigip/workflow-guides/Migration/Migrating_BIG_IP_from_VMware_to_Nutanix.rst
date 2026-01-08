BIG-IP VE and Application workload migraiton from VMware to Nutanix
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

.. image:: ./Assets/device_details_active.jpg

.. image:: ./Assets/device_details_stby.jpg

You can able to see both the BIG-IPs are in HA pair.

Node Pool and Virtual Server is configured as shown below, 

.. image:: ./Assets/juice_shop_vs.jpg

Its associated web application is accessible using Virtual Server IP.

.. image:: ./Assets/stage_1_verification.jpg

Now, before proceeding to Stage 2, couple of BIG-IPs are deployed and no configs were done to it.

.. image:: ./Assets/big_ip_vms_nutanix.jpg

From the Nutanix console, you can able to see two BIG-IPs are deployed.

**Step 2**: Migrating Standby BIG-IP VE to Nutanix
1. Place VMware BIGIP-2 (Standby) into **Forced Offline** mode and save a backup of its configuration.
2. Copy the license file located at ``/config/bigip.license``.
3. Store the configuration and license files in a secure location for later use.
4. Revoke the license on VMware BIGIP-2.

   .. note::
      If the license was assigned via BIG-IQ, follow the applicable BIG-IQ procedures.

5. Disconnect all network interfaces on VMware BIGIP-2.

   .. note::
      Disconnecting interfaces allows faster rollback compared to powering off the VM.

6. Power on Nutanix BIGIP-2 and assign it the same management IP address previously
   used by VMware BIGIP-2.
7. Apply the saved license to Nutanix BIGIP-2.

   .. note::
      Refer to K91841023 if the VE is operating in FIPS mode.

8. Set Nutanix BIGIP-2 to **Forced Offline**.
9. Upload the saved UCS file to Nutanix BIGIP-2 and load it using the
   **no-license** option.

   .. note::
      Refer to K9420 if the UCS contains encrypted credentials.

10. Monitor the logs and wait until the message
    ``Configuration load completed, device ready for online`` appears.
11. Bring Nutanix BIGIP-2 **Online**.

    .. note::
       Ensure the NIC count and interface-to-VLAN mappings exactly match those of
       VMware BIGIP-2.

12. Verify that Nutanix BIGIP-2 is **In Sync**. If configuration changes are pending,
    initiate a config sync using::

        run cm config-sync from-group <device-group-name>

13. The Standby BIG-IP VE has now been successfully migrated to Nutanix.

.. note::
   Because the BIG-IP VEs are running on different hypervisors during this phase,
   connection or persistence mirroring will not function. Messages such as
   ``DAG hash mismatch; discarding mirrored state`` may appear and are expected.

**Current BIG-IP Status:**

- VMware BIGIP-1: Active
- Nutanix BIGIP-2: Standby



