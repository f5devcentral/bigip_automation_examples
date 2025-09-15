**Virtual Server Configuration steps in BIG-IP (Nutanix):**

- | Create a node by specifying the server details where the
    applications are hosted.
  | |A screenshot of a computer AI-generated content may be incorrect.|

- | Navigate to Local Traffic > Pools > Pool List, and create individual
    pools for each vulnerable application (e.g., Juice Shop, DVWA,
    Mutillidae, etc).
  | |image1|

- | Add appropriate health monitors (Note: for DVWA add the custom
    monitor GET /login.php\\r\\n with default login credentials
    (admin/password)
  | |image2|

- Then go to Local Traffic > Virtual Servers > Virtual Server List and
  create a virtual server for each application.

- | Ensure that all virtual servers and nodes show **green (available)**
    status.
  | |image3|

- | Navigate to each app using the BIG-IP virtual server IP and its
    custom port and confirm that each application loads correctly and
    traffic is being passed through the BIG-IP.
  | |image4| 
  |  
  | |A screenshot of a login screen AI-generated content may be
    incorrect.|

.. |A screenshot of a computer AI-generated content may be incorrect.| image:: media/image1.png
   :width: 6.26806in
   :height: 1.77708in
.. |image1| image:: media/image2.png
   :width: 6.26806in
   :height: 1.90139in
.. |image2| image:: media/image3.png
   :width: 6.26806in
   :height: 2.53958in
.. |image3| image:: media/image4.png
   :width: 6.26806in
   :height: 1.86319in
.. |image4| image:: media/image5.png
   :width: 5.76667in
   :height: 3.75833in
.. |A screenshot of a login screen AI-generated content may be incorrect.| image:: media/image6.png
   :width: 5.76667in
   :height: 2.375in
