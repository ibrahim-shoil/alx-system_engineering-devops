# Ensure SSH client configuration uses the private key ~/.ssh/school
file_line { 'Declare identity file':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '    IdentityFile ~/.ssh/school',
  match   => '^\\s*IdentityFile\\s+.*$',
  replace => true,
}

# Ensure SSH client configuration refuses password authentication
file_line { 'Turn off passwd auth':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no',
  match   => '^\\s*PasswordAuthentication\\s+.*$',
  replace => true,
}
