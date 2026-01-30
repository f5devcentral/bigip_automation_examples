Deploy F5 BIG-IP VE in RedHat OpenShift Platform
#########################################################
This documents contains step by step procedure to deploy F5 BIG-IP in RedHat OpenShift Platform (OCP).

Pre-requesites
-------------------------------
Availablitiy of BIG-IP Image in OCP Cluster. For more details on Image Upload, refer to this `link <https://github.com/f5devcentral/bigip_automation_examples/blob/main/bigip/workflow-guides/Migration/OCP/Upload_BIG-IP_Image_to_RedHat_OpenShift/Upload_BIG-IP_Image_to_OCP_console.rst>`__.

BIG-IP Deployment Defintion
-------------------------------
The following deployment defintion creates a BIG-IP pod:

.. code-block:: python

    apiVersion: kubevirt.io/v1
    kind: VirtualMachine
    metadata:
    name: bigip-chthonda-new
    namespace: default
    labels:
        f5type: bigip-ve
    annotations:
        k8s.v1.cni.cncf.io/networks: "default/net-mgmt,default/br0-10-network,default/local-net-20-x"
    spec:
    runStrategy: Always
    template:
        metadata:
        labels:
            f5type: bigip-ve
            bigip-unit: unit-1
        spec:
        domain:
            cpu:
            sockets: 1
            # Adjust cores to the desired number of vCPUs
            cores: 4
            threads: 2
            resources:
            # memory must be 2Gi per core at least
            requests:
            # schedulear will see whether 16 GB is available or not oc describe node/<>
                memory: 16Gi
            limits:
                memory: 32Gi
            devices:
            networkInterfaceMultiqueue: true
            disks:
            - name: bigip-new-datavolume
                disk:
                bus: virtio
            interfaces:
            - name: mgmt
                bridge: {}
            - name: data-ext-ovn
                bridge: {}
            - name: data-int-ovn
                bridge: {}
        volumes:
        - cloudInitNoCloud:
            networkData: |
            version: 2
            ethernets:
                mgmt :
                addresses:
                - 10.144.126.48/24
                data-ext-ovn:
                addresses:
                - 20.20.2.35/24
                data-int-ovn:
                - 10.10.0.95/24      
        - name: bigip1-datavolume
            dataVolume:
            name: "big-ip-17.5.1"
        networks:
        - name: mgmt
            multus:
            # Name of the NAD Network associating to Mgmt network
            networkName: default/net-mgmt
        - name: data-ext-ovn
            multus:
            # Name of the NAD Network associating to External Network
            networkName: default/br0-10-network
        - name: data-int-ovn
            multus:
            # Name of the NAD Network associating to Internal Network
            networkName: default/local-net-20-x
        nodeSelector:
            kubernetes.io/hostname: aa-bb-cc-dd-ee-f1

Save the file and create the BIG-IP Pod:

    $ oc apply -f big-ip-pv.yaml

    persistentvolume/big-ip-image-17.5-pv1 created

BIG-IP Pod is successfully created. This can be verified from Web Console as well.

Initally, console shows the logs as below,

.. image:: ./Assets/big-ip-boot-up.jpg

After sometime, we can able to login to the console as below,

<Login PIC>

Update the password once you login,


Conclusion
-------------------------------
With the follow of above steps, BIG-IP can be successfully deployed in OCP Cluster.

Additional Links
-------------------------------
`Using tmsh to modify BIG-IP Password <https://my.f5.com/manage/s/article/K13121>`__