#!/usr/bin/env bash
# using puppet to make to configuration file
include stdlib

file_line { 'NO passwd':
  ensure => present,
  path => '/etc/ssh/ssh_config',
  line => '     PasswordAuthentication no',
  replace => true,
}


file_line { 'Private key holder':
  ensure => present,
  path => '/etc/ssh/ssh_config',
  line => '     IdentityFile ~/.ssh/school',
  replace => true,
}
