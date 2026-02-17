Attach an Interface Network to BIG-IP Instance in RedHat OpenShift Platform
#########################################################
This documents contains step by step procedure to attach an Interface Network to BIG-IP instance to communicate to external network or internal to Cluster in RedHat OpenShift Platform (OCP). 

Introduction
-------------------------------
Attaching an interface depends on how it is intended to be used. Interface can be External or Internal to the Cluster Network. Configuring a Network Interface is mentioned `here <https://github.com/chaithanyadileep/bigip_automation_examples/blob/upload/bigip/workflow-guides/Migration/OCP/Configuring_NNCP_NAD_configs_in_Red_Hat_OpenShift/configuring_NNCP_NAD_configs_in_ocp.rst>`__, which specifies NNCP and NAD used for creating a Network.

Steps to attach an Interface
-------------------------------
Below are the series of steps to follow to attach an network to BIG-IP VE,

At first, we can able to see from the Interface dropdown in BIG-IP running in OCP

.. image:: ./Assets/big-ip-before-int-atttach.jpg

Now, let's try to attach an interface to this instance. Select the associated BIG-IP Instance in OCP and Navigate to Configuration > Network. Click on **Add network interface** button.

.. image:: ./Assets/network_configurations.jpg

A window shows to add network interface. From the Network section dropdown, select the NAD Network that has to be attached to this instance and Click on Save button.

.. image:: ./Assets/attach_net_save_config.jpg





