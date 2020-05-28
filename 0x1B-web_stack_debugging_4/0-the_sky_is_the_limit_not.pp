# Solution Succes ALL Request with Nginx and ApacheBench
exec { '/usr/bin/env sed -i s/15/1000 /etc/default/nginx': }
-> exec { '/usr/bin/env service nginx restart': }
