# Webstack Monitoring

## Background Context

“You cannot fix or improve what you cannot measure” is a famous saying in the Tech industry. In the age of data-ism, monitoring how our software systems are doing is an important thing. In this project, we will implement one of many tools to measure what is going on our servers.

Web stack monitoring can be broken down into 2 categories:

- Application monitoring: getting data about your running software and making sure it is behaving as expected
- Server monitoring: getting data about your virtual or physical server and making sure they are not overloaded (could be CPU, memory, disk, or network overload)

## Resources

Read or watch:

- [What is server monitoring](https://www.datadoghq.com/blog/what-is-server-monitoring/)
- [What is application monitoring](https://www.datadoghq.com/blog/what-is-application-monitoring/)
- [System monitoring by Google](https://landing.google.com/sre/sre-book/chapters/monitoring-distributed-systems/)
- [Nginx logging and monitoring](https://www.nginx.com/blog/monitoring-nginx/)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
 Why is monitoring needed
 What are the 2 main areas of monitoring
 What are access logs for a web server (such as Nginx)
 What are error logs for a web server (such as Nginx)

## Requirements

General:

- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 16.04 LTS
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.3.7) without any error
- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
- The second line of all your Bash scripts should be a comment explaining what the script is doing

## Tasks

### 0. Sign up for Datadog and install datadog-agent

For this task head to [Datadog](https://www.datadoghq.com/) and sign up for a free Datadog account. When signing up, you’ll have the option of selecting statistics from your current stack that Datadog can monitor for you. Once you have an account set up, follow the instructions given on the website to install the Datadog agent.

### 1. Monitor some metrics

Among the litany of data your monitoring service can report to you are system metrics. You can use these metrics to determine statistics such as reads/writes per second, which can help your company determine if/how they should scale. Set up some monitors within the Datadog dashboard to monitor and alert you of a few. You can read about the various system metrics that you can monitor [here](https://docs.datadoghq.com/integrations/system/).

### 2. Create a dashboard

Now create a dashboard with different metrics displayed in order to get a few different visualizations.
