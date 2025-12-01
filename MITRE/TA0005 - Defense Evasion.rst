**Overview of MITRE ATT&CK Tactic :** **TA0005 - Defense Evasion**
-------------------

**Introduction:**

In cybersecurity, attackers know that simply gaining access to a system
is not enough, they must also avoid being detected if they want to
continue their activities. This is where the Defense Evasion tactic
comes into play. Defense Evasion (TA0005) refers to the techniques
attackers use to disguise their actions, blend in with legitimate
processes, or disable security controls so they can operate unnoticed.
In this article, we will explore the key techniques and sub techniques
used for Defense Evasion, helping us better understand how attackers
operate and how organizations can strengthen their defense using F5
solutions.

**Techniques and Sub Techniques:**

**T1548 – Abuse Elevation Control Mechanism**

Abuse of elevation control mechanisms allows adversaries to execute code
or perform actions with privileges beyond those normally granted to
their account. By exploiting such mechanisms, attackers can gain
administrative access, bypass security controls, and maintain
operational capabilities without raising suspicion. These techniques
target system level controls, user consent prompts, or misconfigurations
in operating systems and cloud environments to escalate privileges in a
stealthy manner.

- | **T1548.001 – Setuid and Setgid**
  | On Unix and Linux systems, files and binaries can be configured with setuid or setgid permissions, allowing execution with the file owner’s or group’s privileges. Adversaries exploit misconfigured setuid/setgid binaries or scripts to escalate their privileges to root or other high-level accounts, enabling unauthorized administrative actions.

- | **T1548.002 – Bypass User Account Control (UAC)**
  | Windows User Account Control (UAC) is designed to prevent unauthorizedelevation of privileges. Attackers bypass UAC prompts to execute applications with administrative rights     without user consent. Common approaches include registry manipulation, exploiting auto elevated or trusted system binaries, and leveraging scheduled tasks or other system         services to gain elevated access undetected.

- | **T1548.003 – Sudo and Sudo Caching**
  | On Unix/Linux systems, the sudo mechanism allows users to execute commands with administrative privileges. Attackers abuse cached sudo credentials or misconfigured sudoers entries to perform privileged actions without requiring re authentication, allowing escalation to root level access while minimizing traceable activity.

- | **T1548.004 – Elevated Execution with Prompt**
  | Some elevation methods require legitimate system prompts for administrative approval. Adversaries can trick users into approving these prompts or leverage system prompts in automated workflows, enabling execution of high privilege operations while maintaining the appearance of legitimate activity.

- | **T1548.005 – Temporary Elevated Cloud Access**
  | Misconfigurations in cloud environments or temporary permission grants can provide adversaries with elevated access for a limited period. Exploiting these opportunities allows attackers to access sensitive resources, perform administrative operations, or escalate privileges further before the temporary elevation expires.

- | **T1548.006 – TCC Manipulation**
  | On macOS, the Transparency, Consent, and Control (TCC) system manages access to protected resources, such as the camera, microphone, and contacts. Adversaries manipulate TCC settings or databases to bypass consent prompts, gaining unauthorized access to sensitive system resources without alerting the user.

**T1134 Access Token Manipulation**

Adversaries manipulate access tokens to execute actions with the
privileges of another account. By exploiting token-based authentication,
attackers can impersonate users, elevate privileges, or access
restricted resources without directly compromising credentials. These
techniques target operating system level token mechanisms to bypass
security controls and maintain stealthy access.

- | **T1134.001 – Token Impersonation/Theft**
  | Attackers obtain and use access tokens belonging to other accounts to impersonate them. By stealing or duplicating tokens, adversaries can perform operations with the privileges of the target user without requiring their credentials.

- | **T1134.002 – Create Process with Token**
  | Adversaries create new processes using the access token of another user. This allows execution under a different account’s context, granting the process elevated privileges or access consistent with the token’s permissions.

- | **T1134.003 – Make and Impersonate Token**
  | Attackers generate a new token and assume its identity to executeactions with elevated privileges. This method enables privilege escalation and resource access by crafting tokens that emulate legitimate accounts.

- | **T1134.004 – Parent PID Spoofing**
  | By altering the parent process ID (PID), adversaries create processes that inherit access tokens from legitimate, higher privileged processes. This technique allows the child process to execute with elevated permissions while appearing as a normal system process.

- | **T1134.005 – SID History Injection**
  | Adversaries inject Security Identifier (SID) history entries into an account’s token to inherit privileges from other accounts or groups. This enables unauthorized access to resources and privileges that the account would not normally possess.

**T1197 – BITS Jobs**

Background Intelligent Transfer Service (BITS) is a Windows service used
to transfer files asynchronously between systems and applications,
typically for updates or background downloads. Adversaries can abuse
BITS jobs to persist malicious code, execute payloads, or exfiltrate
data. Because BITS operates in the background and can retry failed
transfers, malicious activity conducted through this service often
blends in with legitimate system operations, reducing the chance of
detection.

**T1612 – Build Image on Host**

Adversaries may attempt to build malicious container images directly on
a compromised host. By leveraging local build tools such as Docker,
attackers can construct custom images that include malware, backdoors,
or other malicious configurations. This approach allows adversaries to
prepare tailored environments for execution while blending in with
normal container operations.

**T1622 – Debugger Evasion**

Adversaries may employ techniques to detect or evade the presence of a
debugger during execution. Debuggers are commonly used by security
analysts and researchers to study program behavior, analyze malware, and
identify vulnerabilities. By detecting or bypassing debugging
environments, attackers can prevent analysis, hinder reverse
engineering, and ensure their malicious code executes as intended
without interruption.

**T1140 – Deobfuscate/Decode Files or Information**

Adversaries may deobfuscate or decode files, scripts, or other forms of
information to reveal and execute malicious functionality. Obfuscation
and encoding are often used to evade detection and hinder analysis,
while deobfuscation restores the original, usable payload or command
sequence.

**T1610 – Deploy Container**

Adversaries may deploy containers within compromised environments to
execute malicious payloads or maintain persistence. By running workloads
inside containers, attackers can isolate malicious activity, evade
detection, and leverage container orchestration platforms for
scalability. This technique takes advantage of the lightweight and
portable nature of containers to blend in with legitimate infrastructure
operations.

**T1006 – Direct Volume Access**

Adversaries may attempt to directly access disk volumes or raw disk
sectors to bypass file system level protections. By operating at this
lower level, attackers can read or manipulate data without triggering
standard security controls, potentially extracting sensitive
information, modifying files, or concealing their activity from
monitoring tools.

**T1484 – Domain or Tenant Policy Modification**

