# F5 BIG-IP / BIG-IP Next Automation Examples

## Overview

This is a consolidated repo of Workflow Guides for `F5` products: `BigIP` and `BigIP Next`, covering select use-cases with automation and their manual step equivalents. Use the guides and associated automation scripts to become familiar with the use-cases outlined in the table below, and with the automation code provided for these use-cases (Ansible, Terraform, etc.) </br>
</br>
**NOTE: To learn about each use case check the DevCentral article link provided in the table below.** </br>
</br>

## BIG-IP Next Access

**Note:** Next CM API specification can be found over this link [F5® BIG-IP® Next Central Manager API Specifications](https://clouddocs.f5.com/products/bigip-next/mgmt-api/latest/ApiReferences/bigip_public_api_ref/r_openapi-next.html). 


  | **DevCentral Overview Articles**     | **Use Case / Workflow Guides (SaaS Console, Automation)**                      |
  | ------------------------------------ | ------------------------------------------------------------------------------ |
  |[Introducing Next Access Alongside Our Trusted APM](https://community.f5.com/kb/big-ip-next-academytkb-board/big-ip-next-access-introducing-next-access-alongside-our-trusted-apm/328828)                                      |            N/A                                                                    |
  | [SAML Federation made easier](https://community.f5.com/kb/big-ip-next-academytkb-board/big-ip-next-access-saml-federation-made-easier/329007) | [Microsoft EntraID (SAML IdP) with Kerberos SSO](https://github.com/f5devcentral/bigip_automation_examples/tree/main/bigip/bigip_next/next_access/saml-federation/MicrosoftEntra%20ID-IdP-KerberosSSO) |
  |   | [Integration with Okta (SAML IdP)](https://github.com/f5devcentral/bigip_automation_examples/tree/main/bigip/bigip_next/next_access/saml-federation/okta-IdP) |
  |   | [Integration with Okta (SAML IdP) with HTTP Connector providing risk rating](https://github.com/f5devcentral/bigip_automation_examples/tree/main/bigip/bigip_next/next_access/saml-federation/okta-IdP-http-connector) |
  |   | [Multiple IdPs based on matching criteria] |
  | [VPN Use cases](https://community.f5.com/kb/BIG-IP-Next-Academytkb-board/big-ip-next-access-five-minutes-vpn-setup/330291)  | [Edge client with Machine certificate](https://github.com/f5devcentral/bigip_automation_examples/tree/main/bigip/bigip_next/next_access/vpn/edgeclient-certauth) |
  |   | [Machine Tunnel with Machine certificate](https://github.com/f5devcentral/bigip_automation_examples/tree/main/bigip/bigip_next/next_access/vpn/machinetunnel-certauth) |
  
  
## BIG-IP Next WAF

  | **DevCentral Overview Articles**     | **Use Case / Workflow Guides (SaaS Console, Automation)**                      |
  | ------------------------------------ | ------------------------------------------------------------------------------ |
  |[Migrate Apps with WAF Policy from BIG-IP TMOS to BIG-IP Next (Coming Soon) | [Manual Steps and Automation (Ansible) for BIG-IP TMOS to Next Migration](https://github.com/f5devcentral/bigip_automation_examples/tree/main/bigip/bigip_next/security/migrate-from-tmos) |
  |[Deploy and Protect Apps on BIG-IP Next | [Manual Steps and Automation (Terraform) for Deploying a New App with WAF Policy](https://github.com/f5devcentral/bigip_automation_examples/tree/main/bigip/bigip_next/security/deploy-with-new-next-waf) |

## Getting Started

* Access the README for the target Workflow Guides use-case(s) from the tables above.
* Follow the steps in the README and follow Manual and/or Automated workflows


## Support

For support, please open a GitHub issue.  Note, the code in this repository is community supported and is not supported by F5, Inc.  

## Community Code of Conduct

Please refer to the [F5 DevCentral Community Code of Conduct](code_of_conduct.md).

## License

[Apache License 2.0](LICENSE)

## Copyright

Copyright 2014-2023 F5 Networks Inc.

### F5 Networks Contributor License Agreement

Before you start contributing to any project sponsored by F5 Networks, Inc. (F5) on GitHub, you will need to sign a Contributor License Agreement (CLA).

If you are signing as an individual, we recommend that you talk to your employer (if applicable) before signing the CLA since some employment agreements may have restrictions on your contributions to other projects.
Otherwise by submitting a CLA you represent that you are legally entitled to grant the licenses recited therein.

If your employer has rights to intellectual property that you create, such as your contributions, you represent that you have received permission to make contributions on behalf of that employer, that your employer has waived such rights for your contributions, or that your employer has executed a separate CLA with F5.

If you are signing on behalf of a company, you represent that you are legally entitled to grant the license recited therein.
You represent further that each employee of the entity that submits contributions is authorized to submit such contributions on behalf of the entity pursuant to the CLA.
