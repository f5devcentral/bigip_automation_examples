import jenkins.model.*
import org.jenkinsci.plugins.workflow.job.*
import org.jenkinsci.plugins.workflow.cps.*
import hudson.plugins.git.*
import hudson.triggers.SCMTrigger
import hudson.model.*
import com.cloudbees.plugins.credentials.CredentialsScope
import com.cloudbees.plugins.credentials.domains.*
import com.cloudbees.plugins.credentials.impl.*
import hudson.util.Secret
import jenkins.plugins.git.GitSCMSource
import com.cloudbees.jenkins.plugins.sshcredentials.impl.BasicSSHUserPrivateKey
import com.cloudbees.jenkins.plugins.sshcredentials.impl.BasicSSHUserPrivateKey.DirectEntryPrivateKeySource

// Jenkins instance
def jenkins = Jenkins.get()

// Git credentials setup
def user = "ubuntu"
// def privateKeyPath = "/home/ubuntu/.ssh/id_rsa"
def privateKeyPath = "/shared_data/app_host_private_key"

// Add SSH credentials to Jenkins (if not already present)
def credentialsId = "app-host-ssh-key"
def existingCred = com.cloudbees.plugins.credentials.CredentialsProvider.lookupCredentials(
    com.cloudbees.plugins.credentials.common.StandardCredentials,
    jenkins,
    null,
    null
).find { it.id == credentialsId }

if (!existingCred) {
    println "Adding SSH credentials to Jenkins"
    def privateKey = new File(privateKeyPath).text
    def sshKey = new BasicSSHUserPrivateKey(
        CredentialsScope.GLOBAL,
        credentialsId,
        user,
        new BasicSSHUserPrivateKey.DirectEntryPrivateKeySource(privateKey),
        null, // No passphrase
        "SSH key for App Host access"
    )
    def domain = Domain.global()
    def store = jenkins.getExtensionList(
        'com.cloudbees.plugins.credentials.SystemCredentialsProvider'
    )[0].getStore()
    store.addCredentials(domain, sshKey)
} else {
    println "SSH credentials already exist"
}

// Save Jenkins state
jenkins.save()
