# Configuration file_line from puppet
file_line { 'Identityfile setup':
    ensure   => present,
    path     => '/etc/ssh/ssh_config',
    line     => 'IdentityFile ~/.ssh/holberton',
    multiple => false,
}
file_line { 'Auth Setup Off':
    ensure   => present,
    path     => '/etc/ssh/ssh_config',
    line     => 'PasswordAuthentication no',
    multiple => false,
}