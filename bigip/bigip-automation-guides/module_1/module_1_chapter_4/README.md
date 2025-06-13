# DRAFT. Work In Progress
## Introduction to Observability and Monitoring in F5 BIG-IP
### module 1 chapter 4

When automating BIG-IP, you need to see what’s happening in real-time. If something breaks, you can’t rely on manual checks. Observability helps track system health, detect issues early, and keep automation running smoothly. In this chapter, we’ll explore the basics of observability in BIG-IP and how it helps with automation and troubleshooting.

#### Key Components of Observability
  * **Telemetry** collects real-time data like traffic flow, CPU usage, and memory. BIG-IP can send this to tools like Splunk or Grafana for analysis.
  * **Performance monitoring** tracks how well the system is handling workloads. If CPU spikes or a pool member fails, you’ll know instantly.
  * **Logging** can record every connection and request,can capture details and even trigger alerts.


### BIG-IQ

https://community.f5.com/kb/technicalarticles/what-is-big-iq/279463 

BIG-IQ is a platform that provides a central point of control for managing F5 devices. It simplifies the management of BIG-IP devices, making it easier to deploy, monitor, and troubleshoot applications. It is recommended for organizations with multiple BIG-IP devices or complex application environments. While BIG-IP devices are used for traffic management, BIG-IQ is used for managing and monitoring these devices.

When you have multiple BIG-IP devices, managing them individually can be complex and time-consuming. BIG-IQ simplifies this by providing a single pane of glass to manage all your devices. It helps you automate tasks, monitor performance, and troubleshoot issues across your application infrastructure.


### BIG-IP

#### Monitoring Tools

**-------------TODO----------------**
1. BIG-IP iHealth
2. BIG-IP iStats
3. BIG-IP iQuery
4. External Monitoring Tools

#### Logging in BIG-IP

**-------------TODO----------------**
1. Reviewing BIG-IP system logs
2. Audit
3. Rest API
4. Security

#### External Monitoring: Logging in BIG-IP

**-------------TODO----------------**
1. Reviewing BIG-IP log files related to automation and troubleshooting


### Logging usage with iRules

F5 BIG-IP iRules let you control how traffic flows through your system, and adding logging helps you see what’s happening in real time. Whether you’re troubleshooting issues or just want better visibility, logging with iRules is a simple but powerful tool.

Here’s an example iRule that logs client connections and HTTP requests:

```tcl
  when RULE_INIT {
      # Enable logging
      set static::debug 1
  }

  when CLIENT_ACCEPTED {
      if { $static::debug } {
          log local0. "Connection accepted from [IP::client_addr]"
      }
  }

  when HTTP_REQUEST {
      if { $static::debug } {
          log local0. "HTTP request for host: [HTTP::host]"
      }
  }
```

How It Works
  * RULE_INIT: This sets a debug flag. If it's 1, logging is enabled.
  * CLIENT_ACCEPTED: Logs the client’s IP when they connect.
  * HTTP_REQUEST: Logs the hostname when an HTTP request is received.


Applying the iRule to a Virtual Server

For this iRule to work, you need to attach it to a virtual server. Here’s how you can do it.

  1. Go to Local Traffic > iRules > Create.
  2. Enter a name (e.g., logging_irule).
  3. Paste the iRule code into the Definition field and click Finished.
  4. Now, go to Local Traffic > Virtual Servers and select your virtual server.
  5. Under the Resources tab, click Manage in the iRules section.
  6. Select logging_irule and move it to the Enabled list.
  7. Click Finished to apply it.

Where to Find iRule Logs in TMUI (BIG-IP Web Interface):

1. Navigate to System > Logs > Local Traffic.
2. In the Log Files section, select LTM Log (/var/log/ltm).

You'll see real-time logs, including entries from your iRule. If needed, use the Filter field to search for specific messages, like "logging_irule".

```
Mon Feb 20 18:25:46 PST 2025	info	f5bigip.internal	tmm[11001]	 	Rule /Common/logging_irule <CLIENT_ACCEPTED>: Connection accepted from 192.168.1.59
Mon Feb 20 18:25:46 PST 2025	info	f5bigip.internal	tmm[11001]	 	Rule /Common/logging_irule <HTTP_REQUEST>: HTTP request for host: 192.168.1.84:8080
```

Now BIG-IP will log every client connection and HTTP request, making it much easier to monitor traffic and troubleshoot issues. You can also tweak this iRule to add more details or trigger alerts when needed.

