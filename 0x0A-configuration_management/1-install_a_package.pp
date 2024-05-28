# 1-install_a_package.pp

package { 'werkzeug':
  ensure   => '2.1.1',
  provider => pip3,
}

package { 'flask':
  ensure   => '2.1.0',
  provider => pip3,
  require  => Package['werkzeug'],
}

