import jenkins.model.*
import org.jenkinsci.plugins.workflow.job.*
import org.jenkinsci.plugins.workflow.cps.*
import hudson.plugins.git.*
import hudson.triggers.SCMTrigger
import hudson.triggers.TimerTrigger
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

// Pipeline Job Name
def jobName = "Next Live Update Pipeline"

// Git credentials setup
def gitUser = "root"
def gitPrivateKeyPath = "/shared_data/git_private_key"

// Add SSH credentials to Jenkins (if not already present)
def credentialsId = "git-ssh-key"
def existingCred = com.cloudbees.plugins.credentials.CredentialsProvider.lookupCredentials(
    com.cloudbees.plugins.credentials.common.StandardCredentials,
    jenkins,
    null,
    null
).find { it.id == credentialsId }

if (!existingCred) {
    println "Adding SSH credentials to Jenkins"
    def privateKey = new File(gitPrivateKeyPath).text
    def sshKey = new BasicSSHUserPrivateKey(
        CredentialsScope.GLOBAL,
        credentialsId,
        gitUser,
        new BasicSSHUserPrivateKey.DirectEntryPrivateKeySource(privateKey),
        null, // No passphrase
        "SSH key for Git repository access"
    )
    def domain = Domain.global()
    def store = jenkins.getExtensionList(
        'com.cloudbees.plugins.credentials.SystemCredentialsProvider'
    )[0].getStore()
    store.addCredentials(domain, sshKey)
} else {
    println "SSH credentials already exist"
}

// Check if the job already exists
def job = jenkins.getItem(jobName)
if (job == null) {
    println "Creating pipeline job: ${jobName}"
    
    // Create a new pipeline job
    job = new WorkflowJob(jenkins, jobName)

    // Define the pipeline to be read from the repository's Jenkinsfile
    def scm = new GitSCM(
        [new UserRemoteConfig("ssh://gitserver:22/home/git/live-update.git", null, null, credentialsId)], 
        [new BranchSpec("*/main")], // Set the branch to 'main'
        false,
        Collections.emptyList(),
        null,
        null,
        Collections.emptyList()
    )

    def pipelineDefinition = new CpsScmFlowDefinition(scm, "Jenkinsfile") // Use 'Jenkinsfile' from SCM
    job.setDefinition(pipelineDefinition)
    jenkins.add(job, job.name)

    println "Pipeline job ${jobName} created successfully."
} else {
    println "Pipeline job ${jobName} already exists."
}

// Add a timer trigger for daily execution at 22:00
def cronExpression = "H 22 * * *" // Jenkins' format for 22:00 daily
def timerTrigger = new TimerTrigger(cronExpression)

if (!job.triggers.containsKey(timerTrigger.class)) {
    println "Adding daily schedule trigger to ${jobName}"
    job.addTrigger(timerTrigger)
    job.save()
} else {
    println "Trigger already exists for ${jobName}"
}

// Save Jenkins state
jenkins.save()
