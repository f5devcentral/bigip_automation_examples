BIG-IP License Activation Guide
===============================

Prerequisites
-------------
Before starting the license activation process, ensure:

- You have your **Base Registration Key (BRK)** (format: ``AAAAA-BBBBB-CCCCC-DDDDD-EEEEEEE``)
- The BIG-IP system is **installed and reachable** on the network

Step 1: Verify BIG-IP System
----------------------------
SSH into your BIG-IP (or use the console) and check the system version:

.. code-block:: bash

    tmsh show sys version

Verify that the ``tmm`` process is running:

.. code-block:: bash

    bigstart status

Step 2: Access the BIG-IP Configuration Utility
------------------------------------------------
1. Open a web browser and navigate to:

   ``https://<BIGIP-management-IP>``

2. Log in with the ``admin`` account (or a user with licensing privileges).
3. Navigate to:

   **System → License**

Step 3: Apply Base Registration Key
----------------------------------
1. Click **Activate**.
2. Enter your **Base Registration Key**.
3. You now have two options for activation:

Online Activation (Automatic)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If your BIG-IP has Internet access:

1. Select **Automatic Activation**.
2. Click **Next**. BIG-IP will contact the **F5 License Server**.
3. Upon success, the license is automatically installed, and services are restarted.
4. Verify license status:

.. code-block:: bash

    tmsh show sys license

Offline Activation (Manual)
~~~~~~~~~~~~~~~~~~~~~~~~~~
If your BIG-IP does not have Internet access:

1. Select **Manual Activation**.
2. A **Dossier** will be displayed (a long encoded string).
3. Copy this Dossier and save it locally (e.g., ``dossier.txt``).

4. On a computer with Internet access:

   - Go to `https://activate.f5.com/license`
   - Paste your Dossier into the provided text box
   - Click **Next** and download the **License File** (``license.txt``)

5. Return to the BIG-IP system:

   - Upload or paste the contents of ``license.txt`` into the activation box
   - Click **Install License**

6. Wait for BIG-IP to process the license and restart services.
7. Verify license status:

.. code-block:: bash

    tmsh show sys license

Confirm License Status
---------------------
After the system restarts, confirm the license:

.. code-block:: bash

    tmsh show sys license

Expected output:

.. code-block::

    Registration Key : XXXXX-XXXXX-XXXXX-XXXXX-XXXXX
    Licensed Modules : LTM, GTM, AFM, ASM, etc.
    Service Check Date: 07/11/2025

Optional CLI Activation
----------------------
You can also activate via the CLI:

.. code-block:: bash

    tmsh install sys license registration-key <YOUR-KEY>

For manual dossier-based activation via CLI:

.. code-block:: bash

    tmsh run util bash
    get_dossier > /var/tmp/dossier.txt

Then upload the dossier at `https://activate.f5.com/license` and apply the license.

Save Configuration
------------------
After license activation completes:

.. code-block:: bash

    tmsh save sys config

Verify Licensed Modules
----------------------
Check that the licensed modules are active:

.. code-block:: bash

    tmsh show sys provision

To enable specific modules, use:

.. code-block:: bash

    tmsh modify sys provision ltm level nominal
    tmsh save sys config

Information on License as below,

    Note: For testing purpose, BIG-IP LTM-VE-5G-V18 LIC is used for Nutanix and BIG-IP LTM-VE-3G-V23-LIC-DEV is used for OCP respectively.