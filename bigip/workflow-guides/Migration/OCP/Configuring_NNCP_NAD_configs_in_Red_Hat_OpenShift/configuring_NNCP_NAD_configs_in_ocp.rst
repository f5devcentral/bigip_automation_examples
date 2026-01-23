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

Select the Node to which Network should be attached to. In this case, I choose *ocp-node-1*. Click on Edit button to add the Network to this Node.

.. image:: ./Assets/adding_interface_to_nodes.jpg

Click on *Add network adapter* button and select the interface from the dropdown. Once you add the interface, click on Save. It is better to add Interface individually and then carry the NNCP and NAD configurations associated to it.





