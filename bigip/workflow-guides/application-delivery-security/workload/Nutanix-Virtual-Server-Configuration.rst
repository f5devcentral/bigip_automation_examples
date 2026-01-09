**Virtual Server Configuration steps in BIG-IP (Nutanix):**

- | Create a node by specifying the server details where the
    applications are hosted.
 
     .. image:: ./assets/image12_1.png


- | Navigate to Local Traffic > Pools > Pool List, and create individual
    pools for each vulnerable application (e.g., Juice Shop, DVWA,
    Mutillidae, etc).

     .. image:: ./assets/image12_2.png

- | Add appropriate health monitors and ensure that all virtual servers and nodes show **green (available)**
    status. Then go to Local Traffic > Virtual Servers > Virtual Server List and
    create a virtual server for each application.

     .. image:: ./assets/image12_3.png

- | Navigate to each app using the BIG-IP virtual server IP and its
    custom port and confirm that each application loads correctly and
    traffic is being passed through the BIG-IP.

     .. image:: ./assets/image12_5.png

     .. image:: ./assets/image12_6.png

