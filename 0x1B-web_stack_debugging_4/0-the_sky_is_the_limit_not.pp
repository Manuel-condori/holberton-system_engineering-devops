# Sky is the limit, let's bring that limit higher
exec { 'correct file and restart':
  command  => 'sed -i s/15/4096/g /etc/default/nginx; sudo service nginx restart',
  provider => 'shell'
}
