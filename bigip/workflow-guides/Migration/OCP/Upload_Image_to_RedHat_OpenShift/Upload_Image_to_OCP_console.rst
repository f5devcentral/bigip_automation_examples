Uploading BIG-IP VE Image to RedHat OpenShift Platform
#########################################################

In this article, we discuss about how to upload any image to RedHat OpenShift Platform (OCP) cluster, which is required to bring up a VM using it.

Pre-requesites
-------------------------------

1. OCP Cluster Installation

2. Storage Class Availability

3. Have access to the software downloads on `my.f5.com <https://my.f5.com/manage/s/>`__

OCP Installation cluster is mentioned `here <Yet to Update>`__ which also includes Storage Class creation in OCP Cluster.

**Step 1: Download the BIG-IP Image**

1. Log in to your F5 account on `my.f5.com <https://my.f5.com/manage/s/>`__ and navigate to the software downloads page.
2. Select the product, version, image type and location that you want to download.
3. Select "Copy Download Link". The copied link will include authentication token that will be valid for a limited time.
4. Open your terminal and navigate to the directory where you want to save the qcow2 file.

**Step 2: Persistent Storage Using Local Volume**

OCP cluster can be provisioned with the persistent storage by using local volumes. 

Below are the detailed steps to create Local Persistent Volume to Upload Image to OCP Cluster. For better understanding, it is broken down into series of steps.

**Step 2.1: Configuring Local Volumes**

Storage must exist in the underlying infrastructure before the image can be mounted as a volume in OCP. 

In a 3 Node cluster, select the Node in which Image has to deployed and booted. Login to the Node and create a directory of a valid name.

.. image:: ./Assets/creating_directory.jpg

As you can able to see from the above screenshot, directory named **v12** is created in the path /mnt/data.

**Step 2.2: Creating Local Persistent Volume (PV)**

Local Persistent volume allows to access local storage devices such as disk, partition.

Below is the yaml to create PV, we create 2 PVs, one for Image volume and other for scratch,

.. code-block:: python

    apiVersion: v1
    kind: PersistentVolume
    metadata:
    name: big-ip-image-17.5-pv1             <<<< Name of the PV
    spec:
    capacity:
        storage: 100Gi                      <<<< The amount of stroage allocated too this volume
    accessModes:
        - ReadWriteOnce
    persistentVolumeReclaimPolicy: Retain
    storageClassName: tme-storage           <<<< Name of the storage class available
    local:                                  <<<< Volume type being used, in this case it is Local.
        path: /mnt/data/v12                 <<<< Image to the mounted to mentioned path
    nodeAffinity:
        required:
        nodeSelectorTerms:
            - matchExpressions:
                - key: kubernetes.io/hostname
                operator: In
                values:
                    - aa-bb-cc-dd-ee-f1      <<<< Name of the Node in which PV should be created
    volumeMode: Filesystem

    ---

    apiVersion: v1
    kind: PersistentVolume
    metadata:
    name: big-ip-image-17.5-pv2
    spec:
    capacity:
        storage: 100Gi
    accessModes:
        - ReadWriteOnce
    persistentVolumeReclaimPolicy: Retain
    storageClassName: tme-storage
    local:
        path: /mnt/data/v12  
    nodeAffinity:
        required:
        nodeSelectorTerms:
            - matchExpressions:
                - key: kubernetes.io/hostname
                operator: In
                values:
                    - aa-bb-cc-dd-ee-f1 
    volumeMode: Filesystem

Save the file and create the PV:

    $ oc apply -f big-ip-pv.yaml

    persistentvolume/big-ip-image-17.5-pv1 created

    persistentvolume/big-ip-image-17.5-pv2 created

On successful creation of PV, execute "oc get pv" to know its status,

.. image:: ./Assets/persistent_volume.jpg

As you can able to see, the volume status shows available, and it is good to proceed further on uploading BIG-IP Image to OCP Cluster.

**Step 2.3: Upload Image to OCP cluster**

From the OCP Console, Navigate to Virtualization > Bootable Volumes. From the "Add volume" button click on "with form".

.. image:: ./Assets/bootable_volume_page.jpg

A window opens to select the Image location, Click on Upload button to upload the image.

Select the StorageClass as "tme-storage", Select the Disk size around 90 GiB. This is due to when the image uploads it expands to around 83 GiB.

Click on Save button to start uploading the image.

.. image:: ./Assets/add_volume.jpg

Once the image upload is successful, we can able to verify the availability of image either using CLI or OpenShift Web console.

.. image:: ./Assets/oc_get_dv.jpg

As you can able to see, by executing "oc get pv" cmd, we can able to see **big-ip** image is uploaded successfully and ready to be deployed.

Conclusion:
--------------------
With the detailed steps mentioned above, uploading of any image to the OCP cluster can be achieved.


Additional Links:
--------------------
`Downloading BIG-IP ISO file from my.f5.com <https://my.f5.com/manage/s/article/K000138258>`__

`Configuring Local Volumes in RedHat OpenShift Platform <https://docs.redhat.com/en/documentation/openshift_container_platform/3.11/html/configuring_clusters/install-config-configuring-local>`__

`Persistent Volumes | Kubernetes <https://kubernetes.io/docs/concepts/storage/persistent-volumes/>`__

`Configuring Persistent Storage Overview <https://docs.redhat.com/en/documentation/openshift_container_platform/3.11/html/configuring_clusters/configuring-persistent-storage#install-config-persistent-storage-index>`__

`Configuring Persistent Storage using Local Volume <https://docs.redhat.com/en/documentation/openshift_container_platform/3.11/html/configuring_clusters/configuring-persistent-storage#install-config-persistent-storage-persistent-storage-local>`__

`Configuring persistent storage using host path <https://docs.redhat.com/en/documentation/openshift_container_platform/3.11/html/configuring_clusters/configuring-persistent-storage#using_hostpath>`__
