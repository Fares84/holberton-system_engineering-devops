# puppet manifest that kills a process named killmenow

exec { 'killing killmenow':
  command  => 'pkill killmenow',
  provider => 'shell',
}