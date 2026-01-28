Uploading Image to OCP Cluster
#########################################################

In this article, we discuss about how to upload any image to OCP cluster, which is required to bring up a VM using it.

Pre-requesites
-------------------------------
1) OCP Cluster Installation
2) BIG-IP VE with which VM should be booted with

**Step 1: Download the BIG-IP Image**

At first, we need to download the BIG-IP VE Image from `here <https://my.f5.com/manage/s/downloads>`__. If you do not have an account, do sign up.

**Step 2: Upload Image to OCP cluster**

Below are the detailed steps to Upload Image to OCP Cluster. For better understanding, it is broken down into series of steps.

**Step 2.1: Create a mount directory in respective Node**

In a 3 Node cluster, select the Node in which Image has to deployed and booted. Login to the Node and create a directory of a valid name.

.. image:: ./Assets/creating_directory.jpg

As you can able to see, directory named **v12** is created.




