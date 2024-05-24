# 0x10. HTTPS SSL

## Description

This project focuses on understanding HTTPS SSL, its main roles, and the purpose of encrypting traffic. It also covers the concept of SSL termination and how to implement it using HAProxy on Ubuntu 16.04.

## Concepts

- DNS
- Web stack debugging

## Background Context

When website traffic is not secured, it can lead to various security risks and vulnerabilities. This project aims to address those risks by implementing HTTPS SSL.

## Resources

- [What is HTTPS?](https://www.cloudflare.com/learning/ssl/what-is-https/)
- [What are the 2 main elements that SSL is providing](https://www.cloudflare.com/learning/ssl/ssl-decryption-encryption/)
- [HAProxy SSL termination on Ubuntu16.04](https://www.haproxy.com/blog/haproxy-ssl-termination/)
- [SSL termination](https://en.wikipedia.org/wiki/TLS_termination_proxy)

## Learning Objectives

By the end of this project, you should be able to:

- Explain the main roles of HTTPS SSL
- Understand the purpose of encrypting traffic
- Define SSL termination and its significance

## Requirements

- Allowed editors: vi, vim, emacs
- All files will be interpreted on Ubuntu 16.04 LTS
- All files should end with a new line
- A README.md file, at the root of the project folder, is mandatory
- All Bash script files must be executable
- Bash scripts must pass Shellcheck (version 0.3.7) without any error
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining what the script does