Adversaries may modify domain or tenant level policies within enterprise
environments to gain elevated access, weaken security configurations, or
maintain persistence. These policies are commonly used in both on
premises Active Directory and cloud based tenant services to enforce
administrative and security controls. By altering them, attackers can
bypass defenses, distribute malicious configurations, or ensure
continued access across multiple systems and users.

- | **T1484.001 – Group Policy Modification**
  | Group Policy Objects (GPOs) in Active Directory control security settings, software deployment, and configurations across domain joined systems. Adversaries who gain domain administrator or equivalent privileges may modify GPOs to weaken defenses, deploy malicious scripts, or maintain persistence across the environment. Such changes affect multiple systems simultaneously, amplifying the impact of the attack.

- | **T1484.002 – Trust Modification**
  | Domain and tenant trust relationships define how authentication and authorization are handled between different environments. Adversaries may alter trust policies to extend access, bypass restrictions, or impersonate identities across domains or tenants. By modifying these relationships, attackers can move laterally into otherwise restricted environments while maintaining a high level of stealth.

**T1672 – Email Spoofing**

Adversaries may forge or manipulate email headers and sender information
to make a message appear as though it originates from a trusted source.
Email spoofing is commonly used to deliver phishing content, malicious
attachments, or links, with the intent of deceiving recipients into
taking actions beneficial to the attacker.

**T1480 – Execution Guardrails**

Adversaries may implement guardrails within their malware or tools to
ensure that execution only occurs under specific conditions. These
safeguards are designed to limit exposure, prevent detection, and reduce
the chance of execution in unintended environments such as sandboxes or
analysis systems. By restricting execution, attackers increase the
likelihood that their payloads run only on intended targets.

- | **T1480.001 – Environmental Keying**
  | Execution may be restricted by checking for certain environmental characteristics, such as system language, domain membership, or geographic location. If the required conditions are not met, the malicious payload may terminate or remain dormant. This prevents execution in non-targeted environments, reducing the risk of discovery.

- | **T1480.002 – Mutual Exclusion**
  | Malware may employ mutual exclusion techniques, such as lock files or mutex objects, to ensure only a single instance of the payload executes on a system. This prevents conflicts, avoids redundancy, and can serve as an additional safeguard to maintain operational stability and stealth.

**T1211 – Exploitation for Defense Evasion**

Adversaries may exploit software vulnerabilities to bypass security
mechanisms and avoid detection. By targeting flaws in operating systems,
applications, or drivers, attackers can disable protections, escalate
privileges, or execute malicious code stealthily.

**T1222 – File and Directory Permissions Modification**

Attackers may alter file or directory permissions to gain unauthorized
access or evade detection. Modifying access control settings allows
adversaries to read, write, or execute files that would otherwise be
restricted, supporting persistence, data exfiltration, or stealthy
operations.

-  | **T1222.001 – Windows File and Directory Permissions Modification**
   | On Windows systems, NTFS permissions or registry linked ACLs may be
     adjusted to allow unauthorized users to execute or manipulate
     files. This can enable hidden installation of malware, unauthorized
     changes to critical system files, or prevention of security
     monitoring.

-  | **T1222.002 – Linux and Mac File and Directory Permissions
     Modification**
   | On Linux and macOS systems, adversaries may exploit chmod, chown,
     or other file permission utilities to grant themselves or malware
     elevated access. This may allow execution of protected scripts,
     concealment of malicious content, or bypassing system protections.

**T1564 – Hide Artifacts**

Adversaries may hide files, processes, accounts, or other system
artifacts to avoid detection and complicate forensic analysis. These
techniques manipulate system features, metadata, or user visible
interfaces to obscure malicious activity, making it difficult for
defenders to identify, investigate, or respond effectively.

- | **T1564.001 – Hidden Files and Directories**
  | Files or directories may be marked with hidden attributes, placed in system protected locations, or use naming conventions that avoid casual inspection. Attackers often combine this with legitimate looking filenames or nested folder structures to evade discovery by users and automated tools.

- | **T1564.002 – Hidden Users**
  | Adversaries may create accounts that are invisible to standard administrative tools or modify existing accounts to remove them from login prompts. These hidden accounts provide stealthy persistence and can be used to bypass standard authentication monitoring.

-  | **T1564.003 – Hidden Window**
   | Malicious programs may execute in invisible windows or background
     processes that do not appear in typical task lists. This enables
     interaction with the system while remaining unnoticed by the user,
     effectively hiding UI elements or runtime activity.

-  | **T1564.004 – NTFS File Attributes**
   | Attackers may exploit alternate data streams (ADS) or set special
     NTFS file attributes to store malicious content. This allows
     execution of hidden payloads without affecting the visible file
     content or size, avoiding detection by antivirus or monitoring
     tools.

-  | **T1564.005 – Hidden File System**
   | Adversaries may create or manipulate alternate file systems or
     partitions that are not mounted in standard directories. These
     hidden volumes can store malicious binaries, exfiltrated data, or
     configuration files, keeping them invisible to the operating
     system’s normal view.

-  | **T1564.006 – Run Virtual Instance**
   | Malware may execute within hidden virtual machines or nested
     hypervisors to isolate malicious activity from the host OS. This
     evasion method prevents standard monitoring tools from detecting or
     analyzing the behavior of malicious processes.

-  **T1564.007–VBA Stomping** Attackers may replace VBA source code with
   benign content while retaining compiled malicious macros. This allows
   execution of embedded code when a document is opened, bypassing
   static code inspection and analysis.

-  | **T1564.008 – Email Hiding Rules**
   | Custom rules in mail clients may move, archive, or delete messages
     automatically, concealing phishing attempts or malicious payloads
     from users and administrators. This enables continued stealthy
     communication without raising suspicion.

-  | **T1564.009 – Resource Forking**
   | On macOS, resource forks provide an alternative storage area in
     files. Adversaries may place payloads or scripts in these forks,
     allowing execution while keeping the main file seemingly benign.

-  | **T1564.010 – Process Argument Spoofing**
   | Command line arguments may be altered or obfuscated to make
     malicious processes appear legitimate. This can deceive monitoring
     tools and forensic analysis, masking the purpose and origin of
     running code.

-  | **T1564.011 – Ignore Process Interrupts**
   | Processes may be configured to ignore termination or interrupt
     signals, ensuring that malicious activity persists even if the user
     or system attempts to stop it.

-  | **T1564.012 – File/Path Exclusions**
   | Adversaries may add malicious files or directories to security
     product exclusion lists or manipulate system policies to prevent
     scanning. This ensures malicious payloads remain undetected by
     endpoint protection solutions.

-  | **T1564.013 – Bind Mounts**
   | In containerized or virtualized environments, bind mounts can
     redirect legitimate file paths to attacker-controlled locations.
     This technique conceals malicious files or data from the host
     system and monitoring solutions.

