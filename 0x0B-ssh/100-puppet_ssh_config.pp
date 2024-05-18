#!/usr/bin/env bash
# Setting up client config file
include stdlib

file_line { 'Turn off passwd auth':
	ensure => present,
	path => '/etc/ssh/ssh_config',
	lin => '      PasswordAuthentication no',
	replace => true,
}

file_line { 'Declar identity file':
	ensure => present,
	path => '/etc/ssh/ssh_config',
	line => '     IdentityFile ~/.ssh/school',
	replace => true,
}
