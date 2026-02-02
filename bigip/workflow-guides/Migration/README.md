# Application Migration across Heterogeneous Environments using F5 BIG-IP VE

## Scope

As organizations deploy applications across multiple infrastructure platforms to meet scalability, cost, and flexibility requirements, the need to migrate applications and traffic between environments becomes unavoidable. Such migrations introduce challenges related to availability, security, and network consistency.

This document focuses on the use of F5 BIG-IP to support application traffic migration across heterogeneous platforms, ensuring consistent traffic management and policy enforcement with minimal impact to application services.

## Introduction

This article highlights how F5 BIG-IP enables seamless application traffic migration across mixed infrastructure environments commonly found in enterprise deployments. As organizations move applications between platforms such as VMware, Nutanix, and public clouds, maintaining consistent traffic management, availability, and security becomes critical.

Common migration scenarios include moving applications from VMware to alternative platforms based on business needs, extending on-premises applications to Nutanix and public cloud environments, and deploying applications across multiple platforms for resiliency and continuity. BIG-IP plays a central role in these transitions by ensuring consistent application delivery and policy enforcement throughout the migration process.

## Architecture Overview

![ ](./Assets/arch_overview.png)
The architecture demonstrates how F5 BIG-IP VE provides consistent application delivery across heterogeneous infrastructure platforms.

In the source environment, application workloads run on VMware and are front-ended by BIG-IP VE instances responsible for traffic management, availability, and security enforcement. As part of the migration, equivalent BIG-IP VE instances are deployed on Nutanix, allowing both environments to operate in parallel during the transition.

BIG-IP serves as a centralized traffic control layer, ensuring that application delivery and security policies remain consistent while workloads migrate from VMware to Nutanix. This approach enables controlled traffic redirection and seamless failover with minimal impact to application availability.

The architecture also highlights BIG-IP’s ability to extend the same traffic management and policy framework across multiple platforms, including VMware, Nutanix, and container platforms such as Red Hat OpenShift, supporting hybrid and multi-platform deployment models.

**VMware:** 
Two virtual machines are provisioned using Ubuntu ISO images—one designated as the client and the other as the server. On the server VM, multiple intentionally vulnerable web applications deployed such as Juice Shop using Docker containers with custom port configurations. These applications are used for testing and security assessment purposes and can be accessed from the client VM over the configured ports.