-  | **T1564.014 – Extended Attributes**
   | Extended file attributes and metadata may be modified to hide
     malicious content, obfuscate execution details, or bypass content
     inspection mechanisms. This includes storing execution instructions
     or configuration data in less monitored metadata fields.

**T1574 – Hijack Execution Flow**

Adversaries may hijack legitimate execution flows to run malicious code
within trusted processes. By manipulating how applications load
libraries, services, or executable files, attackers can maintain
stealth, bypass security mechanisms, and execute privileged operations.

-  | **T1574.001 – DLL Hijacking**
   | Malicious DLLs may be placed in directories that are searched
     before legitimate libraries, causing a trusted application to load
     attacker-controlled code. This technique exploits Windows DLL
     search order and allows silent execution of malware.

-  | **T1574.002 – Dylib Hijacking**
   | On macOS, attackers may exploit the dynamic linking of dylib
     libraries to inject malicious code into legitimate processes. This
     allows malware to execute under the guise of trusted applications,
     bypassing security monitoring.

-  | **T1574.003 – Executable Installer File Permissions Weakness**
   | Weak permissions in installer files allow adversaries to replace or
     modify executables during installation. This can result in
     automatic execution of malicious code with the privileges granted
     to the installer.

-  | **T1574.004 – Dynamic Linker Hijacking**
   | Attackers may manipulate dynamic linker settings (e.g., LD_PRELOAD
     on Unix like systems) to load malicious libraries into legitimate
     processes. This enables stealthy code execution without modifying
     the original executable.

-  | **T1574.005 – Path Interception by PATH Environment Variable**
   | By placing a malicious executable in a directory listed earlier in
     the system PATH, attackers ensure it is executed instead of the
     intended legitimate binary. This allows control over trusted
     applications without altering their files.

-  | **T1574.006 – Path Interception by Search Order Hijacking**
   | Attackers exploit how applications locate dependent files or
     libraries, ensuring their malicious code is loaded before
     legitimate components. This technique enables injection into
     trusted processes without direct modification.

-  | **T1574.007 – Path Interception by Unquoted Path**
   | Unquoted service paths with spaces can allow execution of
     attacker-controlled binaries if placed in higher priority
     directories. This vulnerability in Windows path handling enables
     silent code execution under trusted service contexts.

-  | **T1574.008 – Services File Permissions Weakness**
   | Weak permissions on service binaries allow adversaries to replace
     or modify them with malicious executables, which are then executed
     by the system during service startup.

-  | **T1574.009 – Services Registry Permissions Weakness**
   | Attackers may modify registry entries controlling service execution
     paths, redirecting execution to malicious binaries while
     maintaining legitimate service names.

-  | **T1574.010 – COR_PROFILER**
   | The COR_PROFILER environment variable may be exploited to inject
     code into .NET applications at runtime, bypassing standard security
     checks.

-  | **T1574.011 – KernelCallbackTable**
   | Windows KernelCallbackTable entries may be altered to redirect
     system callbacks to attacker-controlled routines, enabling deep
     execution level manipulation.

-  | **T1574.012 – AppDomainManager**
   | The AppDomainManager in .NET environments may be modified to
     execute attacker supplied code when application domains are
     initialized, maintaining stealth and persistence.

**T1562 – Impair Defenses**

Adversaries may deliberately weaken or disable security controls to reduce detection capabilities and evade response. By targeting system level protections, logging mechanisms, or network defenses, attackers can maintain stealth, escalate privileges, and operate without interference. These activities increase the attacker’s operational persistence and complicate post incident analysis.

-  | **T1562.001 – Disable or Modify Tools**
   | Malicious actors may stop or tamper with security software such as
     antivirus, endpoint detection and response (EDR) agents, or host
     intrusion prevention systems. Modifications can include killing
     processes, altering configuration files, or preventing updates,
     ensuring malware operates undetected.

-  | **T1562.002 – Disable Windows Event Logging**
   | Event logs capture critical system and user activity. Attackers may
     turn off or modify logging services (e.g., Windows Event Log) to
     erase traces of malicious actions or prevent security monitoring
     tools from detecting them.

-  | **T1562.003 – Impair Command History Logging**
   | Command histories in shells like Bash, Zsh, or PowerShell may be
     cleared, disabled, or redirected. This prevents defenders from
     auditing executed commands, making it harder to reconstruct
     attacker activity.

-  | **T1562.004 – Disable or Modify System Firewall**
   | Firewalls regulate inbound and outbound traffic. Attackers may
     disable or weaken firewall rules, allowing unauthorized network
     connections, lateral movement, or data exfiltration without
     triggering alerts.

-  | **T1562.006 – Indicator Blocking**
   | Attackers may manipulate the system to block alerts, logs, or
     signatures from security monitoring tools. This prevents security
     teams from observing suspicious behavior, even when detection rules
     exist.

-  | **T1562.007 – Disable or Modify Cloud Firewall**
   | In cloud environments, security groups, network ACLs, or firewall
     rules may be changed to allow attacker traffic while bypassing
     security policies. This facilitates lateral movement, unauthorized
     access, or exfiltration of cloud hosted resources.

-  | **T1562.008 – Disable or Modify Cloud Logs**
   | Logging services in cloud platforms (e.g., AWS CloudTrail, Azure
     Monitor) may be disabled or tampered with, preventing visibility
     into administrative or system level operations.

-  | **T1562.009 – Safe Mode Boot**
   | Malware may force the system to boot into Safe Mode or a minimal
     configuration where security software is not loaded. This ensures
     malicious code executes without interference from endpoint
     protections.

-  | **T1562.010 – Downgrade Attack**
   | Security configurations, protocols, or software may be downgraded
     to less secure versions. For instance, weak encryption protocols
     may be re enabled to facilitate cryptanalysis or unauthorized
     access.

-  | **T1562.011 – Spoof Security Alerting**
   | Attackers may generate fake alerts to mislead users or
     administrators, masking real malicious actions and diverting
     attention from ongoing compromise.

-  | **T1562.012 – Disable or Modify Linux Audit System**
   | The Linux audit system (auditd) may be disabled or reconfigured to
     ignore specific events. This prevents logging of sensitive
     operations like privilege escalations or file modifications.

**T1656 – Impersonation**

Adversaries may impersonate users, accounts, or processes to gain unauthorized access, bypass authentication, or evade detection. By masking them as trusted entities, attackers can execute malicious actions while blending with legitimate activity.

**T1070 – Indicator Removal**

Adversaries remove or tamper with system and application artifacts that could reveal malicious activity. This includes files, logs, history, network traces, or persistence mechanisms. Effective indicator removal makes detection, attribution, and post incident investigation significantly more difficult.

