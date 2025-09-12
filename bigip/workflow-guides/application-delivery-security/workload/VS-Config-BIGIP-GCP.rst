**Creating Virtual Servers for the Vulnerable Applications.** 

- Create multiple **BIG-IP virtual servers**, each associated with a specific **pool** that routes traffic to different vulnerable applications (e.g., Juice Shop,  DVWA, Mutillidae etc) hosted on a Ubuntu server. 

  .. image:: ./assets/image7_1.png

- Create and apply a WAF policy for each application to effectively mitigate malicious attacks. 
  
  .. image:: ./assets/image7_2.png 

- Access each vulnerable application through its corresponding BIG-IP virtual server using the assigned custom ports.

    .. image:: ./assets/image7_3.png

    .. image:: ./assets/image7_4.png

    .. image:: ./assets/image7_5.png

-  Simulate a malicious attack and verify that the WAF successfully detects and protects the applications. 
    
    .. image:: ./assets/image7_6.png


- You can find the respective logs here.
    
    .. image:: ./assets/image7_7.png
