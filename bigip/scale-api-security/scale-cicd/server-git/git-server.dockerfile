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
RUN mkdir -p /home/git/scale-app.git && \
    cd /home/git/scale-app.git && \
    git init --bare

# Directly interact with the bare repository (no need to clone)
RUN mkdir /tmp/scale-app && \
    cd /tmp/scale-app && \
    git init --initial-branch main && \
    git remote add origin /home/git/scale-app.git

# Copy the Jenkinsfile into the repository
COPY repo/app/jenkinsfile-scalein /tmp/scale-app/
COPY repo/app/jenkinsfile-scaleout /tmp/scale-app/
COPY repo/app/automation /tmp/scale-app/automation

# Set Git user name and email for the git commands
RUN git config --global user.name "Initial Commit" && \
    git config --global user.email "initial@commit.com"

# Commit the Jenkinsfiles into the repository
RUN cd /tmp/scale-app && \
    git add . && \
    git commit -m "Initial commit with Jenkinsfile" && \
    git push origin main

RUN chown -R git:git /home/git/scale-app.git
COPY post-receive /home/git/scale-app.git/hooks/post-receive

# Set the proper permissions for the hook
RUN chmod +x /home/git/scale-app.git/hooks/post-receive && \
    chown git:git /home/git/scale-app.git/hooks/post-receive

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
