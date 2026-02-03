Deploy Ubuntu Server Machine in RedHat OpenShift Platform
#########################################################
This documents contains step by step procedure to deploy Ubuntu Server in RedHat OpenShift Platform (OCP). This is needed to deploy web based demo applications within it, which acts as a web server.

Pre-requesites
-------------------------------
Availability of Ubunut Server Image in OCP Cluster. For more details on downloading Ubuntu Image, refer to this `link <https://ubuntu.com/download>`__.

Steps to deploy Ubuntu Server
-------------------------------
Below are the detailed steps to bring up Ubuntu Server machine in OCP

1) Create PV and PVC for Ubuntu Storage

2) Create a Ubuntu Server

3) Installation steps

4) Installing a demo application

**Step 1: Creating PV and PVC for Ubuntu Storage**

For creating a Ubuntu machine, as a pre-requisite, we create Persistent Volume Claim (PVC) that is used as Storage/Harddisk for Ubuntu Machine, followed by having a Ubuntu Server defintion file ready,

**Step 1.1: Configuring Local Volumes**

At first, Login to the Node and create a directory of a valid name. This creates a volume in the Node and this volume is being used as storage for Ubuntu machine.

.. image:: ./Assets/ubuntu_harddisk_pv.jpg

**Step 1.2: Creating a PVC for Ubuntu Machine**

To create a PVC, Persistent Volume (PV) should be created first. Below is the definition file to create a PV.

.. code-block:: python

    apiVersion: v1
    kind: PersistentVolume
    metadata:
    name: linux-server-edition-pv           <<<< Name of the PV
    spec:
    capacity:
        storage: 45Gi                       <<<< Volume assigned to the PV
    accessModes:
        - ReadWriteOnce
    persistentVolumeReclaimPolicy: Retain
    storageClassName: tme-storage
    local:
        path: /mnt/data/v13                 <<<< v13 directory is added here
    nodeAffinity:
        required:
        nodeSelectorTerms:
            - matchExpressions:
                - key: kubernetes.io/hostname
                operator: In
                values:
                    - aa-bb-cc-dd-ee-f7     <<<< Name of the Node in which PV should be created
    volumeMode: Filesystem

Save the file and create the PV:

    $ oc apply -f linux-harddisk-pv.yaml

    persistentvolume/linux-server-edition-pv created

With the PV getting created successfully, create a PV Claim (PVC) from it. PVC definiton file is shown below,

.. code-block:: python

    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
    name: linux-server-hd-pvc       <<<< Name of the PVC
    namespace: default
    spec:
    accessModes:
        - ReadWriteOnce
    resources:
        requests:
        storage: 40Gi               <<<< Claimed 40 GB from the total volume of 45
    storageClassName: tme-storage   <<<< Name of the storage class
    volumeMode: Filesystem
    
Save the file and create the PVC:

    $ oc apply -f linux-harddisk-pvc.yaml

    persistentvolumeclaim/linux-server-hd-pvc created

Execute "oc get pvc" command to know the status of PVC,

.. image:: ./Assets/ubuntu_harddisk_pvc.jpg

As you can able to see from the above screenshot, **linux-server-hd-pvc** is created and it is bound to PV created above named **linux-server-edition-pv**.

With this, it is good to proceed with the creation of Ubuntu VM.

**Step 2: Creating a Ubuntu Server**

Creating Defintion file for Ubuntu machine,

**Step 2.1: Ubuntu Server definition file**

.. code-block:: python

    apiVersion: kubevirt.io/v1
    kind: VirtualMachine
    metadata:
    name: ubuntu-server
    namespace: default                                <<<< Name of the Namespace to which Ubuntu machine should be deployed
    spec:
    nodeSelector:
        kubernetes.io/hostname: aa-bb-cc-dd-ee-f7     <<<< Hostname of the device
    running: true
    template:
        metadata:
        labels:
            kubevirt.io/domain: ubuntu              
        spec:
        domain:
            cpu:
            cores: 2
            devices:
            disks:
            - name: rootdisk
                disk:
                bus: virtio
            - name: install-disk
                disk:
                bus: virtio
            interfaces:
            - name: mgmt
                bridge: {}
            resources:
            requests:
                memory: 4Gi
        networks:
        - name: mgmt
            multus:
            networkName: default/net-mgmt               <<<< Name of the NAD Network to which this VM/Pod should be launched in
        volumes:
        - name: rootdisk                                
            dataVolume:     
            name: ubuntu-linux-24.02                    <<<< Image of the Ubuntu ISO file
        - name: install-disk
            dataVolume:                                 
            name: linux-server-hd-pvc                   <<<< PVC used as a Harddisk to the server


Save the file and create the Ubuntu Machine Pod:

    $ oc apply -f linux-server-edition.yaml

    persistentvolume/ubuntu-server created


.. image:: ./Assets/ubuntu_gui.jpg

As you can able to see from the above screenshot, "ubuntu-server" shows status running. Click on "Open Web Console" to perform the installation steps.

**Step 3: Ubuntu Installation steps**

**Step 3.1: Installation process**

This step consists of detailed process of Ubuntu Installation steps. Upon accessing the Web Console, After a few moments, you should see messages like below,

.. image:: ./Assets/bootup_language.jpg

.. image:: ./Assets/ubuntu_installation_network_configuration.jpg

Below step we are configuring storage. Configuring install to have a entier disk for running Ubuntu

.. image:: ./Assets/ubuntu_installation_guided_config.jpg

Installer will calculate the partitions to create and persent as shown below,

.. image:: ./Assets/ubuntu_installation_storage_configuration.jpg

Confirm the changes,

.. image:: ./Assets/ubuntu_installation_storage_configuration_2.jpg

Set up a profile. Ubuntu server needs to hvae at least one known user for the system, and a hostname. 

.. image:: ./Assets/ubuntu_profile_details.jpg

After entering the required information, the screen will now show the progress of the installer. Once installation completes, do not press the **Reboot Now** button at the botton. OCP re initiate the installation process once again, to avoid this follow the process mentioned below,

.. image:: ./Assets/ubuntu_new_install_complete.jpg

**Step 3.2: Update Yaml configs before reboot**

Update the Yaml file in the OCP console, to effectivelty boot from Ubuntu Harddisk PVC but not Ubuntu ISO file. To get it achieved, follow the steps mentioned below,

.. image:: ./Assets/root_disks_configs.jpg

Remove the highlighted configs related to rootdisk, which points to the Ubuntu ISO volume. Simillary, remove the Volume configs associated to rootdisk as well,

.. image:: ./Assets/volume_configs_remove_reboot.jpg

After removing both the rootdisk and volume configs, Click on Save button below to save the configs. Click on Reboot button on the top to reboot the pod.

Pod gets booted up with Ubuntu and ready to be accessed,

.. image:: ./Assets/ubuntu_new_after_bootup.jpg

.. image:: ./Assets/ubuntu_login.jpg

**Step 4: Installing a demo application**

A demo application is installed for testing purpose. In this case, Juice-shop demo app is installed in Ubuntu Machine,

.. image:: ./Assets/juice_shop_app_deploy.jpg

Juice-shop demo app is pulled successfully using docker run cmd and make to run on port 80 as shown above.

Conclusion
-------------------------------
With the follow of above steps, Ubuntu Server can be successfully deployed in OCP Cluster by creating PV and PVC required to it, along with Juice-shop demo app deployed and good to be used for testing.


Additional Links
-------------------------------
`Install Ubuntu Server <https://ubuntu.com/tutorials/install-ubuntu-server#1-overvie>`__



