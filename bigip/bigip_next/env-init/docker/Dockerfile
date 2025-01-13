FROM ubuntu:22.04

# Disable interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Update the repository and install dependencies
RUN apt-get update && apt-get install -y \
    software-properties-common \
    curl wget \
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
RUN wget -O- https://apt.releases.hashicorp.com/gpg | \
    gpg --dearmor | \
    tee /usr/share/keyrings/hashicorp-archive-keyring.gpg > /dev/null

RUN gpg --no-default-keyring \
    --keyring /usr/share/keyrings/hashicorp-archive-keyring.gpg \
    --fingerprint

RUN echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] \
    https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
    tee /etc/apt/sources.list.d/hashicorp.list

RUN apt update
RUN apt-get install -y terraform

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
RUN git clone --branch feature/merge-all https://github.com/yoctoserge/bigip_automation_examples.git

# Run Ansible and Terraform version checks
CMD ["sh", "-c", "ansible --version && terraform --version"]
