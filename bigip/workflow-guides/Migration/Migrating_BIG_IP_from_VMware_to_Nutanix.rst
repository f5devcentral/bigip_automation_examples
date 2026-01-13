Application Migration across Heterogeneous Environments using F5 BIG-IP VE
#########################################################

Scope
-----

As organizations deploy applications across multiple infrastructure platforms to
meet scalability, cost, and flexibility requirements, the need to migrate
applications and traffic between environments becomes unavoidable. Such migrations
introduce challenges related to availability, security, and network consistency.

This document focuses on the use of F5 BIG-IP to support application traffic
migration across heterogeneous platforms, ensuring consistent traffic management
and policy enforcement with minimal impact to application services.

Introduction
------------

This article highlights how F5 BIG-IP enables seamless application traffic
migration across mixed infrastructure environments commonly found in enterprise
deployments. As organizations move applications between platforms such as VMware,
Nutanix and public clouds, maintaining consistent traffic management,
availability and security becomes critical.

Common migration scenarios include moving applications from VMware to alternative
platforms based on business needs, extending on-premises applications to Nutanix
and public cloud environments, and deploying applications across multiple
platforms for resiliency and continuity. BIG-IP plays a central role in these
transitions by ensuring consistent application delivery and policy enforcement
throughout the migration process.


Scenario 1 :
-----------

Migration from VMware to Nutanix
-------------------------------
The migration is breakdown into 5 detailed steps for better understanding,

1) Deploy BIG-IP in HA pair in VMware
2) Migrate Standby BIG_IP VE to Nutanix
3) Failover the Active BIG-IP
4) Migration of application workloads
5) Migratate VMware BIG-IP to Nutanix

**Step 1**: Deploying BIG-IP in HA pair in VMware

Step 1.1: Refer to 
`BIG-IP HA Deployment on VMware
<./././workflow-guides/application-delivery-security/workload/BIG-IP-Deployment-on-VMware.rst>`_
for Deployment Steps

BIG-IP is deployed as HA pair in VMware.

.. image:: ./Assets/device_details_active.jpg

.. image:: ./Assets/device_details_stby.jpg

You can able to see both the BIG-IPs are in HA pair.

Node Pool and Virtual Server is configured as shown below, 

.. image:: ./Assets/juice_shop_vs.jpg

Its associated web application is accessible using Virtual Server IP.

.. image:: ./Assets/stage_1_verification.jpg

Now, before proceeding to Stage 2, couple of BIG-IPs are deployed in Nutanix and no configs were done to it. 

Refer to
`BIG-IP Deployment on Nutanix
<././application-delivery-security/workload/BIG-IP-Deployment-Nutanix.rst>`_
for Deployment Steps

.. image:: ./Assets/big_ip_vms_nutanix.jpg

From the Nutanix console, you can able to see two BIG-IPs are deployed.

Stage 2: Migrating Standby BIG-IP VE to Nutanix
--------------------------------------------------

1. Place VMware BIGIP-2 (Standby) into **Forced Offline** mode and save a backup of its configuration.

.. image:: ./Assets/ucs_license_file_copies.jpg

2. Copy the license file located at ``/config/bigip.license``.

3. Store the configuration and license files in a secure location for later use.

4. Revoke the license on VMware BIGIP-2.

.. image:: ./Assets/revoke_sys_license.jpg

5. Disconnect all network interfaces on VMware BIGIP-2.

.. image:: ./Assets/connection_disconnected.jpg

6. Power on Nutanix BIGIP-2 and assign it the same management IP address previously
   used by VMware BIGIP-2.

.. image:: ./Assets/nutanix_big_ip_login_2.jpg

7. Apply the saved license to Nutanix BIGIP-2.

.. image:: ./Assets/license_install.jpg

8. Set Nutanix BIGIP-2 to **Forced Offline**.

.. image:: ./Assets/license_install.jpg

9. Upload the saved UCS file to Nutanix BIGIP-2 and load it using the

.. image:: ./Assets/uploading_license.jpg

10. Monitor the logs and wait until the message
    ``Configuration load completed, device ready for online`` appears.

11. Bring Nutanix BIGIP-2 **Online**.

    Note::

       Ensure the NIC count and interface-to-VLAN mappings exactly match those of
       VMware BIGIP-2.

12. Verify that Nutanix BIGIP-2 is **In Sync**. If configuration changes are pending,
    initiate a config sync using::

        run cm config-sync from-group <device-group-name>

