FROM debian:bullseye

# Install required packages
RUN apt-get update && apt-get install -y \
    openssh-server git bash curl && \
    apt-get clean

# Add a user for Git
RUN useradd -m -d /home/git -s /bin/bash git && \
    echo "git:password" | chpasswd

# Configure SSH
RUN mkdir /var/run/sshd && \
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config

# Create a bare Git repository
RUN mkdir -p /home/git/script-crud-service.git && \
    cd /home/git/script-crud-service.git && \
    git init --bare

# Directly interact with the bare repository (no need to clone)
RUN mkdir /tmp/script-crud-service && \
    cd /tmp/script-crud-service && \
    git init --initial-branch main && \
    git remote add origin /home/git/script-crud-service.git

# Copy the Jenkinsfile into the repository
COPY repo/app/Jenkinsfile /tmp/script-crud-service/
COPY repo/app/src /tmp/script-crud-service/src
COPY repo/app/automation /tmp/script-crud-service/automation

# Set Git user name and email for the git commands
RUN git config --global user.name "Initial Commit" && \
    git config --global user.email "initial@commit.com"

# Commit the Jenkinsfile into the repository
RUN cd /tmp/script-crud-service && \
    git add . && \
    git commit -m "Initial commit with Jenkinsfile" && \
    git push origin main

RUN chown -R git:git /home/git/script-crud-service.git
COPY post-receive /home/git/script-crud-service.git/hooks/post-receive

# Set the proper permissions for the hook
RUN chmod +x /home/git/script-crud-service.git/hooks/post-receive && \
    chown git:git /home/git/script-crud-service.git/hooks/post-receive

# Create a bare Git repository
RUN mkdir -p /home/git/live-update.git && \
    cd /home/git/live-update.git && \
    git init --bare

# Directly interact with the bare repository (no need to clone)
RUN mkdir /tmp/live-update && \
    cd /tmp/live-update && \
    git init --initial-branch main && \
    git remote add origin /home/git/live-update.git

# Copy the automation scripts
COPY repo/live-update/. /tmp/live-update

# Commit the automation scripts to the repository 
RUN cd /tmp/live-update && \
    git add . && \
    git commit -m "Initial commit of live-update scripts" && \
    git push origin main

RUN chown -R git:git /home/git/live-update.git

# Generate SSH key for the git user
RUN mkdir -p /root/.ssh && \
    ssh-keygen -t rsa -b 4096 -f /root/.ssh/id_rsa -N "" && \    
    cat /root/.ssh/id_rsa.pub >> /root/.ssh/authorized_keys    

# Create shared volume mount point
VOLUME /shared_data

# Expose SSH port
EXPOSE 22

# Add a script that will generate SSH keys and copy the public key to /shared_data
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Start SSH service with entrypoint script
CMD ["/entrypoint.sh"]
