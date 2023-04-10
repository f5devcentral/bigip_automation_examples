This work-flow will setup, test and destroy rate limiting feature on F5 Distributed Cloud Platform.
<br><br>

Prerequisites before running this work-flow:
1. Backend should be already hosted and available on a public IP
2. Update above backend details in terraform.tfvars.json file
3. Also update domain to be used for creating HTTP load balancer in tfvars file
4. Upload/Update F5 XC cert and key in this folder with names matching in variables.tf
5. Make sure custom runner is configured with all needed packages and available in this repo
6. Click on `Actions` tab and run `Test ratelimiting on F5 XC` flow to test this feature
<br>

Resources which are created and destroyed:<br>
1. Origin pool with provided backend details
2. HTTP load balancer