-  | **T1070.001 – Clear Windows Event Logs**
   | Attackers selectively or entirely clear Windows event logs to erase
     traces of compromise. Targeted clearing may focus on security,
     system, or application logs associated with their actions.

-  | **T1070.002 – Clear Linux or Mac System Logs**
   | Attackers clear or edit the System logs in /var/log or equivalent
     directories. This hides evidence of privilege escalation, malware
     execution, or lateral movement.

-  | **T1070.003 – Clear Command History**
   | Adversaries delete shell history files (e.g., .bash_history) or
     PowerShell transcripts to remove evidence of executed commands.

-  | **T1070.004 – File Deletion**
   | Adversaries delete malicious files, temporary scripts, or tools
     using OS utilities or specialized malware functions to prevent
     discovery.

-  | **T1070.005 – Network Share Connection Removal**
   | Attackers remove network share connections used for lateral
     movement or data exfiltration from logs or active sessions to avoid
     detection.

-  | **T1070.006 – Timestomp**
   | Attackers alter file metadata, including creation, modification,
     and access timestamps, to mislead forensic investigators. This
     technique can make malicious files appear legitimate or older than
     they are.

-  | **T1070.007 – Clear Network Connection History and Configurations**
   | Attackers clear temporary network configurations, routing tables,
     or cached connection data to remove traces of remote access or
     lateral movement.

-  | **T1070.008 – Clear Mailbox Data**
   | Adversaries remove email evidence, including sent items, drafts, or
     logs to obscure phishing campaigns or sensitive data exfiltration.

-  | **T1070.009 – Clear Persistence**
   | Adversaries remove artifacts related to persistence mechanisms,
     such as scheduled tasks, startup scripts, or registry keys, may be
     removed once the objective is achieved.

-  | **T1070.010 – Relocate Malware**
   | Attackers may move Malware to different directories, drives, or
     partitions to evade signature-based detection or manual analysis.

**T1202 – Indirect Command Execution**

Attackers may use intermediaries or indirect mechanisms to execute commands on a target system. This can include leveraging built in system utilities, scripts, or scheduled tasks to perform operations while minimizing direct interaction and reducing detection likelihood.

**T1036 – Masquerading**

Masquerading involves making files, processes, accounts, or other system artifacts appear legitimate to evade detection. By imitating trusted system resources, software, or users, attackers can blend malicious actions into normal system operations, avoid triggering alerts, and complicate forensic investigation.

-  | **T1036.001 – Invalid Code Signature**
   | Attackers modify executables or libraries so that they appear
     digitally signed, even if the signature is invalid or forged. This
     can bypass signature-based security checks in antivirus or endpoint
     detection systems, giving malware the appearance of a trusted
     application.

-  | **T1036.002 – Right to Left Override**
   | Attackers can make executable files appear as harmless document
     types (e.g., evilcodе.txт.exe looks like text.doc). This is
     particularly effective for tricking users into opening malicious
     files and bypassing automated file inspection tools.

-  | **T1036.003 – Rename Legitimate Utilities**
   | Attackers replace or wrap legitimate system binaries (e.g., cmd.exe
     or powershell.exe) with malicious versions while keeping the
     original name. This allows execution of attacker controlled code
     under a trusted filename, avoiding detection.

-  | **T1036.004 – Masquerade Task or Service**
   | Attackers name malicious scheduled tasks or system services similar
     to legitimate ones (e.g., Windows Update Helper) while executing
     malicious payloads. This ensures continuous execution without
     raising suspicion.

-  | **T1036.005 – Match Legitimate Resource Name or Location**
   | Attackers mimic files, registry entries, or directories or
     legitimate paths names (e.g., placing a malicious binary in
     C:\Windows\System32\svchost.exe). This confuses defenders and
     security tools, making it difficult to distinguish malicious files
     from legitimate system components.

-  | **T1036.006 – Space after Filename**
   | Attackers add a trailing space or other non-printable characters in
     filenames (e.g., notepad .exe) that can bypass poorly configured
     security filters or automated detection mechanisms.

-  | **T1036.007 – Double File Extension**
   | Attackers uses files with names like report.doc.exe to exploit user
     trust and mislead automated detection systems into treating
     executables as harmless documents.

-  | **T1036.008 – Masquerade File Type**
   | Attackers modify file icons, extensions, and metadata to mimic
     trusted applications, media, or document types. For instance, an
     executable may appear as a PDF or image file to evade user
     suspicion.

-  | **T1036.009 – Break Process Trees**
   | Attackers detach malicious processes from their parent processes,
     by this they can obscure the origin of the process in system
     monitoring tools, making it appear as if the execution is
     legitimate or system generated.

-  | **T1036.010 – Masquerade Account Name**
   | Attackers impersonate user accounts, legitimate usernames (e.g.,
     Administrator1) or service accounts to blend into the environment,
     providing persistent, undetected access.

-  | **T1036.011 – Overwrite Process Arguments**
   | Attackers alter command line arguments or parameters to mislead
     security monitoring systems, hiding the true intent or operation of
     the process.

**T1556 – Modify Authentication Process**

Adversaries may manipulate authentication processes to bypass security controls, evade detection, and maintain undetected access. By tampering with login modules, credential providers, or authentication flows across operating systems, applications, and cloud services, attackers can impersonate legitimate users or create stealthy backdoors. Such actions allow adversaries to avoid triggering alerts while sustaining persistence in the environment.

-  | **T1556.001 – Domain Controller Authentication**
   | Adversaries modify domain controller components or Kerberos
     libraries to bypass normal authentication checks. This allows them
     to authenticate as any user without triggering account monitoring
     alerts, undermining detection mechanisms in Active Directory
     environments.

-  | **T1556.002 – Password Filter DLL**
   | Adversaries install malicious password filter DLLs to intercept
     passwords during user changes. This enables credential harvesting
     and stealthy persistence without generating suspicious
     authentication failures.

-  | **T1556.003 – Pluggable Authentication Modules (PAM)**
   | Adversaries manipulate PAM on Linux/Unix systems to silently
     capture credentials or approve malicious logins, evading system
     authentication logs and monitoring.

-  | **T1556.004 – Network Provider DLL**
   | Adversaries insert or modify network provider DLLs to intercept
     authentication traffic, allowing unauthorized access while
     bypassing security alerts tied to login events.

-  | **T1556.005 – Reversible Encryption**
   | Adversaries exploit reversible password encryption to obtain
     plaintext credentials silently, avoiding detection by standard
     credential monitoring systems.

-  | **T1556.006 – Multi Factor Authentication (MFA) Interception**
   | Adversaries intercept MFA tokens or manipulate MFA processes to
     bypass multi factor security checks without alerting monitoring
     systems.

