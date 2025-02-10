import jenkins.model.*
import hudson.security.*
import jenkins.security.*
import jenkins.security.apitoken.ApiTokenStore.HashedToken
import hudson.model.User
import org.springframework.security.core.userdetails.UsernameNotFoundException

// Get the Jenkins instance
def instance = Jenkins.getInstance()

// Set up the admin user with a known username and password
def hudsonRealm = new HudsonPrivateSecurityRealm(false)
def userExists = true
try {
    def checkUser = hudsonRealm.load("admin")
    println("User already available")
}
catch(UsernameNotFoundException e) {
    userExists = false
    println("User not available. Creating...")
}

if (!userExists) {
    def user = hudsonRealm.createAccount("admin", "admin")  // Username and password are both 'admin'
    instance.setSecurityRealm(hudsonRealm)

    // Grant admin privileges
    def strategy = new FullControlOnceLoggedInAuthorizationStrategy()
    strategy.setAllowAnonymousRead(false)
    instance.setAuthorizationStrategy(strategy)

    instance.save()

    // Get or create the API token property for the admin user
    def apiTokenProperty = user.getProperty(ApiTokenProperty.class)

    // If the token property doesn't exist, create it
    if (apiTokenProperty == null) {
        apiTokenProperty = new ApiTokenProperty()
        user.addProperty(apiTokenProperty)
        instance.save()
    }

    // Now check for the token, or generate it if not present
    def tokenName = "OWASP_LAB_TOKEN"
    def tokens = apiTokenProperty.tokenStore.getTokenListSortedByName()
    def tokenFound = false

    for (HashedToken token: tokens) {
        println(token.getName())
        if (token.getName() == tokenName) {
            tokenFound = true
            break
        }
    }

    if (!tokenFound) {
        // Create a new API token if it doesn't exist
        token = apiTokenProperty.tokenStore.generateNewToken(tokenName)
        println("Generated API Token: ${token.plainValue}")

        // Optionally, save the token to a file for use in other processes
        new File("/shared_data/admin-token.txt").text = token.plainValue
    } else {
        println("API Token '${tokenName}' already exists for user 'admin'.")
    }

}