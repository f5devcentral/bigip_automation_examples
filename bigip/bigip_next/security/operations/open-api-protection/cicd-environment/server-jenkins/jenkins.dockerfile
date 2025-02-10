# Use the official Jenkins LTS image as the base image
FROM jenkins/jenkins:lts

# Switch to the root user to install additional dependencies
USER root

# Disable interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    software-properties-common \
    lsb-release \
    python3-full \
    python3-pip

# Install Ansible
RUN pip install ansible requests --break-system-packages

# Install Node.js v22 and related dependencies
RUN curl -fsSL https://deb.nodesource.com/setup_22.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g npm@latest \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install plugins (recommended and user-specified)
RUN jenkins-plugin-cli --plugins \
    "credentials ssh-credentials workflow-aggregator matrix-auth credentials-binding" \
    "git configuration-as-code ssh-slaves job-dsl locale" \
    "cloudbees-folder build-timeout timestamper ws-cleanup ant gradle" \ 
    "pipeline-graph-view git matrix-auth pam-auth ldap email-ext mailer dark-theme" \
    "configuration-as-code docker-workflow" \
    "ansible" \
    && mkdir -p /usr/share/jenkins/ref/init.groovy.d

# Copy Groovy script and configuration file
COPY admin-user.groovy /usr/share/jenkins/ref/init.groovy.d/
COPY app-pipeline.groovy /usr/share/jenkins/ref/init.groovy.d/
COPY ssh-key.groovy /usr/share/jenkins/ref/init.groovy.d/

ENV CASC_JENKINS_CONFIG="/var/casc_configs"

RUN mkdir /var/casc_configs
COPY global-security.yml /var/casc_configs

# Change back to Jenkins user
USER jenkins
