**Steps to** **Deploy a VM in ESXi Using Ubuntu ISO:**

1. **Log in to VMware ESXi Web Client:**

   - | Open a browser and enter the ESXi host IP.
     | |image1|

   - Log in with your credentials.

2. **Create a New Virtual Machine:**

   - Click **“Create/Register VM”**.

   - Select **“Create a new virtual machine”** and click **Next**.

..

   |image2|

- Enter a name for your VM (e.g., Ubuntu-VM).

- Choose the compatibility (default is fine).

- Select the guest OS family as **Linux**.

- Choose the guest OS version as **Ubuntu Linux (64-bit)**.

- | Click **Next**.
  | |image3|

3. **Configure VM Storage:**

   - Select the datastore where you want to store the VM files.

   - Click **Next**.

4. **Configure VM Hardware:**

   - Assign CPU and Memory (e.g., 2 CPUs, 4GB RAM).

   - Add a network adapter and connect it to the desired network.

   - For the **CD/DVD drive**, select **Datastore ISO file**.

   - Browse and select the Ubuntu ISO file you uploaded to the
     datastore.

   - Ensure **Connect at power on** is checked.

   - Configure disk size (e.g., 20GB) and storage type (thin or thick
     provisioning).

   - | Click **Next**.
     | |image4|

5. **Review and Finish:**

   - Review your VM configuration.

   - Click **Finish** to create the VM.

..

   |image5|

   |image6|

6. **Power On and Install Ubuntu:**

   - Select the newly created VM.

   - Click **Power on**.

   - Open the console to the VM.

   - Follow the Ubuntu installation wizard to install the OS.

.. |image1| image:: /media/image.png
   :width: 5.51042in
   :height: 3.125in
.. |image2| image:: /media/image2.png
   :width: 6.26042in
   :height: 3.94792in
.. |image3| image:: /media/image3.png
   :width: 5.51042in
   :height: 3.3125in
.. |image4| image:: /media/image4.png
   :width: 5.51042in
   :height: 3.32292in
.. |image5| image:: /media/image5.png
   :width: 6.26042in
   :height: 3.61458in
.. |image6| image:: /media/image6.png
   :width: 6.26042in
   :height: 1.21875in
