# script fix-wordpress settings
exec { 'fix-wordpress':
  command => 'sed -i s/class-wp-locale.phpp/class-wp-locale.php/g /var/www/html/wp-settings.php',
  path    => ['/usr/bin', '/usr/sbin', '/bin']
}
