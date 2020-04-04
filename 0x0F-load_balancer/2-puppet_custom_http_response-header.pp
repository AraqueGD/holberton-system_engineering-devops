# Add a custom HTTP header with Puppet.
exec { 'config_haproxy':
    command  => 'sudo apt-get update -y; sudo apt-get install haproxy -y; sudo sed -i "35i\     add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-enabled/default; sudo service nginx start',
    provider => shell,
}
