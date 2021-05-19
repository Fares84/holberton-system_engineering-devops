# a puppet script to fix a typo that causes a 500 error

exec { 'replace phpp by php':
  command => 'sed -i.bak \'s|phpp|php|g\' /var/www/html/wp-settings.php',
  path    => '/bin/',
}