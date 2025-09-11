**Steps to** **Deploy a VM in ESXi Using Ubuntu ISO:**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Log in to VMware ESXi Web Client:**

   - Open a browser and enter the ESXi host IP.

      .. image:: ./assets/image1_1.png

   - Log in with your credentials.

2. **Create a New Virtual Machine:**

   - Click **“Create/Register VM”**.

   - Select **“Create a new virtual machine”** and click **Next**.

      .. image:: ./assets/image1_2.png
   
   - Enter a name for your VM (e.g., Ubuntu-VM).

   - Choose the compatibility (default is fine).

   - Select the guest OS family as **Linux**.

   - Choose the guest OS version as **Ubuntu Linux (64-bit)**.

   - | Click **Next**.

      .. image:: ./assets/image1_3.png

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

   - Click **Next**.

      .. image:: ./assets/image1_4.png

5. **Review and Finish:**

   - Review your VM configuration.

   - Click **Finish** to create the VM.

      .. image:: ./assets/image1_5.png

6. **Power On and Install Ubuntu:**

   - Select the newly created VM.

   - Click **Power on**.

   - Open the console to the VM.

   - Follow the Ubuntu installation wizard to install the OS.
