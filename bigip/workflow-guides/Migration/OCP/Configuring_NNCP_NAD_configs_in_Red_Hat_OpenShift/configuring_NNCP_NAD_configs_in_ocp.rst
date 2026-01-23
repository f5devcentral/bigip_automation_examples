Connecting OpenShift to External Network
#########################################################

OpenShift can be configured to access external network in additoin to the internal pod network. This is to assign the Lab Network VLANs to be assigned to the VMs created in RedHat OpenShift.

There are series of steps that has to be followed along with configuration of RedHat OpenShift (OCP) associated to it need to be carried out.

Pre-requesites
-------------------------------
OCP 3 Node Cluster should be available. Installation of OCP 3 Node cluster is mentioned in the doc here.

Network configurations such as Port Group and Virtual Switch should be configured in VMware ESXi Machine.

Now, with the above conditions satisfied, we proceed with the introducing Network to the 3 Node cluster first and then to the VMs in that cluster.

Section 1: Connect OpenShift node to a Network with different Physical NICs 
-------------------------------
At first, Let's login to the VMware ESXi Machine where 3 Node cluster is installed.

.. image:: ./Assets/3_node_cluster.jpg

Select the Node to which Network should be attached to. In this case, I choose **ocp-node-1**. Click on Edit button to add the Network to this Node.

.. image:: ./Assets/adding_interface_to_nodes.jpg

Click on **Add network adapter** button and select the interface from the dropdown. Once you add the interface, click on Save. It is better to add Interface individually and then carry the NNCP and NAD configurations associated to it.

**Step 1.1: Ensure Attached interface is showing in OCP console**

Login to OCP console, and navigate to Networking > Node network configuraitons to confirm the Network attachment status.

.. image:: ./Assets/interface_in_ocp_new.jpg

This confirms interface is attached successfully and can move to configuring network interfaces on OpenShift nodes.

**Step 1.2: External network with an OVS bridge on a dedicated NIC**

In this step, we will create an NNCP that creates a new OVS bridge **br1** called on the node, using an unused NIC ens224.


.. code-block:: python

    apiVersion: nmstate.io/v1
    kind: NodeNetworkConfigurationPolicy
    metadata:
    name: br1-net-mgmt
    spec:
    nodeSelector:
        kubernetes.io/hostname: aa-bb-cc-dd-ee-f7  <<<<Adjust Role
    desiredState:
        interfaces:
        - name: br1
        description: |-
            A dedicated OVS bridge with ens224 as a port
            allowing traffic from 10.144.126.0/24 Network
        type: ovs-bridge
        state: up
        bridge:
            options:
            stp: false      <<<< Disable Spanning Tree
            port:
            - name: ens224  <<<< Name of the Network interface
        ovn:
        bridge-mappings:
        - localnet: net-mgmt
            bridge: br1
            state: present


Note: Make stp as false, this will not send the BPDU packets to the Switch connected to it.