-  | **T1556.007 – Hybrid Identity**
   | Adversaries manipulate hybrid identity synchronization or
     federation settings to bypass authentication, ensuring stealthy
     access across on premises and cloud systems.

-  | **T1556.008 – Network Provider DLL**
   | Adversaries integrate malicious DLLs into Windows authentication
     flows to capture credentials or inject unauthorized logins, all
     while avoiding detection.

-  | **T1556.009 – Conditional Access Policies**
   | Adversaries weaken or bypass conditional access policies in cloud
     environments to evade MFA enforcement or device compliance checks,
     enabling stealthy access to resources.

**T1578 – Modify Cloud Compute Infrastructure**

Adversaries may manipulate cloud compute infrastructure to evade security controls, remove forensic evidence, or maintain undetected persistence. By altering virtual machines, snapshots, or configuration settings, attackers can operate stealthily while blending malicious activity into legitimate cloud operations.

-  | **T1578.001 – Create Snapshot**
   | Adversaries create snapshots of cloud resources to stage malicious
     activity or exfiltrate data without affecting live production
     systems, avoiding detection by runtime monitoring tools.

-  | **T1578.002 – Create Cloud Instance**
   | Adversaries launch new cloud instances to execute malicious
     operations in isolation from monitored environments, reducing the
     risk of detection.

-  | **T1578.003 – Delete Cloud Instance**
   | Adversaries remove cloud instances after completing malicious
     actions to erase traces, hindering forensic investigation and
     alerting mechanisms.

-  | **T1578.004 – Revert Cloud Instance**
   | Adversaries revert cloud instances to previous snapshots to
     eliminate evidence of compromise, evading audit logs and system
     monitoring.

-  | **T1578.005 – Modify Cloud Compute Configurations**
   | Adversaries adjust compute configurations, such as permissions or
     quotas, to conceal malicious activity, avoid alerts, and maintain
     stealthy operations.

**T1666 – Modify Cloud Resource Hierarchy**

Adversaries may manipulate the structure of cloud resource hierarchies including projects, subscriptions, resource groups, or organizational units to gain elevated control over environments and expand access to sensitive assets. By modifying these hierarchies, attackers can reassign ownership, alter trust boundaries, or restructure permissions in ways that enable persistence, privilege escalation, and long term access across the cloud environment.

**T1112 – Modify Registry**

Adversaries may modify the Windows Registry to evade detection, maintain persistence, or manipulate system behaviour in a stealthy manner. By altering keys or values used by operating systems and applications, attackers can disable security controls, implant malicious configurations, or ensure their actions blend into legitimate system activity. Registry modifications are difficult to detect because changes often mimic normal administrative or application operations.

**T1601 – Modify System Image**

Adversaries may modify system images used for OS deployment or recovery to evade detection and maintain stealthy persistence. By tampering with trusted system images, attackers can implant malicious components or weaken security configurations, ensuring that newly deployed or restored systems inherit the compromised state. This makes detection difficult, as changes occur outside normal runtime monitoring and appear as legitimate system configurations.

- | **T1601.001 – Patch System Image**
  | Adversaries modify system images by embedding malicious code, scripts,or configuration changes designed to evade security monitoring. When these images are deployed, the malicious components execute as part of the system’s normal startup, bypassing security controls and blending into legitimate processes.

- | **T1601.002 – Downgrade System Image**
  | Adversaries revert system images to older versions that lack modern security features or patches. This allows malware or unauthorized configurations to operate undetected, bypassing defenses that rely on current security baselines, and creating opportunities for further stealthy compromise.

**T1599 – Network Boundary Bridging**

Adversaries may bypass network segmentation, firewalls, or other boundary controls to move laterally, exfiltrate data, or maintain persistence while avoiding detection. By bridging network boundaries, attackers can operate in less monitored network segments or directly access sensitive systems without triggering alerts, effectively evading perimeter based defenses.

-  | **T1599.001 – Network Address Translation (NAT) Traversal**
   | Adversaries manipulate NAT configurations or use NAT traversal
     techniques to communicate across network segments that would
     normally restrict traffic. This enables attackers to bypass
     security controls such as firewalls or intrusion detection systems,
     allowing stealthy command and control communications or lateral
     movement without raising suspicion.

**T1027 – Obfuscated Files or Information**

Adversaries may obfuscate, encode, or manipulate files and information to evade detection, bypass signature based security systems, or hide malicious activity. By transforming data or code, attackers make it more difficult for automated defenses and analysts to identify malicious behaviour, allowing malware or commands to operate stealthily within the environment. Obfuscation techniques are frequently used to evade antivirus, endpoint detection, intrusion detection systems, and forensic analysis.

-  | **T1027.001 – Binary Padding**
   | Adversaries add extra, non-functional data to binaries to alter
     their appearance or hash values. This can bypass signature based
     detection without affecting execution, allowing malware to run
     undetected.

-  | **T1027.002 – Software Packing**
   | Adversaries use packers or compressors to transform binaries,
     hiding code and data from static analysis. Packed malware can evade
     antivirus and automated scanning tools until unpacked at runtime.

-  | **T1027.003 – Steganography**
   | Adversaries hide malicious information or code within legitimate
     looking files such as images, audio, or video. This allows
     exfiltration or execution without raising suspicion, evading
     traditional file based detection.

-  | **T1027.004 – Compile After Delivery**
   | Adversaries deliver source code or scripts that are compiled on the
     target system. This prevents pre execution analysis and evades
     defenses that rely on inspecting delivered executables.

-  | **T1027.005 – Indicator Removal from Tools**
   | Adversaries remove identifiable metadata, debug symbols, or other
     indicators from tools and malware. This reduces detectability and
     complicates forensic analysis.

-  | **T1027.006 – HTML Smuggling**
   | Adversaries embed malicious payloads within HTML files, which are
     then downloaded and reconstructed on the client side. This bypasses
     perimeter security controls and email filters.

-  | **T1027.007 – Dynamic API Resolution**
   | Adversaries resolve APIs dynamically at runtime rather than
     statically linking them. This hides API calls from static analysis,
     evading detection based on known function usage.

-  | **T1027.008 – Stripped Payloads**
   | Adversaries remove or strip debugging information and other
     non-essential data from executables or scripts. This reduces
     visibility into the tool’s functionality, making analysis and
     detection more difficult.

-  | **T1027.009 – Embedded Payloads**
   | Adversaries embed additional payloads within other files or
     binaries. These payloads remain dormant or concealed until
     executed, allowing malware to evade inspection.

-  | **T1027.010 – Command Obfuscation**
   | Adversaries modify commands or scripts using encoding,
     substitutions, or other transformations to make them harder to
     detect or analyze. This evades detection by security monitoring
     tools and human reviewers.

