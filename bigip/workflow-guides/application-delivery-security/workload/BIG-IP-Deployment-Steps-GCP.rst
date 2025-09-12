**BIG-IP Deployment Steps in GCP:**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Prerequisites:**
~~~~~~~~~~~~~~~~~~

- You must have a **Google Cloud account**.

- Create or select an existing **GCP project** for deployment.

- Enable Required APIs like Cloud Marketplace API, IAM API and compute
  Engine API.

**Deployment Steps:**

1. **Open Marketplace**

- Go to GCP console and then to the marketplace.

- Search for “F5 Advanced WAF with LTM, IPI, Threat Campaigns (PAYG,
  200Mbps)”

- | Select the correct image from **F5 Networks**.
.. image:: ./assets/image5_1.png

2. **Launch the Image and Configure the Deployment**

- Click **Launch** to start configuration.

- Give the instance name ,zone and Region, machine type (min.
  n2-standard-4 (4 vCPUs, 16 GB RAM)) and network settings like VPC
  network, subnet etc.

- Review the settings and click on “Deploy” button.

- GCP will spin up the BIG-IP VE instance with the selected image and
  settings.

3. **Access the BIG-IP GUI Page.**

- Once deployed get the external-ip of the instance.

- Do ssh with default credentials (root/default)

- | Modify the admin password for web UI using the below command
  | <<tmsh modify auth password admin>>

- Now try to access the Instance using https://<external-ip>

- Since this is a **PAYG image**, the license is automatically applied.

- | Go to **System > License** and verify the same.
.. image:: ./assets/image5_2.png
