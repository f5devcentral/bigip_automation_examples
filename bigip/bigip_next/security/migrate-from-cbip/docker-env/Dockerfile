FROM ubuntu:20.04

# Disable interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Update the repository and install dependencies
RUN apt-get update && apt-get install -y \
    software-properties-common \
    curl \
    gnupg \
    lsb-release \
    nano \
    && rm -rf /var/lib/apt/lists/*

# Install Ansible
RUN apt-add-repository --yes --update ppa:ansible/ansible \
    && apt-get update \
    && apt-get install -y ansible \
    && rm -rf /var/lib/apt/lists/*

# Install Terraform
RUN curl -fsSL https://apt.releases.hashicorp.com/gpg | apt-key add - \
    && apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main" \
    && apt-get update \
    && apt-get install -y terraform \
    && rm -rf /var/lib/apt/lists/*

# Create a new user named 'ubuntu' and set up the home directory
RUN useradd -m -s /bin/bash ubuntu

# Switch to the 'ubuntu' user
USER ubuntu

# Create the SSH keys
RUN ssh-keygen -t rsa -q -f "$HOME/.ssh/id_rsa" -N ""
RUN touch "$HOME/.ssh/cm-key"
RUN chmod 600 "$HOME/.ssh/cm-key"
RUN touch "$HOME/.ssh/cbip-key"
RUN chmod 600 "$HOME/.ssh/cbip-key"

# Switch to the home directory and clone the sources
WORKDIR /home/ubuntu
RUN git clone https://github.com/f5devcentral/bigip_automation_examples.git

# Run Ansible and Terraform version checks
CMD ["sh", "-c", "ansible --version && terraform --version"]

