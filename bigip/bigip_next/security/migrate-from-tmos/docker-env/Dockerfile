FROM ubuntu:22.04

# Disable interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Update the repository and install dependencies
RUN apt-get update && apt-get install -y \
    software-properties-common \
    curl \
    gnupg \
    lsb-release \
    nano \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install Ansible
RUN apt-add-repository --yes --update ppa:ansible/ansible \
    && apt-get update \
    && apt-get install -y ansible

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
RUN mkdir "$HOME/.ssh"

# Switch back to root to copy the SSH keys and adjust permissions
USER root

# Copy current .ssh to docker
COPY ./keys/* "/home/ubuntu/.ssh/"

# Change ownership and permissions of the copied files
RUN chown -R ubuntu:ubuntu /home/ubuntu/.ssh && \
    chmod 700 /home/ubuntu/.ssh && \
    chmod 600 /home/ubuntu/.ssh/*

# Switch back to the 'ubuntu' user
USER ubuntu

# Switch to the home directory and clone the sources
WORKDIR /home/ubuntu
RUN git clone https://github.com/f5devcentral/bigip_automation_examples.git

# Run Ansible and Terraform version checks
CMD ["sh", "-c", "ansible --version && terraform --version"]