13. The Standby BIG-IP VE has now been successfully migrated to Nutanix.

.. image:: ./Assets/nutanix_big_ip_in_standby.jpg

.. note::
   Because the BIG-IP VEs are running on different hypervisors during this phase,
   connection or persistence mirroring will not function. Messages such as
   ``DAG hash mismatch; discarding mirrored state`` may appear and are expected.

**Current BIG-IP Status:**

- VMware BIGIP-1: Active
- Nutanix BIGIP-2: Standby

Stage 3 – Fail Over the Active BIG-IP VE to Nutanix
--------------------------------------------------

1. Initiate a failover, transitioning VMware BIGIP-1 from Active to Standby.

2. Nutanix BIGIP-2 becomes the Active BIG-IP VE.

.. image:: ./Assets/switchover_from_vmware_to_nutanix.jpg

**Current BIG-IP Status:**

- VMware BIGIP-1: Standby
- Nutanix BIGIP-2: Active

Stage 4 – Migrate Application Workloads from VMware to Nutanix
--------------------------------------------------------------

1. The recommended and preferred method for migrating application workloads from
   VMware to Nutanix is to use **Nutanix Move**, as it provides an automated and
   consistent migration workflow.

2. For the purpose of this testing and validation exercise, application workloads
   were **manually deployed** on Nutanix instead of using Nutanix Move.

3. Manual deployment included provisioning new ubuntu virtual machines and restoring 
   application data to match the existing VMware environment.

.. image:: ./Assets/vms_in_nutanix.jpg

4. Application configurations were updated and validated to ensure proper
   integration with the Active BIG-IP VE running on Nutanix, including pool member
   configuration, health monitors, and traffic flow validation.

.. image:: ./Assets/virtual_server_configs.jpg

.. image:: ./Assets/pool_status_bigip_in_nutanix.jpg

.. image:: ./Assets/accessing_application.jpg

.. note::
   To minimize service interruption, it is recommended to migrate applications in
   smaller batches rather than all at once. Nutanix Move requires briefly shutting
   down the source VM to complete the final data synchronization before starting it
   on Nutanix.

**Current BIG-IP Status:**

- VMware BIGIP-1: Standby
- Nutanix BIGIP-2: Active

Stage 5 – Migrate the Remaining Standby BIG-IP VE to Nutanix
------------------------------------------------------------

1. Place VMware BIGIP-1 (Standby) into **Forced Offline** mode and back up its
   configuration.

.. image:: ./Assets/vmware_big_ip_offline.jpg

2. Save the license file from ``/config/bigip.license``.

3. Store both files securely for later restoration.

4. Revoke the license from VMware BIGIP-1.

.. image:: ./Assets/big_ip_1_sys_license.jpg

5. Disconnect all interfaces on VMware BIGIP-1.

.. image:: ./Assets/disconnecting_interfaces_vmware_big_ip1.jpg

6. Power on Nutanix BIGIP-1 and configure it with the same management IP as
   VMware BIGIP-1.

.. image:: ./Assets/ip_assign_1.png

.. image:: ./Assets/ip_assign_8.png

7. Apply the saved license to Nutanix BIGIP-1.

.. image:: ./Assets/install_license_bigip_1.jpg

8. Set Nutanix BIGIP-1 to **Forced Offline**.

9. Upload and restore the saved UCS file using the **no-license** option.

.. image:: ./Assets/loading_ucs_file_to_nutanix_big_ip1.jpg

10. Monitor logs until the message
    ``Configuration load completed, device ready for online`` is displayed.

11. Bring Nutanix BIGIP-1 **Online**, ensuring NIC count and VLAN mappings match
    the original VMware configuration.

12. Confirm that the device is **In Sync** and perform a configuration sync if needed.

.. image:: ./Assets/final_big_ips_state_verification.jpg

13. VMware BIGIP-1 has now been fully migrated to Nutanix.

**Migration Status:**

- Nutanix BIGIP-1: Standby
- Nutanix BIGIP-2: Active

Summary
-------

This document demonstrates the detailed process for migrating F5 BIG-IP
Virtual Edition instances and application workloads from VMware to Nutanix AHV.
By following this phased approach within a planned maintenance window, organizations
can achieve a smooth transition with minimal impact to application services, ensuring
continuity both during and after the migration.



