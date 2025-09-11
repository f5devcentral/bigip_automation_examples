**Red Hat OpenShift Container Platform (OCP) Setup on VMware** 

**Creating Cluster from Red Hat Console:** 

1. | Login to Red Hat Hybrid Cloud Console using the
     link(*https://console.redhat.com*) 
   | *Note: Valid account having subscription is required to create
     OpenShift Cluster* 

2. Select “Red Hat OpenShift” widget  

3. Click “Dashboard” in the left menu and click on “Create cluster”\ |A
   screenshot of a computer AI-generated content may be incorrect.| 

4. Select “Datacenter” column and click on “Create cluster” under
   Assisted Installer\ |image1| 

5. | Enter details of the cluster in Section 1 
   | |image2| 

6. | Select “control plane nodes” and “network configuration” and click
     “Next” 
   | *Note : - For this demo we’re going with 1 Node and Static IP* 
   | |image3| 

7. | In Section 2, provide *DNS, Machine network* and *Default gateway*
     and click “Next” 
   | *Note :- If you’re not sure, please get these details from your
     network team and don’t use the below details as it is in
     screenshot* 
   | |image4| 
   |  

8. | Provide *Host MAC Adress* and *IPv4 address* and click “Next” 
   | *Note :- For more than 1 nodes, you need to provide MAC and IPv4
     address for all hosts* 
   | |image5| 

9. | Under the “Operators” section, click “Next” 
   | *Note :- For more than 1 node, select “Virtualization” and
     proceed* 
   | |image6| 

10. | Under “Host discovery” section, click “Add host” 
    | |image7| 

11. | Provide SSH key and click “Generate Discovery ISO” 
    | |image8| 

12. | Click “Download Discovery ISO”, ISO (size ~125MB) download will
      start 
    | |image9| 
    |  

13. | Now navigate to ESXi and create a VM with required specifications
      based on requirement. 
    | In this demo below specs are used: 
    | 1. CPU -> 9 (**Hardware virtualization should be enabled**) 
    | |image10| 
    | 2. Memory -> 32 GB RAM 
    | 3. Hard disk 1 -> 200 GB (Screenshots shows 100GB, recommended to
      use 200 GB as Client VM also needs to be installed) 
    | 4. Network Adapter 1 -> Default VM Network with MAC Address set to
      the one defined earlier while creating cluster in step 8 
    | 5. CD/DVD Drive 1 -> Select “Datastore ISO file”, where OCP ISO
      file downloaded should be uploaded and used for VM. Enable
      “Connect at power on” 
    | |image11| 
    | 6. VM Options -> Advanced -> Edit Configurations -> Add parameter 
    | key -> disk.enableUUID 
    | value -> TRUE 
    | |image12|\ 7. Click ”Next” and Finish to complete the
      configuration of VM 
    | 8. “Power on” the VM 
    |  

14. | Once the VM starts booting, wait for some time (~2 minutes), the
      VM will be visible in “Host discovery” in Red Hat console with MAC
      Address as hostname. 
    | Note :- If more than 1 node is selected, wait for all the nodes to
      discover and select role. 
    | |image13| 

15. | Click “Next” and under “Storage” section also click “Next” 
    | |image14| 

16. | Verify “Networking”. 
    | *Note :- If more than 1 node, IPv4 address for API and Ingress
      need to be provided in this section* 
    | |image15| 

17. | Review configuration and click “Install cluster” 
    | |image16| 

18. | Installation will start 
    | |image17| 

19. | It’ll take around ~1 hour to complete. Make a note of the console
      login credentials available under “Web Console URL” 
    | |image18| 

20. | To access the cluster console, URL needs to be resolved by
      configuring in hosts file. 
    | Click “Not able to access the Web Console” and copy-paste the
      configuration to hosts file. 
    | |image19| 

21. | Along with those URL mentioned, include *cdi-uploadproxy* URL as
      well which is required for uploading images in OCP cluster 
    | |image20| 

22. | Once the hosts file configuration is saved, access the “Web
      console URL”, click “Accept risk and continue”, you’ll land on
      cluster login page. Credentials for login are available in step
      19. 
    | |A screenshot of a login page AI-generated content may be
      incorrect.| 

23. | After login, verify the Nodes, CPU, Memory and Filesystem. 
    | Note :- To access the cluster from CLI, navigate to “Copy login
      command” under "kube:admin” 
    | |image21| 
    | |image22| 
    | |image23| 

**Commands to install OC** 

1. curl -LO
   https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest/openshift-client-linux.tar.gz 

2. tar -xvf openshift-client-linux.tar.gz 

3. sudo mv oc /usr/local/bin/ 

 

.. |A screenshot of a computer AI-generated content may be incorrect.| image:: media/image1.png
   :width: 6.15in
   :height: 2.8in
.. |image1| image:: media/image2.png
   :width: 6.19167in
   :height: 2.75in
.. |image2| image:: media/image3.png
   :width: 6.26806in
   :height: 2.85972in
.. |image3| image:: media/image4.png
   :width: 3.03333in
   :height: 3.65833in
.. |image4| image:: media/image5.png
   :width: 5.35833in
   :height: 3.9in
.. |image5| image:: media/image6.png
   :width: 5.38333in
   :height: 3.83333in
.. |image6| image:: media/image7.png
   :width: 5.29167in
   :height: 3.69167in
.. |image7| image:: media/image8.png
   :width: 5.325in
   :height: 3.41667in
.. |image8| image:: media/image9.png
   :width: 3.28333in
   :height: 4.7in
.. |image9| image:: media/image10.png
   :width: 3.20833in
   :height: 4.65in
.. |image10| image:: media/image11.png
   :width: 5.23333in
   :height: 3.3in
.. |image11| image:: media/image12.png
   :width: 5.33333in
   :height: 4.53333in
.. |image12| image:: media/image13.png
   :width: 6.26806in
   :height: 3.17014in
.. |image13| image:: media/image14.png
   :width: 6.26806in
   :height: 3.32917in
.. |image14| image:: media/image15.png
   :width: 6.26806in
   :height: 1.41389in
.. |image15| image:: media/image16.png
   :width: 6.15833in
   :height: 3.10833in
.. |image16| image:: media/image17.png
   :width: 5.80833in
   :height: 3.66667in
.. |image17| image:: media/image18.png
   :width: 5.13333in
   :height: 3.625in
.. |image18| image:: media/image19.png
   :width: 5.175in
   :height: 5.55in
.. |image19| image:: media/image20.png
   :width: 6.26806in
   :height: 2.81736in
.. |image20| image:: media/image21.png
   :width: 6.26806in
   :height: 1.30903in
.. |A screenshot of a login page AI-generated content may be incorrect.| image:: media/image22.png
   :width: 5.275in
   :height: 3.25833in
.. |image21| image:: media/image23.png
   :width: 6.26806in
   :height: 3.71528in
.. |image22| image:: media/image24.png
   :width: 6.26806in
   :height: 3.05069in
.. |image23| image:: media/image25.png
   :width: 6.26806in
   :height: 1.84444in