-  | **T1027.011 – Fileless Storage**
   | Adversaries store malicious code in memory, registry, or other
     non-disk locations. This avoids detection by traditional file based
     security systems.

-  | **T1027.012 – LNK Icon Smuggling**
   | Adversaries embed malicious payloads within shortcut (.LNK) files
     by disguising them with legitimate icons. This allows execution
     without alerting the user or security tools.

-  | **T1027.013 – Encrypted/Encoded File**
   | Adversaries encrypt or encode files to hide their content from
     static analysis or automated defenses. The payload is decrypted or
     decoded at runtime to execute malicious actions.

-  | **T1027.014 – Polymorphic Code**
   | Adversaries modify code dynamically to produce unique variants with
     the same functionality. This prevents signature based detection and
     complicates analysis of malware samples.

-  | **T1027.015 – Compression**
   | Adversaries compress files or payloads to hide their content from
     scanners or automated analysis tools. Compressed malware may evade
     detection until decompressed at execution.

-  | **T1027.016 – Junk Code Insertion**
   | Adversaries insert meaningless instructions, loops, or data to
     alter binary signatures without affecting execution. This technique
     defeats signature based detection and complicates reverse
     engineering.

-  | **T1027.017 – SVG Smuggling**
   | Adversaries embed malicious scripts or payloads in SVG (Scalable
     Vector Graphics) files. When processed by a browser or application,
     the payload executes without triggering traditional file based
     defenses.

**T1647 – Plist File Modification**

Adversaries on macOS may modify property list (plist) files to persist malware, alter system behaviour, or evade detection. Plist files store configuration data for applications and system processes. By tampering with these files, attackers can ensure that malicious components are executed at startup or modify settings to bypass security controls without triggering alerts.

**T1542 – Pre OS Boot**

Adversaries may compromise firmware or pre boot environments to maintain persistent and stealthy control over a system before the operating system loads. Modifications at this stage allow malware to bypass OS level defenses and detection mechanisms, providing attackers with the ability to persist undetected and manipulate security features.

-  | **T1542.001 – System Firmware**
   | Adversaries modify BIOS or UEFI firmware to execute malicious code
     at system startup. This provides stealthy persistence that bypasses
     operating system level security controls.

-  | **T1542.002 – Component Firmware**
   | Adversaries compromise firmware of peripheral components such as
     network cards, hard drives, or embedded controllers. This allows
     malware to survive reinstallation of the OS and evade detection by
     traditional security tools.

-  | **T1542.003 – Bootkit**
   | Adversaries install bootkits that load before the OS, giving them
     control over the boot process. This can evade OS level monitoring
     and security solutions while ensuring persistent malicious
     activity.

-  | **T1542.004 – ROMMONkit**
   | Adversaries manipulate the ROM Monitor (ROMMON) on networking or
     embedded devices to implant malware in pre boot stages, bypassing
     device level defenses and enabling persistent control.

-  | **T1542.005 – TFTP Boot**
   | Adversaries exploit systems booting via TFTP to deliver compromised
     boot images. This enables execution of malicious code before OS
     level defenses are active, evading detection.

**T1055 – Process Injection**

Adversaries inject malicious code into legitimate processes to evade detection, bypass security controls, and maintain stealthy execution. By running code within trusted processes, attackers can avoid monitoring mechanisms, blend activity with legitimate behaviour, and execute payloads without triggering alerts.

-  | **T1055.001 – Dynamic link Library Injection**
   | Adversaries inject malicious DLLs into the memory space of trusted
     processes. This allows execution of malicious functionality under
     the context of legitimate applications, evading detection.

-  | **T1055.002 – Portable Executable Injection**
   | Adversaries insert malicious Portable Executable (PE) files into
     running processes to execute code stealthily, bypassing antivirus
     and runtime monitoring.

-  | **T1055.003 – Thread Execution Hijacking**
   | Adversaries hijack threads of existing processes to execute
     injected code, blending activity with normal process execution and
     evading security monitoring.

-  | **T1055.004 – Asynchronous Procedure Call**
   | Adversaries leverage APCs to inject code that executes
     asynchronously in target processes. This allows stealthy execution
     without creating new threads that could trigger alerts.

-  | **T1055.005 – Thread Local Storage**
   | Adversaries store malicious code in a process’s thread local
     storage to evade detection and execute in the context of legitimate
     threads.

-  | **T1055.006 – Ptrace System Calls**
   | Adversaries use ptrace or similar system calls on Linux/macOS to
     inject code into other processes, bypassing memory protections and
     avoiding detection.

-  | **T1055.007 – Proc Memory**
   | Adversaries write directly into the memory of a target process to
     execute code without creating new files or processes, evading
     detection by file based or process based security tools.

-  | **T1055.008 – Extra Window Memory Injection**
   | Adversaries leverage memory regions associated with GUI windows to
     inject malicious code, executing within legitimate process memory
     and evading traditional monitoring.

-  | **T1055.009 – Process Hollowing**
   | Adversaries replace the memory of a legitimate process with
     malicious code. The original process appears legitimate while
     executing attacker controlled functionality.

-  | **T1055.010 – Process Doppelgänging**
   | Adversaries use transactional NTFS techniques to create a copy of a
     legitimate process and execute malicious code in its memory,
     bypassing security controls.

-  | **T1055.011 – VDSO Hijacking**
   | Adversaries manipulate the Virtual Dynamic Shared Object (VDSO) to
     execute malicious code within process memory, evading user space
     monitoring.

-  | **T1055.012 – ListPlanting**
   | Adversaries inject code by planting structures in process linked
     lists or memory tables, executing within legitimate process context
     to avoid detection.

**T1620 – Reflective Code Loading**

Adversaries load executable code directly into memory without writing it to disk. This avoids detection by file based antivirus and endpoint detection solutions, enabling stealthy execution and evasion of forensic analysis.

**T1207 – Rogue Domain Controller**

Adversaries may deploy a rogue domain controller to impersonate or replace legitimate authentication services. This allows attackers to issue unauthorized credentials, capture logins, and manipulate authentication without triggering standard security alerts, maintaining persistence and privilege escalation capabilities.

**T1014 – Rootkit**

Adversaries deploy rootkits to hide malware, processes, or system modifications from security tools and monitoring utilities. Rootkits operate at the kernel or system level, intercepting system calls and modifying data structures to maintain stealth, persistence, and the ability to execute privileged operations undetected.

**T1553 – Subvert Trust Controls**

Adversaries manipulate trust mechanisms, certificates, or code signing systems to bypass security policies and evade detection. By undermining trust based protections, malicious code can execute undetected while appearing legitimate.

