**Nutanix (VMware) Deployment Steps:** 

**Prerequisites:** 

- Nutanix CE cluster up and running under VMware ESXi. 

- Should have BIG-IP VE image in QCOW2 format. 

- Nutanix Image Service should be available. 

- A configured virtual network (VLAN) in Nutanix CE. 

**Deployment Steps:** 

1. **Download BIG-IP VE Image for AHV** 

- Go to the F5 Downloads portal <https://downloads.f5.com> 

- Login and Navigate to: 

- **BIG-IP Virtual Edition** and Select the version you want (e.g.,
  16.x, 17.x) Note: 16.x is stable and recommended  

- Choose Platform as KVM (since AHV supports QCOW2 images, same as
  KVM). 

- Download the **QCOW2** image file (typically ends in .qcow2.zip or
  .qcow2.gz) and extract it. 

2. **Upload Image to Nutanix CE** 

- In Prism Element, go to: 

- Settings > Image Configuration (or just click on "Images" under the
  settings gear icon). 

- Click and Add Image. 

- | Provide the values for name, storage container and Image source and
    then click on save button. 
  | |A screenshot of a computer AI-generated content may be incorrect.| 

3. **Create the BIG-IP Virtual Machine** 

- Go to VM from dropdown list and click on  Create VM. 

- | Provide the VM name, set CPU and Memory and Add the Disk.
  | |image1| 
  | |image2| 

- Add a Network Interface (NIC) and provide the required details and
  then click on **Save.** 

..

   | |image3| 
   |  

- Finally click on Save button. 

4. **Access the BIG-IP Web UI** 

- Access the BIG-IP Web UI using a browser. 

- < https://ip_addr:8443/> 

- Log in using the **admin** credentials configured during initial
  setup. 

- Navigate to **System > License**. 

- Choose either: 

- Manual Activation: Upload a license file provided by F5 

- Automatic Activation: Use an F5 license key with internet access. 

- Select and provision the required software modules based on your
  license: 

- LTM (Local Traffic Manager) 

- ASM (Application Security Manager) 

- Advanced WAF, etc. 

- Click Submit and allow the system to provision the selected modules. 

- Navigate to Local Traffic > Pools > Pool List, and create individual
  pools for each vulnerable application (e.g., Juice Shop, etc). 

- Specify the node IP address (Ubuntu server details hosting the apps). 

- Set the correct custom HTTP port for each app (e.g., 3000 for Juice
  Shop, 3001 for DVWA, etc.). 

- Add appropriate health monitors (Note: for DVWA add the custom monitor
  GET /login.php\\r\\n with default login credentials
  (admin/password)   

- Then go to Local Traffic > Virtual Servers > Virtual Server List and
  create a virtual server for each application. 

- | Ensure that all virtual servers and nodes show **green (available)**
    status. 
  |  
  | |image4| 
  |  

- | Navigate to each app using the BIG-IP virtual server IP and its
    custom port and confirm that each application loads correctly and
    traffic is being passed through the BIG-IP. 
  | |image5|   

 

.. |A screenshot of a computer AI-generated content may be incorrect.| image:: media/image1.png
   :width: 6.26181in
   :height: 3.3in
.. |image1| image:: media/image2.png
   :width: 4.68472in
   :height: 5.76181in
.. |image2| image:: media/image3.png
   :width: 5.39236in
   :height: 5.76181in
.. |image3| image:: media/image4.png
   :width: 4.03056in
   :height: 3.85417in
.. |image4| image:: media/image5.png
   :width: 6.26806in
   :height: 2.19167in
.. |image5| image:: media/image6.png
   :width: 6.26806in
   :height: 2.96042in
