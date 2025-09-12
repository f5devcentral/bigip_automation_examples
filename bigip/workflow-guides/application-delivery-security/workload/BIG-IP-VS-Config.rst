**BIG-IP Virtual Server Configuration:**
--------------------

Below is a step-by-step process to create a Virtual Server and validate
the effectiveness of the Web Application Firewall (WAF) by simulating
malicious attacks on application endpoints.

- Before creating the virtual server (VS), let’s configure required
  network settings, VLANs, self IPs, and other required BIG-IP features
  via CLI or web interface. 

  .. image:: ./assets/image6_1.png

  .. image:: ./assets/image6_2.png

- Install and configure various vulnerable web applications such as
  Juice Shop, DVWA (Damn Vulnerable Web Application), XVWA (Xtreme
  Vulnerable Web Application), Mutillidae, and others on an Ubuntu
  server. 

  Ensure each application is running on different custom HTTP ports (e.g., 8080, 8081, etc.) to avoid conflicts. 

- Now, on the BIG-IP system, create a virtual server configured with the appropriate node details pointing to the Ubuntu machine hosting the vulnerable apps. 

  **Node and Pool Details:**

  .. image:: ./assets/image6_4.png

  .. image:: ./assets/image6_5.png

  .. image:: ./assets/image6_6.png

  .. image:: ./assets/image6_7.png
   
  .. image:: ./assets/image6_8.png

  .. image:: ./assets/image6_9.png

  .. image:: ./assets/image6_10.png

- Associate the virtual server with a pool that includes these nodes and their respective custom HTTP ports. Confirm that the virtual server is up and operational on the BIG-IP platform. Also, Apply the WAF policy to the created virtual servers.

  .. image:: ./assets/image6_11.png

  .. image:: ./assets/image6_12.png

  .. image:: ./assets/image6_13.png

- Access the vulnerable applications through the BIG-IP virtual server’s IP and verify connectivity and functionality by navigating to the respective HTTP ports. 

  .. image:: ./assets/image6_14.png

  .. image:: ./assets/image6_15.png