-  | **T1553.001 – Gatekeeper Bypass**
   | Adversaries bypass macOS Gatekeeper protections to run untrusted or
     unsigned applications, avoiding system warnings and security
     enforcement.

-  | **T1553.002 – Code Signing**
   | Adversaries modify executables or libraries to appear digitally
     signed, even with forged or invalid signatures, bypassing signature
     based security controls and appearing as trusted software.

-  | **T1553.003 – SIP and Trust Provider Hijacking**
   | Adversaries manipulate System Integrity Protection (SIP) or trust
     providers to allow malicious modifications without triggering
     security alerts.

-  | **T1553.004 – Install Root Certificate**
   | Adversaries install rogue root certificates to intercept encrypted
     communications, tamper with trust chains, or bypass TLS/SSL
     verification.

-  | **T1553.005 – Mark of the Web Bypass**
   | Adversaries remove or bypass Mark of the Web security flags,
     enabling files downloaded from the internet to execute without user
     warnings.

-  | **T1553.006 – Code Signing Policy Modification**
   | Adversaries modify code signing policies to permit unsigned or
     malicious code execution, circumventing system enforcement
     mechanisms.

**T1218 – System Binary Proxy Execution**

Adversaries exploit trusted system binaries to proxy execution of malicious code, leveraging legitimate processes to bypass security controls. By using binaries that are already whitelisted or trusted by endpoint protection systems, attackers can execute code, scripts, or assemblies without triggering alerts. This method allows malware to blend seamlessly with normal system activity, evade application whitelisting, and avoid detection by traditional security mechanisms.

-  | **T1218.001 – Compiled HTML File (CHM)**
   | Adversaries execute malicious code embedded in CHM files via
     trusted Windows utilities. This allows code execution under the
     context of a trusted process, bypassing script execution
     restrictions.

-  | **T1218.002 – Control Panel (CPL)**
   | Adversaries exploit Control Panel applets to run malicious DLLs or
     scripts. Execution occurs through legitimate CPL utilities, making
     the activity appear as normal system administration operations.

-  | **T1218.003 – CMSTP**
   | Adversaries abuse CMSTP (Connection Manager Profile Installer) to
     install or execute arbitrary code. Since CMSTP is signed and
     trusted by Windows, execution may bypass application whitelisting
     or endpoint controls.

-  | **T1218.004 – InstallUtil**
   | Adversaries leverage InstallUtil.exe to load and execute malicious
     .NET assemblies without user intervention, using a legitimate
     system utility to proxy execution.

-  | **T1218.005 – Mshta**
   | Adversaries execute malicious scripts using mshta.exe, which runs
     HTML applications. This allows attackers to bypass application
     execution restrictions while running code in the context of a
     trusted utility.

-  | **T1218.007 – Msiexec**
   | Adversaries abuse msiexec.exe to install or execute malicious MSI
     packages. Execution via this trusted Windows installer allows
     malware to evade detection by blending with legitimate software
     installations.

-  | **T1218.008 – Odbcconf**
   | Adversaries use odbcconf.exe to execute scripts or commands as part
     of ODBC configuration tasks, proxying malicious actions through a
     trusted executable.

-  | **T1218.009 – Regsvcs/Regasm**
   | Adversaries use regsvcs.exe or regasm.exe to register and execute
     .NET assemblies, enabling code execution under the context of
     system signed utilities and bypassing execution restrictions.

-  | **T1218.010 – Regsvr32**
   | Adversaries load and execute DLLs using regsvr32.exe. This allows
     execution of remote or local scripts without creating new
     processes, bypassing traditional endpoint detection methods.

-  | **T1218.011 – Rundll32**
   | Adversaries leverage rundll32.exe to execute malicious DLLs,
     enabling attackers to run arbitrary code while remaining under the
     context of a trusted Windows binary.

-  | **T1218.012 – Verclsid**
   | Adversaries exploit verclsid.exe to load and execute COM objects or
     scripts, proxying malicious execution through a legitimate system
     process to evade detection.

-  | **T1218.013 – Mavinject**
   | Adversaries inject code into trusted processes using mavinject,
     enabling execution under the guise of legitimate binaries, reducing
     traceability.

-  | **T1218.014 – MMC**
   | Adversaries leverage Microsoft Management Console (MMC) snap ins to
     execute scripts or load malicious components through trusted
     administrative frameworks.

-  | **T1218.015 – Electron Applications**
   | Adversaries exploit Electron based applications to execute
     JavaScript or scripts. Since Electron apps are commonly installed
     and trusted, attackers can execute malicious actions while evading
     security monitoring.

**T1216 – System Script Proxy Execution**

Adversaries leverage trusted system scripting utilities to execute malicious scripts while bypassing application control policies and security monitoring. By using legitimate scripting hosts, attackers can blend malicious activity with normal system operations, avoid detection, and maintain persistence.

-  | **T1216.001 – PubPrn**
   | Adversaries exploit PubPrn to execute scripts indirectly,
     leveraging the utility to run commands or scripts under the context
     of trusted system processes. This allows malware to operate without
     triggering execution restrictions or endpoint alerts.

-  | **T1216.002 – SyncAppvPublishingServer**
   | Adversaries use SyncAppvPublishingServer to proxy script execution,
     allowing malicious code to run in the context of a trusted process.
     This evades monitoring solutions and endpoint controls that would
     normally block unauthorized script execution.

**T1221 – Template Injection**

Adversaries inject malicious content, scripts, or macros into
templates used by applications. Execution occurs when the template is
loaded by a user, enabling stealthy code execution that bypasses
standard execution controls. Template injection is often used for
evading endpoint monitoring, triggering payloads conditionally, or
spreading malware across users.

**T1205 – Traffic Signaling**

Adversaries manipulate network communication patterns to signal or trigger actions on compromised systems while avoiding detection. By using unusual or covert traffic patterns, attackers can control malware, initiate secondary stages, or exfiltrate data without triggering alerts in conventional network monitoring systems.

-  | **T1205.001 – Port Knocking**
   | Adversaries send a specific sequence of network packets to a target
     system to trigger hidden services or malware functionality. This
     method allows remote signaling without exposing open ports, evading
     firewall or intrusion detection systems.

-  | **T1205.002 – Socket Filters**
   | Attackers implement custom socket filters to selectively
     communicate with compromised hosts. This allows malware to respond
     only to intended signals, reducing exposure to network monitoring
     tools and limiting detection risk.

**T1127 – Trusted Developer Utilities Proxy Execution**

Adversaries exploit trusted developer tools to execute malicious codeindirectly. Using these utilities allows malware to bypass execution restrictions, blend with legitimate processes, and evade security monitoring. Trusted utilities such as MSBuild, InstallUtil, and others are leveraged because they are already whitelisted on most systems.

