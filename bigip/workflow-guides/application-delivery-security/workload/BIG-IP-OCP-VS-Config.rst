**BIG-IP in OCP Virtual Server Configuration:**
-------------------------------------------

Below is a step-by-step process to create a Virtual Server and validate
the effectiveness of the Web Application Firewall (WAF) by simulating
malicious attacks on application endpoints.

- Before creating the virtual server (VS), let’s configure required
  network settings, VLANs, self IPs, and other required BIG-IP features
  via CLI or web interface. 

  .. image:: ./assets/image_ocp1.png

  .. image:: ./assets/image_ocp2.png

- Install and configure various vulnerable web applications such as
  Juice Shop, DVWA (Damn Vulnerable Web Application), XVWA (Xtreme
  Vulnerable Web Application), Mutillidae, and others on an Ubuntu
  server. 

  Ensure each application is running on different custom HTTP ports (e.g., 3000,8080, 8081, etc.) to avoid conflicts. 

- Now, on the BIG-IP system, create a virtual server configured with the appropriate node details pointing to the Ubuntu machine hosting the vulnerable apps. 

  **Node and Pool Details:**

  .. image:: ./assets/image_ocp3.png

  .. image:: ./assets/image_ocp4.png

  .. image:: ./assets/image_ocp5.png

  .. image:: ./assets/image_ocp6.png
   
  .. image:: ./assets/image_ocp7.png

  .. image:: ./assets/image_ocp8.png

  .. image:: ./assets/image_ocp9.png

- Associate the virtual server with a pool that includes these nodes and their respective custom HTTP ports. Confirm that the virtual server is up and operational on the BIG-IP platform. Also, Apply the WAF policy to the created virtual servers.

  .. image:: ./assets/image_ocp10.png

  .. image:: ./assets/image_ocp11.png

  .. image:: ./assets/image_ocp12.png

- Access the vulnerable applications through the BIG-IP virtual server’s IP and verify connectivity and functionality by navigating to the respective HTTP ports. 

  .. image:: ./assets/image_ocp13.png

  .. image:: ./assets/image_ocp14.png
