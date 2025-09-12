**Creating Virtual Servers for the vulnerable applications.** 

- | Create multiple **BIG-IP virtual servers**, each associated with a
    specific **pool** that routes traffic to different vulnerable
    applications (e.g., Juice Shop, DVWA, Mutillidae etc) hosted on a
    Ubuntu server. 
  | |A screenshot of a computer AI-generated content may be incorrect.| 

- | Create and apply a WAF policy for each application to effectively
    mitigate malicious attacks. 
  | |image1| 
  |  

- | Access each vulnerable application through its corresponding BIG-IP
    virtual server using the assigned custom ports\ **.** 
  | |image2| 
  | |A screenshot of a login form AI-generated content may be
    incorrect.| 
  | |image3| 

- | Simulate a malicious attack and verify that the WAF successfully
    detects and protects the applications. 
  |   
  | |image4|

..

   | you can find the respective logs here.
   | |image5|

.. |A screenshot of a computer AI-generated content may be incorrect.| image:: media/image1.png
   :width: 5.76667in
   :height: 2.70833in
.. |image1| image:: media/image2.png
   :width: 5.76667in
   :height: 3.275in
.. |image2| image:: media/image3.png
   :width: 5.76667in
   :height: 2.49167in
.. |A screenshot of a login form AI-generated content may be incorrect.| image:: media/image4.png
   :width: 5.76667in
   :height: 2.05in
.. |image3| image:: media/image5.png
   :width: 5.76667in
   :height: 3.04167in
.. |image4| image:: media/image6.png
   :width: 5.76667in
   :height: 2.74167in
.. |image5| image:: media/image7.png
   :width: 6.26667in
   :height: 3.575in