-  | **T1127.001 – MSBuild**
   | Adversaries compile and execute malicious projects via MSBuild,
     avoiding application whitelisting and detection while running code
     under a trusted process.

-  | **T1127.002 – ClickOnce**
   | Attackers exploit ClickOnce deployment to automatically run
     malicious applications in a trusted framework, bypassing endpoint
     controls that prevent untrusted executables from running.

-  | **T1127.003 – JamPlus**
   | Adversaries leverage JamPlus tools to load and execute malicious
     binaries in a controlled environment, proxying execution through
     trusted processes and evading monitoring.

**T1535 – Unused/Unsupported Cloud Regions**

Adversaries exploit cloud regions that are deprecated, unused, or not actively monitored. These regions often have misconfigurations, weaker security controls, or limited logging, allowing attackers to operate stealthily. By leveraging these environments, attackers can maintain persistence, perform administrative actions, or exfiltrate data with minimal risk of detection.

**T1550 – Use Alternate Authentication Material**

Attackers use alternate authentication materials to bypass standard authentication mechanisms. This allows unauthorized access while minimizing detection risk. By reusing valid tokens, hashes, or session cookies, attackers can impersonate users or services and perform actions normally restricted to legitimate accounts.

-  | **T1550.001 – Application Access Token**
   | Adversaries obtain or reuse application access tokens to
     authenticate against APIs or services without requiring user
     credentials. This allows silent access to cloud or enterprise
     resources while evading traditional login monitoring.

-  | **T1550.002 – Pass the Hash**
   | Adversaries leverage stored password hashes to authenticate
     directly to systems without knowing the plaintext password. This
     facilitates lateral movement across endpoints while bypassing multi
     factor authentication and login auditing.

-  | **T1550.003 – Pass the Ticket**
   | Adversaries abuse Kerberos tickets to access network resources
     without performing standard login processes. This allows attackers
     to impersonate users, escalate privileges, or access sensitive data
     while remaining under the radar.

-  | **T1550.004 – Web Session Cookie**
   | Attackers hijack valid web session cookies to gain access to web
     applications or cloud services. By reusing these cookies, they
     bypass login workflows, including MFA protections, and avoid
     triggering authentication alerts.

**T1078 – Valid Accounts**

Adversaries exploit legitimate accounts to gain access, maintain persistence, and evade detection. Using trusted credentials blends malicious activity with normal user behaviour, making it difficult for security monitoring systems to differentiate between legitimate and malicious operations.

-  | **T1078.001 – Default Accounts**
   | Adversaries exploit default system or application accounts with
     known credentials to gain initial access quickly and bypass
     security mechanisms that rely on account validation.

-  | **T1078.002 – Domain Accounts**
   | Attackers use valid domain accounts to access network resources,
     escalate privileges, and execute administrative actions without
     raising alarms.

-  | **T1078.003 – Local Accounts**
   | Adversaries leverage local system accounts to access endpoints
     directly, bypassing network based monitoring and security controls.

-  | **T1078.004 – Cloud Accounts**
   | Attackers exploit cloud service accounts to access cloud
     infrastructure, modify configurations, or exfiltrate data while
     remaining under the guise of legitimate user activity.

**T1497 – Virtualization/Sandbox Evasion**

Adversaries detect virtualized or sandboxed environments to avoid executing malicious code in analysis systems. Evasion ensures malware remains undetected by automated security solutions, delaying investigation and response.

-  | **T1497.001 – System Checks**
   | Adversaries check for artifacts of virtual machines or sandboxed
     environments, such as virtual hardware identifiers, specific
     drivers, or registry entries, to decide whether to execute
     malicious code.

-  | **T1497.002 – User Activity Based Checks**
   | Attackers monitor for normal user interactions like mouse movement,
     keyboard input, or desktop activity to determine if the environment
     is real or automated, preventing execution in simulated
     environments.

-  | **T1497.003 – Time Based Evasion**
   | Adversaries manipulate timers, system uptime, or delay execution to
     avoid detection by analysis tools that only observe activity for
     short periods.

**T1600 – Weaken Encryption**

Attackers weaken cryptographic mechanisms to simplify attacks or bypass protection controls. By reducing key strength, disabling hardware crypto, or modifying configurations, attackers can access encrypted data or communications while evading detection.

-  | **T1600.001 – Reduce Key Space**
   | Adversaries weaken encryption by using smaller key sizes, making it
     feasible to brute force or decrypt data faster and bypassing secure
     communications or storage protections.

-  | **T1600.002 – Disable Crypto Hardware**
   | Attackers disable hardware based cryptographic protections,
     enabling access to plaintext data or cryptographic operations
     without triggering security alerts.

**T1220 – XSL Script Processing**

Adversaries leverage XSL (Extensible Stylesheet Language) scripts to process or transform XML data maliciously. By embedding scripts or commands into XSL templates, attackers can execute arbitrary code during document processing, bypass security controls, and exfiltrate or manipulate data without detection.

**How F5 Can Help**
-------------------

F5 helps businesses keep their applications safe, fast, and reliable, no
matter where they run on-premises, in the cloud, or at the edge. Using
solutions like **BIG-IP**, **NGINX App Protect**, and **F5 Distributed
Cloud Services**, organizations can protect against cyber threats,
control who can access their apps, and make sure services stay available
for users. F5 also simplifies management, giving teams clear visibility
and control across all environments.

By combining strong security with better performance and easier
management, F5 allows businesses to focus on growth and innovation while
keeping their applications and data secure. Please reach out to your
local F5 team for more details on other mitigation methods for MITRE
Tactic 05 Defense Evasion.

**Conclusion** 
--------------

Modern cyber threats are very sophisticated, often leveraging techniques
to evade detection and maintain persistence within systems.
Understanding these defense evasion strategies is critical for building
effective security measures. F5 solutions help organizations counter
such tactics by providing visibility, traffic inspection, and adaptive
protection across applications and networks. By combining strong
security, simplified management, and consistent enforcement across
on-premises, cloud, and edge environments, F5 enables businesses to
protect their applications and data, stay resilient against stealthy
attacks, and operate with confidence in a constantly evolving threat
landscape.

**Reference links**

-  `MITRE \| ATT&CK Tactic 05 – Defense
   Evasion <https://attack.mitre.org/tactics/TA0005/>`__

-  `MITRE ATT&CK: What It Is, how it Works, Who Uses It and Why \| F5
   Labs <https://www.f5.com/labs/learning-center/mitre-attack-what-it-is-how-it-works-who-uses-it-and-why>`__ 

-  `MITRE ATT&CK® <https://attack.mitre.org/>`__ 

**Tags :** BIG-IP , Cloud , Advanced-WAF , Verified-Designs ,
NGINX-App-Protect , Distributed-Cloud , Security