### Monitoring and Alerting

#### iCall 

F5 BIG-IP has a built-in automation tool called iCall that helps with observability and logging. It lets the system react to specific events without needing external scripts or monitoring tools. This is useful for keeping things running smoothly without manual intervention.

A good example is monitoring CPU usage. If the CPU gets too high, we want BIG-IP to log a warning. Here’s how we can do it with iCall.

##### Step 1: Create the Monitoring Script

This script, `cpu_monitor_script`, checks the system’s CPU usage and compares it to a threshold (80%). If the usage goes over, it logs a message.

```bash
tmsh
create /sys icall script cpu_monitor_script
modify /sys icall script cpu_monitor_script
definition {
  set cpu_threshold 80
  set output [exec tmsh show sys performance system]
  foreach line [split $output "\n"] {
      if {[regexp {Utilization\s+(\d+)\s+(\d+)} $line -> current avg]} {
          if {$avg > $cpu_threshold} {
              exec logger -p local0.alert "iCall: High CPU usage detected: ${avg}% (Threshold: ${cpu_threshold}%)"
          } else {
              exec logger -p local0.info "iCall: CPU usage is normal: ${avg}%"
          }
          break
      }
  }
}


show /sys log ltm

create /sys icall handler periodic cpu_monitor_handler interval 60 script cpu_monitor_script
start /sys icall handler periodic cpu_monitor_handler
stop /sys icall handler periodic cpu_monitor_handler

delete /sys icall handler periodic cpu_monitor_handler
delete /sys icall script cpu_monitor_script
```

if {$cpu_rate > $cpu_perf_threshold} {
             if {$DEBUG} {puts "tmsh show sys performance->${cpu_num}: ${cpu_rate}%. Exceeded threshold ${cpu_perf_threshold}%."}
             exec logger -p local0.alert "\"tmsh show sys performance\"->${cpu_num}: ${cpu_rate}%. Exceeded threshold ${cpu_perf_threshold}%."
         }
```

##### Step 2: Run the Script Automatically

Now, we create a handler that runs this script every 60 seconds. This way, the system keeps an eye on CPU load without manual checks.
create sys icall handler periodic cpu_monitor_handler
```bash
  tmsh create sys icall handler periodic cpu_monitor_handler {
      interval 60
      script cpu_monitor_script
  }
```

create /sys icall handler periodic cpu_monitor_handler interval 60 script cpu_monitor_script
start /sys icall handler periodic cpu_monitor_handler

##### Step 3: Check the Logs

Once the script is running, you can check the logs to see if any warnings have been triggered. Logs are stored in `/var/log/ltm`. To view them, run:

```bash
  tail -f /var/log/ltm
```

This will show real-time log updates. If CPU usage crosses 80%, you’ll see an entry like:

```
  Feb 20 12:34:56 bigip notice High CPU usage detected: 85%
```

With this setup, BIG-IP automatically monitors CPU usage and logs a warning if it goes above 80%. No need for external monitoring tools—BIG-IP takes care of it. You can also extend this by adding actions like sending alerts or adjusting system settings when needed.

#### Alerting

F5 BIG-IP can send alerts based on logs or system events. This is useful for monitoring critical services and reacting quickly to issues. Here’s how you can set up alerts in BIG-IP.

To make alerts work, you need to configure an [SMTP server in BIG-IP](https://my.f5.com/manage/s/article/K30371285#config). This is used to send emails when alerts are triggered.

From TMSH, you can create an alert for a specific event. For example, let’s create an alert for config changes.

```bash
alert config_create "object (.*) - create" {
  email toaddress="bigadmin@example.com"
  fromaddress="info@example.com"
  body="A config change has occurred"
}

alert config_delete "object (.*) - obj_delete" {
  email toaddress="bigadmin@example.com"
  fromaddress="info@example.com"
  body="A config change has occurred"
}

alert config_modify "object (.*) - modify" {
  email toaddress="bigadmins@example.com"
  fromaddress="info@example.com"
  body="A config change has occurred"
}
```

This alert watches for config changes and sends an email to BIG-IP admins when it happens.

To trigger this alert, you can run a command like:

```bash
logger -p local0.notice "object 0 - modify"
```

The same way, you can create alerts for other events like high memory usage, failed connections, or security threats. Alerts help you stay on top of system health and respond quickly to issues.