[Installing Client Server Machines in ESXi | F5 BIG-IP Learn](https://github.com/f5devcentral/bigip_automation_examples/blob/main/bigip/workflow-guides/application-delivery-security/workload/Ubuntu-deployment-ESXi.rst)

A virtual machine (VM) is provisioned on VMware ESXi, which is deployed on a Dell PowerEdge R640 bare-metal server. The VM is booted using the BIG-IP OVA image obtained from the official F5 Downloads portal. Once the BIG-IP instance is operational, application workloads hosted on another VM which are deployed within the same ESXi environment and are integrated through a virtual server configured on the BIG-IP. This setup ensures secure access by routing traffic through the virtual server, effectively preventing direct exposure of the applications to external networks.  

[Deploying BIG-IP on VMware | F5 BIG-IP Solutions](https://github.com/f5devcentral/bigip_automation_examples/blob/main/bigip/workflow-guides/application-delivery-security/workload/BIG-IP-Deployment-on-VMware.rst)

**Nutanix on VMware:**
Nutanix Community Edition (CE) 2.1 is deployed as a VM on VMware ESXi, and its console provides the management interface for creating and operating workloads inside the Nutanix environment. Within this Nutanix-managed infrastructure, a new VM is provisioned using a BIG-IP Virtual Edition (VE) image. This BIG-IP VE instance is then configured with the necessary Virtual Servers, Pools, and policies to front-end and manage traffic for multiple applications hosted within Nutanix. BIG-IP delivers comprehensive application protection for these Nutanix-hosted workloads by leveraging its advanced security capabilities, including Web Application Firewall (WAF), Bot Defense and other L4–L7 security services. This ensures that applications running inside the Nutanix ecosystem remain secure, resilient, and optimized for performance.

[Steps to install Nutanix on VMware | F5 BIG-IP Learn](https://github.com/f5devcentral/bigip_automation_examples/blob/main/bigip/workflow-guides/application-delivery-security/workload/Nutanix_CE_2.1_installation_on_VMware.rst)

[Steps to Deploy BIG-IP on Nutanix Vmware | F5 BIG-IP Learn](https://github.com/f5devcentral/bigip_automation_examples/blob/main/bigip/workflow-guides/application-delivery-security/workload/BIG-IP-Deployment-Nutanix.rst)

**OCP (OpenShift Container Platform):**
A 3-node OpenShift Container Platform (OCP) cluster is deployed on a VMware-based infrastructure, providing a robust foundation for containerized workloads.Within the OCP virtualization environment, a virtual machine (VM) is provisioned using a QCOW2 image, enabling flexible and efficient resource utilization. In parallel, application workloads are hosted on a separate Ubuntu-based VM, where they are deployed using Docker. These workloads are integrated with an F5 BIG-IP virtual server, which acts as a centralized and secure entry point for external traffic. 

Please refer to the links below for detailed instructions on setting up the OCP infrastructure—including OCP nodes, cluster creation, and VM deployment as well as deploying BIG-IP on the respective cluster nodes.

[OCP Infra setup & Cluster Creation | F5 BIG-IP Learn](https://github.com/f5devcentral/bigip_automation_examples/blob/main/bigip/workflow-guides/application-delivery-security/workload/OCP-Setup-VMware.rst)

[Configure NNCP & NAD on OCP Cluster | F5 BIG-IP Learn](https://github.com/f5devcentral/bigip_automation_examples/blob/main/bigip/workflow-guides/Migration/OCP/Configuring_NNCP_NAD_configs_in_Red_Hat_OpenShift/configuring_NNCP_NAD_configs_in_ocp.rst)

[Deploy BIG-IP on OCP Cluster | F5 BIG-IP Learn](https://github.com/f5devcentral/bigip_automation_examples/blob/main/bigip/workflow-guides/Migration/OCP/Deploy_F5_BIG_IP_VE_in_Red_Hat_OpenShift/deploy_big_ip.rst)

[Deploy Ubuntu Server Machine on OCP Cluster | F5 BIG-IP Learn](https://github.com/f5devcentral/bigip_automation_examples/blob/main/bigip/workflow-guides/Migration/OCP/Deploy_Ubuntu_Linux_server_machine_in_Red_Hat_OpenShift/ubuntu_deploy.rst)

## Scenario 1: Migration from VMware to Nutanix

![ ](./Assets/migration_overview.png)

This scenario demonstrates the migration of application traffic and workloads from a VMware-based environment to Nutanix AHV using F5 BIG-IP Virtual Edition. BIG-IP enables a phased migration approach by maintaining consistent traffic management, availability, and security policies while applications and infrastructure components transition between platforms.

For complete, step-by-step migration instructions, refer to [Migration In-Detailed](https://github.com/f5devcentral/bigip_automation_examples/blob/main/bigip/workflow-guides/Migration/Migrating_BIG_IP_from_VMware_to_Nutanix.rst).
A high-level overview of the process is outlined below.

## Migration Stages Overview

### Stage 1 – BIG-IP VE HA pair deployment on Nutanix
At this stage BIG-IP Virtual Edition instances are already present on Vmware and a we will deploy a couple of BIG-IPs on Nutanix platform as well.

![ ](./Assets/device_details_active.jpg)

![ ](./Assets/device_details_stby.jpg)

![ ](./Assets/big_ip_vms_nutanix.jpg)

### Stage 2 – Migrate Standby BIG-IP VE from VMware to Nutanix
The Standby BIG-IP VE is migrated first from the VMware source environment to the Nutanix target platform. Configuration and licensing are preserved, allowing the migrated instance to rejoin the high-availability configuration without affecting active application traffic.

![ ](./Assets/nutanix_big_ip_in_standby.jpg)

### Stage 3 – Failover Active BIG-IP VE to Nutanix
Application traffic is failed over from the Active BIG-IP VE running on VMware to the BIG-IP VE running on Nutanix. At this stage, Nutanix becomes the active traffic-handling platform while VMware remains in standby.

![ ](./Assets/switchover_from_vmware_to_nutanix.jpg)

### Stage 4 – Migrate Application Workloads from VMware to Nutanix
Application workloads are transitioned from the VMware platform to the Nutanix platform. While automated tools such as Nutanix Move are recommended for production migrations, manual deployment may be used for testing and validation purposes. BIG-IP continues to provide consistent traffic steering and availability during this phase.

![ ](./Assets/accessing_application.jpg)

### Stage 5 – Migrate Remaining BIG-IP VE from VMware to Nutanix
The remaining BIG-IP VE is migrated from VMware to Nutanix and added back into the high-availability configuration. Upon completion, both BIG-IP instances operate entirely from the Nutanix platform.

![ ](./Assets/final_big_ips_state_verification.jpg)

## Scenario 2: Migration from VMware to Red Hat OpenShift

This scenario demonstrates the migraiton of applicaiton traffic and workloads from a VMware to RedHat Openshift Container Platform using F5 BIG-IP Virtual Edition. With BIG-IP, we follow series of steps to migration from VMware along with application workloads to OCP.

## Migration Stages Overview

### Stage 1 – BIG-IP VE HA pair deployment on Nutanix
At this stage BIG-IP Virtual Edition instances are already present on Vmware and a we will deploy a couple of BIG-IPs on Nutanix platform as well.

![ ](./Assets_VMware_to_OCP/active-big-ip-mac-details.jpg)

![ ](./Assets_VMware_to_OCP/standby-ip-mac-details.jpg)

![ ](./Assets_VMware_to_OCP/application-access-before-testing.jpg)

### Stage 2 – Migrate Standby BIG-IP VE from VMware to OCP

The Standby BIG-IP VE is migratd from VMware to OCP. Configuration and licensing are preserved, allowing the migrated instance to rejoin the high-availability configuration without affecting active application traffic.

![ ](./Assets_VMware_to_OCP/stby-big-ip-in-ocp-GUI.jpg)

### Stage 3 – Failover Active BIG-IP VE to OCP

Application traffic is failed over from the Active BIG-IP VE running on VMware to the BIG-IP VE running on OCP. At this stage, OCP becomes the active traffic-handling platform while VMware remains in standby.

![ ](./Assets/stage-3-switchover.jpg)

### Stage 4 – Migrate Application Workloads from VMware to OCP

Workload applications are migrated from VMware to OCP and made to run to same IP and Port as in previous VMware platform.

![ ](./Assets_VMware_to_OCP/application-access-before-testing.jpg)

### Stage 5 – Migrate Remaining BIG-IP VE from VMware to OCP

The remaining BIG-IP VE is migrated from VMware to OCP and added back into the high-availability configuration. Upon completion, both BIG-IP instances operate entirely from the OCP platform. 

![ ](./Assets_VMware_to_OCP/stby-big-ip-in-ocp-GUI.jpg)

### Conclusion

This workflow demonstrates how F5 BIG-IP Virtual Edition enables a controlled and low-risk migration of application traffic from VMware to Nutanix and OCP. By leveraging BIG-IP high availability and consistent traffic management capabilities, organizations can transition applications across heterogeneous infrastructure platforms while preserving availability, security, and operational consistency.

The phased migration approach enables infrastructure and application components to be migrated independently from VMware to Nutanix and VMware to OCP minimizing service disruption and providing clear validation checkpoints at each stage. This approach ensures application traffic is handled reliably throughout the migration process and continues seamlessly after transitioning to the target platforms.

### References

https://community.f5.com/kb/technicalarticles/f5-big-ip-ve-and-application-workloads-migration-from-vmware-to-nutanix/340465

https://techdocs.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-ve-setup-vmware-esxi-11-5-0/2.html

https://clouddocs.f5.com/cloud/public/v1/nutanix/nutanix_setup.html



