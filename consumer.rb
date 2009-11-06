require 'rubygems'
require 'mq'

AMQP.start do
  
  queue = MQ.queue('sport')

  queue.subscribe do |news|
    puts "sport: '#{news}'"
  end

end
